//CPS Call Rewrites
z = f(1, 2);
f(1, 2, function(z){
});

y = g(4.5, 0.2, true);
g(4.5, 0.2, true, function(y){
});

result = convert([1, 8, 2, 4, 4]);
convert([1, 8, 2, 4, 4], function(result){});

result = convert([1, 8, 2, 4, 4], {reverse: true});
convert([1, 8, 2, 4, 4], {reverse: true}, function(result){});

kick(can);
kick(can, function(){});

message = hello('Tonya');
hello('Tonya', function(message){});

miles = distance(start, finish);
distance(start, finish, function(miles){});

title = capitalize(title);
capitalize(title, function(title){});

shampoo(dog);
shampoo(dog, function(){});

hello();
hello(function(){});

//CPS Function Rewrites
function add(x, y) {
  var result = x + y;
  return result;
}
function add(x, y, callback) {
  var result = x + y;
  callback(result);
}

function subtract(x, y) {
  return x - y;
}
function subtract(x, y, callback) {
  callback(x - y);
}

function greeting(person) {
  return 'Hola, ' + person + '!';
}
function greeting(person, callback) {
  callback('Hola, ' + person + '!');
}

function hello() {
  console.log('Hello, world!');
}
function hello(callback) {
  console.log('Hello, world!');
  callback();
}

function product(numbers) {
  return numbers.reduce(function(a, b) {
    return a * b;
  }, 1);
}
// Nested Callbacks 1 
function square(num) {
  return num * num;
}

var squared = square(5);

function square(num, callback){
  setTimeout(function(){
    callback(num*num);
  }, 2000);
}

square(5,function(squared){
  setTimeout(function(){
    console.log(squared);
  }, 2000);
});

//Nested Callbacks 2 
var x = 4;
var y = 3;
var x2 = square(x);
var y2 = square(y);
var sum = x2 + y2;

var x = 4;
var y = 3; 
square(x, function(x2){
    console.log(x2+y2);
});

//Nested Callbacks 3
function squareRoot(num) {
  return Math.sqrt(num);
}

function squareRoot(num, callback) {
  setTimeout(function(){
    callback(Math.sqrt(num);
  }, 500);
}

square(x, function(x2){
  square(y, function(y2){
    squareRoot((x2+y2), function(sqrt){
      console.log('The answer is: ' + sqrt);
    });
  });
});