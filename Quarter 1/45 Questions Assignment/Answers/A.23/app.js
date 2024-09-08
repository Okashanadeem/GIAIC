// 23. Conditional Tests: Write a series of conditional tests. Print a statement
// describing each test and your prediction for the results of each test. Your code
// should look something like this:
// let car = 'subaru';
// console.log("Is car == 'subaru'? I predict True.")
// console.log(car == 'subaru')
// • Look closely at your results, and make sure you understand why each line evaluates to True or False.
// • Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
let car = "toyota";
console.log("Is car = 'toyota' ");
console.log(car == "toyota"); //true
console.log("Is car !== 'honda'");
console.log(car !== "honda"); //true
console.log("Is car == 'Toyota' in uppercase");
console.log(car.toUpperCase() == "TOYOTA"); //true
console.log("Is length of car == 6");
console.log(car.length == 6); //true
// console.log("Does car include 'toy'")
// console.log(car.includes("toy")) //true
console.log("Is car = 'suzuki' ");
console.log(car == "suzuki"); //false
console.log("Is car !== 'toyota'");
console.log(car !== "toyota"); //false
console.log("Is car == 'toyota' in uppercase");
console.log(car.toUpperCase() == "toyota"); //false
console.log("Is length of car == 7");
console.log(car.length == 7); //false
export {};
// console.log("Does car include 'hon'")
// console.log(car.includes("hon")) //false
