//Object Exercises 2 
// Inheritance
var mom = {
  firstName: 'Alice',
  lastName: 'Wong',
  eyeColor: 'brown',
  hairColor: 'black'
};
var daughter = {
  firstName: 'Ilene',
  hairColor: 'brown'
};
daughter.__proto__ = mom;
mom.showInfo = function(){
    console.log(this.firstName + ' ' + this.lastName + ' ' + this.eyeColor + ' ' + this.hairColor);
}
mom.showInfo();
daughter.showInfo();

// Person + these thises +
class Person {
  constructor(name){
    this.name = name;
    this.friends = [];
  }
  addFriend(friend){
    this.friends.push(friend);
  }
  createGreeting(other){
    return('Yo ' + other.name + '! from ' + this.name + '.');
  }
  greet(other){
    console.log(this.createGreeting(other));
  }
  lazyGreet(other){
    setTimeout(() => {this.greet(other);}, 10000);
  }
  createGreetingsForFriends() {
    var self = this;
    var greetings = this.friends.map(function(person){return self.createGreeting(person);});
    return greetings;
  }
}

var alfie = new Person('Alfie');
var anushka = new Person('Anushka');
var henrique = new Person('Henrique');
alfie.addFriend(anushka);
alfie.addFriend(henrique);
alfie.createGreetingsForFriends();