// 41. Magicians: Make a array of magician’s names. Pass the array to a function
// called show_magicians(), which prints the name of each magician in the array.
var magicianName = ["Ali", "Okasha", "Shahzaib", "Armughan"];
var printName = function () {
    magicianName.forEach(function (name) {
        console.log(name);
    });
};
printName();
