var express = require('express');
var app = express();
var body_parser = require('body-parser');

var promise = require('bluebird');
var pgp = require('pg-promise')({
  promiseLib: promise
});
var db = pgp({database: 'test'});

app.set('view engine', 'hbs');

app.use(body_parser.urlencoded({extended: false}));
app.use('/static', express.static('public'));

app.get('/todos', function(request, response, next){
  let query = "SELECT * FROM task";
  db.any(query)
    .then(function(resultsArray){
      response.render('todo.hbs', {
        results: resultsArray
      });
    })
    .catch(next);
});

app.get('/todos/add', function(request, response){
  response.render('add.hbs');
});

app.get('/todos/done/:id', function(request, response){
  var id = request.params.id;
  db.query('UPDATE task SET done = TRUE WHERE id = $1', id)
    .then(function(){
      response.redirect('/todos');
    });
});

app.post('/submit', function(request, response){
  console.log(request.body.name);
  db.query('INSERT INTO task (description) VALUES ($1)', request.body.name)
    .then(function(){
      response.redirect('/todos');
    });
});


app.listen(8000, function(){
  console.log('Listening on port 8000')
});