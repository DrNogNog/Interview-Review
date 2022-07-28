console.log('Teaching the world how to code'.length);
console.log('hello'.toUpperCase());
console.log('Hey'.startsWith('H'));
console.log('   Remember   '.trim());
console.log(Math.ceil(43.8));
console.log(Number.isInteger(2017));
// There are 7 fundamental data types in JavaScript: strings, numbers, booleans, null, undefined, symbol, and object.
var myName = 'Arya';
console.log(myName);
var favoriteFood = 'pizza';
var numOfSlices = 8;
console.log(favoriteFood);
console.log(numOfSlices);

let meal = 'Enchiladas';
console.log(meal)
meal = 'Burrito';
let changeMe = true;
changeMe = false;
console.log(changeMe)

const myName = 'Gilberto';
console.log(myName);
const entree = 'Enchiladas';
console.log(entree)
// This is An Error: entree = 'Tacos'
// This is An Error: const testing;

let levelUp = 10;
let powerLevel = 9001;
let multiplyMe = 32;
let quarterMe = 1152;

// Use the mathematical assignments in the space below:

levelUp += 5;
powerLevel -= 100;
multiplyMe *= 11;
quarterMe /= 4;

// These console.log() statements below will help you check the values of the variables.
// You do not need to edit these statements. 
console.log('The value of levelUp:', levelUp); 
console.log('The value of powerLevel:', powerLevel); 
console.log('The value of multiplyMe:', multiplyMe); 
console.log('The value of quarterMe:', quarterMe);

function myfunction(p1,p2){
    return p1 * p2;
}
var favoriteAnimal = 'Dog'
console.log('My favorite animal: ' + favoriteAnimal)

var myName = 'Gor';
var myCity = 'Brook';
console.log(`My name is ${myName}. My favorite city is ${myCity}`);
// Uses backticks
let newVariable = 'Playing around with typeof.';
console.log(typeof newVariable);

function myFunction(){
    document.getElementById("demo").innerHTML = "Hello"
}

const person = {
    firstName: "John",
    lastName: "Doe"
  };
// a print alert in a OK popup box  
alert(person.firstName);

const persons = {
    name: "John", age: 50 
};
alert(person.name, person.age);
//<button onclick ="alert('Hello')">Click me.</button>
//<div onmouseover="this.style.backgroundColor='red'">myDIV.</div>
myName = myName.replace("Gor", "Gordon");
const fruits = ["Banana", "Orange", "Apple"];
fruits.pop();
fruits.push("Apple");
fruits.splice(1,2);
fruits.sort();
const d = new Date();
year = d.getFullYear();
month = d.getMonth();
d.setFullYear(2020);

agep = n;
var votable = (agep < 18) ? "Too young" : "Old Enough";
alert(votable);
{/* <button id="demo">Click me1</button>

<script>
document.getElementById("demo").
addEventListener
("
click
", myFunction);
</script> */}