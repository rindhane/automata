const net = require('net');

const server=net.createServer(conn=>{
    console.log('new client hello');

    conn.on('data', data=>{
        console.log(data.toString());
        conn.write(data+'\r\n'+'mello');
    })
    
    conn.on('end',()=>{
        console.log('client left');
    })
})

server.listen({
host:'localhost',
port:9090
});


server.on('connection',(client)=>{
    console.log('client connected');
    client.write('welcome');
})

