//Javascript Exercises 1 
//Hello, you!
function hello(name){
    console.log("Hello",name);
}
hello("Tanweer");
//Hello, you! Part 2 
function hello(name){
    if (typeof(name) != "undefined"){
        console.log("Hello, ",name,"!");
    }else{
        console.log("Hello, world!");
    }
}
hello();
hello("Tanweer");
//Madlib
function madlib(name, subject){
    return(`${name}'s favorite subject in school is ${subject}`);
}
madlib("Tanweer", "math");
//Tip Calculator
function tipAmount(bill, serviceLevel){
    if(serviceLevel == "good"){
        return(bill*.20);
    }else if(serviceLevel == "fair"){
        return(bill*.15);
    }else if(serviceLevel == "bad"){
        return(bill*.10);
    }else{
        return("Invalid input for level of service");
    }
}
tipAmount(100,"good");
tipAmount(40, "fair");
//Tip Calculator 2
function tipAmount(bill, serviceLevel){
    if(serviceLevel == "good"){
        return(bill + bill*.20);
    }else if(serviceLevel == "fair"){
        return(bill + bill*.15);
    }else if(serviceLevel == "bad"){
        return(bill + bill*.10);
    }else{
        return("Invalid input for level of service");
    }
}
tipAmount(100,"good");
tipAmount(40, "fair");
//Tip Calculator 3 
function tipAmount(bill, serviceLevel, peopleSplitting){
    if(serviceLevel == "good"){
        return((bill + bill*.20)/peopleSplitting);
    }else if(serviceLevel == "fair"){
        return((bill + bill*.15)/peopleSplitting);
    }else if(serviceLevel == "bad"){
        return((bill + bill*.10)/peopleSplitting);
    }else{
        return("Invalid input");
    }
}
tipAmount(100,"good", 5);
tipAmount(40, "fair", 2);
//Print Numbers
function printNumbers(start, end){
  for(let i = start; i <= end; i++){
    console.log(i);
  }
}
printNumbers(1,10);
//Print a Square
function printSquare(size){
  for(let i=0; i<size; i++){
    console.log("*".repeat(size));
  }
}
printSquare(5);
//Print a Box
function printBox(width, height){
  var heightEnding = "*".repeat(width);
  var middleRow = "*" + " ".repeat(width-2) + "*\n";
  var middle = middleRow.repeat(height-2);
  var box = heightEnding + "\n" + middle + heightEnding;
  
  console.log(box);
}
printBox(6,4);
//Print a Banner
function printBanner(text){
  var starRow = "*".repeat(text.length + 4);
  var textRow = "* " + text + " *\n";
  var banner = starRow + "\n" + textRow + starRow;
  
  console.log(banner);
}
printBanner("Welcome to Digital Crafts!");
//Factor a Number
function factor(number){
  let factors = [];
  for(let i = 1; i<=number; i++){
    if(number%i == 0){
      factors.push(i);
    }else{
      continue;
    }
  }
  return(factors);
}
factor(15);
//Caeser Cipher
function cipher(text, offset){
  var upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
  var lowerCase = "abcdefghijklmnopqrstuvwxyz".split("");
  var pre = text.split("");
  var post = [];
  for(let i=0; i<text.length; i++){
    if(upperCase.indexOf(pre[i]) != -1){
      if(upperCase.indexOf(pre[i]) >= offset){
        post.push(upperCase[upperCase.indexOf(pre[i])-offset]);
      }
      else{
        let carry = upperCase.length + (upperCase.indexOf(pre[i]) - offset);
        post.push(upperCase[carry]);
      }
    } else if(lowerCase.indexOf(pre[i]) != -1){
      if(lowerCase.indexOf(pre[i]) >= offset){
        post.push(lowerCase[lowerCase.indexOf(pre[i])-offset]);
      }
      else{
        let carry = lowerCase.length + (lowerCase.indexOf(pre[i]) - offset);
        post.push(lowerCase[carry]);
      }
    } else {
      post.push(pre[i]);
    }
  }
  post = post.join("");
  return(post);
}
// Caeser Cipher 2
function decipher(text, offset){
  var upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
  var lowerCase = "abcdefghijklmnopqrstuvwxyz".split("");
  var pre = text.split("");
  var post = [];
  for(let i=0; i<text.length; i++){
    if(upperCase.indexOf(pre[i]) != -1){
      if(upperCase.indexOf(pre[i]) + offset < upperCase.length){
        post.push(upperCase[upperCase.indexOf(pre[i])+offset]);
      }
      else{
        let carry = (upperCase.indexOf(pre[i]) + offset) - upperCase.length;
        post.push(upperCase[carry]);
      }
    } else if(lowerCase.indexOf(pre[i]) != -1){
      if(lowerCase.indexOf(pre[i]) + offset < lowerCase.length){
        post.push(lowerCase[lowerCase.indexOf(pre[i])+offset]);
      }
      else{
        let carry = (lowerCase.indexOf(pre[i]) + offset) - lowerCase.length;
        post.push(lowerCase[carry]);
      }
    } else {
      post.push(pre[i]);
    }
  }
  post = post.join("");
  return(post);
}
//Leetspeak
function leetspeak(text){
  var leet = {
    "A":4,
    "a":4,
    "E":3,
    "e":3,
    "G":6,
    "g":6,
    "L":1,
    "l":1,
    "O":0,
    "o":0,
    "S":5,
    "s":5,
    "T":7,
    "t":7
  };
  var message = text.split("");
  var leetmessage = [];
  for(let i = 0; i<text.length; i++){
    if(message[i] in leet){
      leetmessage.push(leet[message[i]]);
    } else {
      leetmessage.push(message[i]);
    }
  }
  leetmessage = leetmessage.join("");
  return(leetmessage);
}
// Long-long Vowels
function longLongVowels(string){
  var vowels = {
    "a":"aaaa",
    "e":"eeee",
    "i":"iiii",
    "o":"oooo",
    "u":"uuuu"
  };
  var text = string.split("");
  var longtext = [];
  longtext.push(text[0]);
  for(let i=1; i<string.length; i++){
    if(text[i] in vowels && text[i-1] in vowels){
      longtext.push(vowels[text[i]]);
    } else {
      longtext.push(text[i]);
    }
  }
  longtext = longtext.join("");
  return longtext;
}
//Sum the Numbers
function sumNumbers(array){
  sum = 0;
  for(let i=0; i<array.length; i++){
    sum += array[i];
  }
  return sum;
}
// Just the positives
function positiveNumbers(array){
  positives = [];
  for(let i=0; i<array.length; i++){
    if(array[i] >= 0){
      positives.push(array[i]);
    }else{
      continue;
    }
  }
  return positives;
}
// Matrix Addition
function matrixAdd(array1, array2){
  add = [[,],[,]]
  for(let i = 0; i < array1.length; i++){
    for(let j = 0; j < array1[i].length; j++){
      add[i][j] = array1[i][j] + array2[i][j]
    }
  }
  return add;
}
// Matrix Multiplication

// Rock Paper Scissors
function rockPaperScissors(player1, player2){
  var win = {
    "rock":"scissors",
    "paper":"rock",
    "scissors":"paper"
  };
  if(win[player1]==player2){
    return("player 1");
  } else if (win[player2]==player1){
    return("player 2");
  } else {
    return("draw");
  }
}
// Tic Tac Toe