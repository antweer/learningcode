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

//similar to a view on django
app.get('/', function(request, response){
  response.send('Hello World!');
}); 

app.get('/about', function(request, response){
  response.send('About Me');
}); 

app.get('/projects', function(request, response){
  response.send('Projects');
}); 

app.get('/cats', function(request, response){
  response.send('Meow');
});

app.get('/dogs', function(request, response){
  response.send('Woof');
});

app.get('/cats_and_dogs', function(request, response){
  response.send('Living together');
});

app.get('/fav_animals', function(request, response){
  var animals = [
    { name: 'cats', favorite: true },
    { name: 'dogs', favorite: true },
    { name: 'tree frogs', favorite: true },
    { name: 'earth worms', favorite: false },
    { name: 'guinea pigs', favorite: true },
    ];
  var context = {
    animal: animals,
  }
  response.render('template2.hbs', context);
})

//URL Parameters
app.get('/post/:slug', function (request, response){
  var slug = request.params.slug;
  response.send('Post about: ' + slug);
});

app.get('/greet/:name', function(request, response){
  var name = request.params.name;
  var age = request.query.age || '21';
  var year = 2017 - age;
  var context = {
    title: 'Greet & Age',
    name: name,
    year: year
  };
  response.render('templates1.hbs', context);
});

//GET Parameters
app.get('/hello', function(request, response){
  var name = request.query.name || 'World';
  var context = {
    title: 'Hello', 
    name: name, 
    content: 'hello',
    friend: [
      {name: "john john spetseris", age: 'old man'},
      {name: "jordawg", age: 'getting there'}
      ]};
  response.render('hello.hbs', context);
})

app.get('/form', function(request, response){
  response.render('form.hbs');
});

app.get('/year', function(request, response){
  var age = request.query.age || '21';
  var year = 2017 - age;
  response.send('You were born in ' + year + '.');
})

app.post('/submit', function(request, response){
  console.log(request.body);
  response.redirect('/thank-you');
})

app.get('/thank-you', function(request, response){
  response.render('thanks.hbs', {title: 'Thanks!'});
})

app.get('/search', function(request, response, next){
  let term = request.query.searchTerm;
  let query = "SELECT * FROM restaurant WHERE restaurant.name ILIKE '%$1#%'";
  db.any(query, term)
    .then(function(resultsArray){
      response.render('search.hbs', {
        results: resultsArray
      });
    })
    .catch(next);
});

app.listen(8000, function(){
  console.log('Listening on port 8000')
});