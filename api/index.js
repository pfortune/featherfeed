import dotenv from 'dotenv';
dotenv.config();

import { createClient } from '@supabase/supabase-js';
import Hapi from '@hapi/hapi';
import Nes from '@hapi/nes';

// Create a single supabase client for interacting with your database
const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_KEY
);

// Create a new Hapi server with CORS enabled
const server = Hapi.server({
  port: process.env.PORT || 3000,
  routes: {
    cors: {
      origin: ['https://featherfeed.ie'],
      additionalHeaders: ['cache-control', 'x-requested-with'],
    },
  },
});

await server.register(Nes);

server.subscription('/detections/updates');

// Define the default root route
server.route({
  method: 'GET',
  path: '/',
  handler: (request, h) => {
    return `
            <h1>API Endpoints</h1>
            <ul>
                <li><a href="/status">/status</a> - Check API status</li>
                <li><a href="/detections">/detections</a> - Fetch all detections</li>
                <li>/detection/{id} - Fetch a specific detection by ID</li>
            </ul>
        `;
  },
});

// Define the status route
server.route({
  method: 'GET',
  path: '/status',
  handler: (request, h) => {
    return { status: 'OK' };
  },
});

// Route to fetch all detections
server.route({
  method: 'GET',
  path: '/detections',
  handler: async (request, h) => {
    const { data, error } = await supabase
      .from('detections')
      .select('*')
      .order('date', { ascending: false }); // Sort by 'date' in descending order

    if (error) {
      console.error('Error fetching detections:', error);
      return h.response({ error: error.message }).code(500);
    }

    return data;
  },
});

// Route to create a new detection
server.route({
  method: 'POST',
  path: '/detection',
  handler: async (request, h) => {
    const { data, error } = await supabase
      .from('detections')
      .insert([request.payload]);

    if (error) {
      console.error('Error creating detection:', error);
      return h.response({ error: error.message }).code(500);
    }

    const detection = data[0];

    // Publish the new detection to the websocket
    server.publish('/detections/updates', detection);
  },
});

// Route fetch single detection
server.route({
  method: 'GET',
  path: '/detection/{id}',
  handler: async (request, h) => {
    const { data, error } = await supabase
      .from('detections')
      .select('*')
      .eq('id', request.params.id);

    if (error) {
      console.error('Error fetching detection:', error);
      return h.response({ error: error.message }).code(500);
    }

    if (data.length === 0) {
      return h.response({ message: 'Detection not found' }).code(404);
    }

    const detection = data[0];

    return detection;
  },
});

// Start the server
const start = async () => {
  try {
    await server.start();
    console.log(`Server running on ${server.info.uri}`);
  } catch (err) {
    console.error(err);
    process.exit(1);
  }
};

start();
