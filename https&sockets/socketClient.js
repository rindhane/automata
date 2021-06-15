const net = require('net');

const options = {
    host: 'localhost',
    port:9090
}

const client = net.createConnection(options, ()=>{
    client.write('hello\r\n');
})

client.on('data', data=>{
    console.log(data.toString());
    client.end();
})