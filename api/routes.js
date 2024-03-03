import dotenv from 'dotenv';
dotenv.config();

import { createClient } from '@supabase/supabase-js';

const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

const routes = [
  {
    method: 'GET',
    url: '/',
    handler: async (request, reply) => {
      return reply.type('text/html').send(`
        <h1>API Endpoints</h1>
        <ul>
          <li><a href="/status">/status</a> - Check API status</li>
          <li><a href="/detections">/detections</a> - Fetch all detections</li>
          <li>/detection/{id} - Fetch a specific detection by ID</li>
        </ul>
      `);
    },
  },
  // Define the status route
  {
    method: 'GET',
    url: '/status',
    handler: async (request, reply) => {
      return reply.send({ status: 'OK' });
    },
  },
  // Route to fetch all detections
  {
    method: 'GET',
    url: '/detections',
    handler: async (request, reply) => {
      const { data, error } = await supabase
        .from('detections')
        .select('*')
        .order('date', { ascending: false }); // Sort by 'date' in descending order

      if (error) {
        request.log.error('Error fetching detections:', error);
        return reply.code(500).send({ error: error.message });
      }

      return reply.send(data);
    },
  },
  // Route to create a new detection
  {
    method: 'POST',
    url: '/detection',
    handler: async (request, reply) => {
      const { data, error } = await supabase
        .from('detections')
        .insert([request.body]);

      if (error) {
        request.log.error('Error creating detection:', error);
        return reply.code(500).send({ error: error.message });
      }

      const detection = data[0];

      return reply.send(detection);
    },
  },
  // Route fetch single detection
  {
    method: 'GET',
    url: '/detection/:id',
    handler: async (request, reply) => {
      const { data, error } = await supabase
        .from('detections')
        .select('*')
        .eq('id', request.params.id);

      if (error) {
        request.log.error('Error fetching detection:', error);
        return reply.code(500).send({ error: error.message });
      }

      if (data.length === 0) {
        return reply.code(404).send({ message: 'Detection not found' });
      }

      const detection = data[0];

      return reply.send(detection);
    },
  },
];

export default routes;
