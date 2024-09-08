// //synchronous function
// let name = "Okasha";
// let age = 18;
// console.log (`hello ${name}. your age is ${age} years old.`)
// //Asynchronous function
// setTimeout(() => {
//    console.log(`Hi ${name}. Your age is ${age}.`) 
// }, 3000);
// // callback fuction 
// // Define func1 to log a message
// let func1 = () => {
//    console.log("func1 is called");
// };
// // Define func2 to accept a callback and call it
// let func2 = (callback : () => void) => {
//    console.log("func2 is called");
//    callback(); // Call the callback function
// };
// // Call func2 and pass func1 as the callback
// func2(func1);
function func3(cb) {
    console.log("Okasha");
    setTimeout(function () {
        console.log("this is a setTimeout");
        cb();
    }, 2000);
}
console.log("Ayesha");
function callback() {
    console.log("this is a callback");
}
func3(callback);
