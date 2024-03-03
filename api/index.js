import Fastify from 'fastify';
import fastifyCors from '@fastify/cors';
import fastifyWebsocket from 'fastify-websocket';
import routes from './routes.js';

const app = Fastify({ logger: true });

async function setup() {
  // Registering plugins
  await app.register(fastifyCors, {
    origin: ['https://featherfeed.ie'],
  });

  await app.register(fastifyWebsocket);

  // Register each route
  routes.forEach((route) => {
    app.route(route);
  });

  // Start the server
  try {
    await app.listen({ port: process.env.PORT || 3000 });
    console.log(`Server running at: ${app.server.address().port}`);
  } catch (err) {
    app.log.error(err);
    process.exit(1);
  }
}

setup();
