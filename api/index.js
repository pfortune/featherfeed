// Import Hapi framework
const Hapi = require('@hapi/hapi');

// Create a new Hapi server with CORS enabled
const server = Hapi.server({
    port: 3000,
    host: 'localhost',
    routes: {
        cors: {
            origin: ['http://localhost:5173'], // Allow requests from any origin
            credentials: true // Allow cookie-based authentication
        }
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
