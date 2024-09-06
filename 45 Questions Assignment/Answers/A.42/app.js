// 42. Great Magicians: Start with a copy of your program from Exercise 39.
// Write a function called make_great() that modifies the array of magicians by adding
// the phrase the Great to each magician’s name. Call show_magicians() to
// see that the list has actually been modified.
var magicianName = ["Criss Angel", "Dynamo", "Harry Houdini", "Penn and Teller"];
var printName = function () {
    magicianName.forEach(function (name) {
        console.log(name);
    });
};
console.log("Original array:");
printName();
var make_great = function () {
    for (var i = 0; i < magicianName.length; i++) {
        magicianName[i] = "The Great" + magicianName[i];
    }
};
// Modify the array
make_great();
console.log("Modified Array");
printName();
