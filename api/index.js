require('dotenv').config();
import { createClient } from '@supabase/supabase-js'
const Hapi = require('@hapi/hapi');

// Create a single supabase client for interacting with your database
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

// Create a new Hapi server with CORS enabled
const server = Hapi.server({
    port: process.env.PORT || 3000,
    routes: {
        cors: {
            origin: ['https://featherfeed.ie'],
            additionalHeaders: ['cache-control', 'x-requested-with']
        }
    }
});

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
                <li>/detections/{id} - Fetch a specific detection by ID</li>
            </ul>
        `;
    }
});

// Define the status route
server.route({
    method: 'GET',
    path: '/status',
    handler: (request, h) => {
        return { status: 'OK' };
    }
});

// Route to fetch all detections
server.route({
    method: 'GET',
    path: '/detections',
    handler: async (request, h) => {
        const { data, error } = await supabase
            .from('detections')
            .select('*');

        if (error) {
            console.error('Error fetching detections:', error);
            return h.response({ error: error.message }).code(500);
        }

        return data;
    }
});

// Route to fetch a specific detection by ID
server.route({
    method: 'GET',
    path: '/detections/{id}',
    handler: async (request, h) => {
        const id = request.params.id;
        const { data, error } = await supabase
            .from('detections')
            .select('*')
            .eq('id', id)
            .single();

        if (error) {
            console.error(`Error fetching detection with ID ${id}:`, error);
            return h.response({ error: error.message }).code(500);
        }

        return data;
    }
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
