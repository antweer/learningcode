// Exercise 1 
var phonebookDict = {
  Alice: '703-493-1834',
  Bob: '857-384-1234',
  Elizabeth: '484-584-2923'
};
// 1.1 
console.log(phonebookDict.Elizabeth);
// 1.2 
phonebookDict.Kareem = '938-489-1234';
// 1.3 
delete phonebookDict.Alice;
// 1.4 
phonebookDict.Bob = '968-345-2345';
// 1.5 
for(var personName in phonebookDict){
  var phoneNumber = phonebookDict[personName];
  console.log(`${personName}: ${phoneNumber}`);
}

// Letter Histogram
function letterHistogram(string){
  var letters = string.split("");
  var histogram = {};
  for(let i = 0; i<letters.length; i++){
    if(histogram[letters[i]]){
      histogram[letters[i]] += 1;
    } else {
      histogram[letters[i]] = 1;
    }
  }
  return histogram;
}

// Word Histogram 
function wordHistogram(string){
  var words = string.split(" ");
  var histogram = {};
  for(let i = 0; i<words.length; i++){
    if(histogram[words[i]]){
      histogram[words[i]] += 1;
    } else {
      histogram[words[i]] = 1;
    }
  }
  return histogram;
}

// Bonus 