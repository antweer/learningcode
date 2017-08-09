// Closure Exercises
// Counter 1 
function counter(){
  var count = 0;
  function counting(){
    count++;
    return count;
  }
  return counting;
}

// Counter 2
function counter(num){
  var count = num;
  function counting(){
    count++;
    return count;
  }
  return counting;
}

// Counter 3
function counter(num){
  var count = num;
  var obj = {
    increment: function (){
      count++;
      return count
      },
    decrement: function (){
      count--;
      return count
      }
  }
  return obj;
}
