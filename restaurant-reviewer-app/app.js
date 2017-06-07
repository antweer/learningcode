var express = require('express');
var app = express();
var promise = require('pg-promise');
var body_parser = require('body-parser');

app.use(body_parser.urlencoded({extended: false}));
app.use('/static', express.static('public'));



app.listen(8000, function(){
  console.log('Listening on Port 8000');
});