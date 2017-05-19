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

