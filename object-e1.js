// Problem 1 
function Person(name, email, phone) {
  this.name = name;
  this.email = email;
  this.phone = phone;
  }

Person.prototype.greet = function(other) {
  console.log('Hello ' + other.name + ', I am ' + this.name + '!');
  };

Person.prototype.info = function() {
  console.log(this.name + ': ' + this.email + ' ' + this.phone);
}
  
var sonny = new Person('Sonny', 'sonny@hotmail.com', '483-485-4948');
var jordan = new Person('Jordan', 'jordan@aol.com', '495-586-3456');
sonny.greet(jordan);
jordan.greet(sonny);
sonny.info();
jordan.info();

// Card constructor
class Card {
  constructor (point, suit) {
    this.point = point;
    this.suit = suit;
  }
  getImageUrl() {
    return("images/" + this.point + "_of_" + this.suit + ".png");
  }
}

// Hand constructor
class Hand {
  constructor () {
    this.hand = [];
  }
  addCard (object) {
    this.hand.push(object);
  }
  getPoints(){
    let points = 0;
    for(let x = 0; x < this.hand.length; x++){
      if(this.hand[x].point == 1){
        if((21-points)<11){
          points += 1;
        } else {
          points += 11;
        }
      }else if(this.hand[x].point > 10){
        points += 10;
      }else{
        points += this.hand[x].point;
      }
    }
    return points;
  }
}

// Deck constructor