var rl = require('readline');

var readline = rl.createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('What is your name? ', function(name){
  console.log('Hello, ' + name + '!');
  readline.close();
});