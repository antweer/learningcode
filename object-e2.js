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

// Person