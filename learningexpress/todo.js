var express = require('express');
var app = express();
var body_parser = require('body-parser');
var session = require('express-session');
var promise = require('bluebird');
var pgp = require('pg-promise')({
  promiseLib: promise
});
var db = pgp({database: 'postgres'});

var morgan = require('morgan');
app.use(morgan('dev'));

app.set('view engine', 'hbs');

app.use(body_parser.urlencoded({extended: false}));
app.use('/static', express.static('public'));
app.use(session({
  secret: process.env.SECRET_KEY || 'dev', 
  resave: true,
  saveUninitialized: false,
  cookie: {maxAge: 600000}
}));

app.use(function(request, response, next){
  if (request.session.user) {
    next();
  }else if (request.path == '/login'){
    next();
  } else {
    response.redirect('/login');
  }
});

app.get('/', function(request, response, next){
  let query = "SELECT * FROM task";
  db.any(query)
    .then(function(resultsArray){
      response.render('todo.hbs', {
        results: resultsArray
      });
    })
    .catch(next);
});

app.get('/add', function(request, response){
  response.render('add.hbs');
});

app.get('/done/:id', function(request, response){
  var id = request.params.id;
  db.query('UPDATE task SET done = TRUE WHERE id = $1', id)
    .then(function(){
      response.redirect('/');
    });
});

app.post('/submit', function(request, response){
  console.log(request.body.name);
  db.query('INSERT INTO task (description) VALUES ($1)', request.body.name)
    .then(function(){
      response.redirect('/');
    });
});

app.get('/login', function(request, response){
  response.render('login.hbs');
});

app.post('/login', function (request, response) {
  var username = request.body.username;
  var password = request.body.password;
  if (username == 'tanweer' && password == 'tanweer') {
    request.session.user = username;
    response.redirect('/');
  } else {
    response.render('login.hbs');
  }
});

app.listen(9000, function(){
  console.log('Listening on port 8000')
});