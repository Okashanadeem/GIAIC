// function
function myfunction() {
    console.log("hello world");
}
myfunction();
function myfuction1() {
    var num = 2 + 2;
    console.log(num);
}
myfuction1();
function myfuction2() {
    var sum = 2 + 2;
    return sum;
}
console.log(myfuction2());
function greet(name) {
    console.log("hello", name);
}
greet("Ali");
function myfunction3(num2) {
    var x = num2 * 4;
    return x;
}
var num1 = 2;
if (num1 % 2 == 0) {
    var result = myfunction3(10);
    console.log(result);
}
