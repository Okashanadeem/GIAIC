// 42. Great Magicians: Start with a copy of your program from Exercise 39.
// Write a function called make_great() that modifies the array of magicians by adding
// the phrase the Great to each magician’s name. Call show_magicians() to
// see that the list has actually been modified.

let magicianName : string[] = ["Criss Angel","Dynamo","Harry Houdini","Penn and Teller"]
let printName = (): void => {
    magicianName.forEach(name =>{
        console.log(name)
    })
}
console.log("Original array:")
printName()

let make_great = ():void => {
    for(let i = 0; i < magicianName.length; i++){
    magicianName[i] = "The Great" + magicianName[i]
    }
}
// Modify the array
make_great()

console.log("Modified Array")
printName()