var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.set('view engine', 'hbs');

app.get('/', function(req, res){
  res.render('chat2.hbs');
});

io.on('connection', function(socket){
  console.log('a user connected');
  socket.on('chat messages', function(msg){
    io.emit('chat messages', msg);
  });
  socket.on('disconnect', function(){
    console.log('user disconnected');
  });
});

http.listen(9000, function(){
  console.log('listening on 3000');
});