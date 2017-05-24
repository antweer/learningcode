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
class Deck {
  constructor(){
    this.cards = [
    { point: 1, suit: 'hearts' },
    { point: 1, suit: 'spades' },
    { point: 1, suit: 'diamonds' },
    { point: 1, suit: 'clubs' },
    { point: 2, suit: 'hearts' },
    { point: 2, suit: 'spades' },
    { point: 2, suit: 'diamonds' },
    { point: 2, suit: 'clubs' },
    { point: 3, suit: 'hearts' },
    { point: 3, suit: 'spades' },
    { point: 3, suit: 'diamonds' },
    { point: 3, suit: 'clubs' },
    { point: 4, suit: 'hearts' },
    { point: 4, suit: 'spades' },
    { point: 4, suit: 'diamonds' },
    { point: 4, suit: 'clubs' },
    { point: 5, suit: 'hearts' },
    { point: 5, suit: 'spades' },
    { point: 5, suit: 'diamonds' },
    { point: 5, suit: 'clubs' },
    { point: 6, suit: 'hearts' },
    { point: 6, suit: 'spades' },
    { point: 6, suit: 'diamonds' },
    { point: 6, suit: 'clubs' },
    { point: 7, suit: 'hearts' },
    { point: 7, suit: 'spades' },
    { point: 7, suit: 'diamonds' },
    { point: 7, suit: 'clubs' },
    { point: 8, suit: 'hearts' },
    { point: 8, suit: 'spades' },
    { point: 8, suit: 'diamonds' },
    { point: 8, suit: 'clubs' },
    { point: 9, suit: 'hearts' },
    { point: 9, suit: 'spades' },
    { point: 9, suit: 'diamonds' },
    { point: 9, suit: 'clubs' },
    { point: 10, suit: 'hearts' },
    { point: 10, suit: 'spades' },
    { point: 10, suit: 'diamonds' },
    { point: 10, suit: 'clubs' },
    { point: 11, suit: 'hearts' },
    { point: 11, suit: 'spades' },
    { point: 11, suit: 'diamonds' },
    { point: 11, suit: 'clubs' },
    { point: 12, suit: 'hearts' },
    { point: 12, suit: 'spades' },
    { point: 12, suit: 'diamonds' },
    { point: 12, suit: 'clubs' },
    { point: 13, suit: 'hearts' },
    { point: 13, suit: 'spades' },
    { point: 13, suit: 'diamonds' },
    { point: 13, suit: 'clubs' },
  ];
    this.deck = [];
  }
  shuffle () {
    let cardsPile = this.cards.length;
    let deckPile = this.deck.length;
    if(cardsPile > 0){
      for(let x=0; x<cardsPile; x++){
        this.deck.push(this.cards.splice(random(0,this.cards.length),1)[0]);
      }
    }else{
      for(let x=0; x<deckPile; x++){
        this.cards.push(this.deck.splice(random(0,this.deck.length),1)[0]);
      }
    }
  }
  draw() {
    if(this.deck.length > 0){
      return(this.deck.pop());
    }else{
      return(this.cards.pop());
    }
  }
  numCardsLeft(){
    if(this.deck.length > 0){
      return(this.deck.length);
    }else{
      return(this.cards.length);
    }
  }
}