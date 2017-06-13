var express = require('express');
var app = express();

var http = require('http').Server(app);
var io = require('socket.io')(http);

app.set('view engine', 'hbs');

app.use('/socket-io', express.static('node_modules/socket.io-client/dist'));

app.get('/', function (request, response) {
  response.render('chat.hbs');
});

io.on('connection', function(client){
  console.log('CONNECTED', client.id);
  
  //client.on('incoming', function(msg){
  //  io.emit('chat-msg', msg);
    //io.emit allows you to send message to everyone vs client.emit which will only show the message in the browser - commenting out to implement chat rooms
  //});
  
  client.on('join-room', function(room){
    client.join(room,function() {
      console.log(client.rooms);
      io.to(room).emit('chat-msg', '**new user joined**'); //to(room) sends the message only to the people in that room
    });
    
    client.on('incoming', function (msg){
      io.to(msg.room).emit('chat-msg', msg.msg);
    });
  });
  
  client.on('disconnect', function () {
    console.log('EXITED');
  });
});


http.listen(9000, function(){
  console.log('Listening on port 8000')
});