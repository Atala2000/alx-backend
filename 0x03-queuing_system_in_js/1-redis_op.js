import { createClient } from 'redis';

// Create a Redis client instance
const client = createClient();

// Add error event listener
client.on('error', (err) => {
    console.error('Redis client not connected to the server:', err);

});

// Add connect event listener
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        console.log(reply);
    });
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
