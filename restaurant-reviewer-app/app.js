var express = require('express');
var app = express();
var promise = require('bluebird');
var body_parser = require('body-parser');
var pgp = require('pg-promise')({
  promiseLib: promise
});
var db = pgp({database: 'test'});

app.use(body_parser.urlencoded({extended: false}));
app.use('/static', express.static('public'));
app.set('view engine', 'hbs');

app.get('/', function(req, resp){
  resp.render('homepage.hbs', {title: 'Review restaurants!'});
});

app.get('/search', function(req, resp, next){
  let search = req.query.searchTerm;
  let query = "SELECT * FROM restaurant WHERE restaurant.name ILIKE '%$1#%'";
  db.any(query, search)
    .then(function(resultsArray){
      resp.render('search_results.hbs', {
        results: resultsArray
      });
    })
    .catch(next);
});

app.listen(8000, function(){
  console.log('Listening on Port 8000');
});