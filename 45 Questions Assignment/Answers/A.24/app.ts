// 24. More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests. Have at least one True and one False result for each of the following:

// • Tests for equality and inequality with strings

// • Tests using the lower case function

// • Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to

// • Tests using "and" and "or" operators

// • Test whether an item is in a array

// • Test whether an item is not in a array

let car : string = "Toyota";

console.log("Is car == 'Toyota' ")
console.log(car == "Toyota") //true

console.log("Is car !== 'Honda'")
console.log(car !== "Honda") //true

console.log("Is car == 'Suzuki' ")
console.log(car == "Suzuki") //false

console.log("Is car !== 'Toyota'")
console.log(car !== "Toyota") //false

console.log("Is car == 'toyota' in lowe case")
console.log(car.toLowerCase() == "toyota"); //true

console.log("Is car == 'toyota' in uppercase")
console.log(car.toLowerCase() == "Toyota"); //false


let cityName : string = "UnitedState"

console.log("Is cityName.tolowercase == unitedstate");
console.log(cityName.toLowerCase() == "unitedstate");

console.log("Is cityName.tolowercase == unitedState");
console.log(cityName.toLowerCase() == "unitedState");



let num : number = 10;

console.log("Is  num > 2");
console.log(num > 2); //true

console.log("Is  num < 11");
console.log(num < 11); //true

console.log("Is  num >= 10");
console.log(num >= 10); //true

console.log("Is  num <= 10");
console.log(num <= 10); //true

console.log("Is  num !== 11");
console.log(num !== 11); //true


console.log("Is  num < 2");
console.log(num < 2); //False

console.log("Is  num < 2");
console.log(num > 10); //False

console.log("Is  num >= 10");
console.log(num >= 12); //false

console.log("Is  num <= 12");
console.log(num <= 9); //false

console.log("Is  num !== 10");
console.log(num !== 10); //false


let subject : string = "English";
let marks : number = 98;

console.log("Is subject is equals to English and marks are equals to 98");
console.log(subject == "English" && marks == 98);//true
console.log("Is subject is equals to English and marks are equals to 90");
console.log(subject == "English" && marks == 90);//false
console.log("Is subject is equals to english and marks are equals to 80");
console.log(subject == "english" && marks == 80);//false

console.log("Is subject is equals to English or marks are equals to 98");
console.log(subject == "English" || marks == 98);//true
console.log("Is subject is equals to English or marks are equals to 90");
console.log(subject == "English" || marks == 90);//true
console.log("Is subject is equals to english or marks are equals to 80");
console.log(subject == "english" || marks == 80);//false


// let items : string[] = ["Apple", "Banana", "Watermelon", "Grapes", "Mango"];

// console.log("Apple is insid Items");
// console.log(items.includes("Apple"));

// console.log("Apple is not insid Items");
// console.log(!items.includes("Apple"));
