// Import Hapi framework
const Hapi = require('@hapi/hapi');

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
