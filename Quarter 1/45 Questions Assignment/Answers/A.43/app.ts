// 43. Unchanged Magicians: Start with your work from Exercise 42. Call the
// function make_great() with a copy of the array of magicians’ names. Because the
// original array will be unchanged, return the new array and store it in a separate array.
// Call show_magicians() with each array to show that you have one array of the original
// names and one array with the Great added to each magician’s name.

let magicianName: string[] = ["Criss Angel", "Dynamo", "Harry Houdini", "Penn and Teller"];

// Function to print magicians' names
let printName = (names: string[]): void => {
    names.forEach(name => {
        console.log(name);
    });
}

// Function to modify a copy of the array by adding "The Great" to each magician's name
let make_great = (names: string[]): string[] => {
    // Return a new array with "The Great" added to each magician's name
    return names.map(name => "The Great " + name);
}

console.log("Original array:");
printName(magicianName);

// Modify a copy of the original array
let greatMagicians = make_great(magicianName);

console.log("\nModified array (copy):");
printName(greatMagicians);

console.log("\nOriginal array (unchanged):");
printName(magicianName);
