// function

function myfunction() {
    console.log("hello world")
}
myfunction()


function myfuction1() {
    let num = 2 + 2
    console.log(num)
}
myfuction1()


function myfuction2() {
    let sum = 2 + 2
    return sum
}
console.log(myfuction2())


function greet(name: string ){
    console.log("hello", name)
}
greet("Ali")

function myfunction3(num2: number) {
    let x = num2 * 4;
    return x;
}

let num1: number = 2;
if (num1 % 2 == 0) {
    let result = myfunction3(10);
    console.log(result); 
}

