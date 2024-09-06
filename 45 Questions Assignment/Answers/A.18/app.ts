// 18. Seeing the World: Think of at least five places in the world you’d like to visit.

// • Store the locations in a array. Make sure the array is not in alphabetical order.

// • Print your array in its original order.

// • Print your array in alphabetical order without modifying the actual list.

// • Show that your array is still in its original order by printing it.

// • Print your array in reverse alphabetical order without changing the order of the original list.

// • Show that your array is still in its original order by printing it again.

// • Reverse the order of your list. Print the array to show that its
// order has changed.

// • Reverse the order of your list again. Print the list to show it’s back to its original order.

// • Sort your array so it’s stored in alphabetical order. Print the array to show that its order has been changed.

// • Sort to change your array so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

let places: string[] = ["Switzerland", "Tokyo", "Japan", "Germany", "Paris"];
console.log("Original Array:");
console.log(places);

// Sorted Array (without modifying the original)
let sortedArray = [...places].sort(); // Copy the array and then reverse
console.log(`\nSorted Array (without modifying the original):`);
console.log(sortedArray)

// Show that the original array is still the same
console.log(`\nOriginal is still the same:`);
console.log(places)

// Reversed Array (without modifying the original)
let reversedArray = [...places].reverse(); // Copy the array and then reverse
console.log(`\nReversed Array (without modifying the original):`);
console.log(reversedArray)

// Show that the original array is still the same
console.log(`\nOriginal is still the same:`);
console.log(places)

// Reverse the original array (this changes the original array)
places.reverse();
console.log(`\nOriginal Array is reversed:`);
console.log(places)

// Reverse the array again to go back to the original order
places.reverse();
console.log(`\nArray is back to its original form:`);
console.log(places)

// Sort the original array (this modifies the original array)
places.sort();
console.log(`\nOriginal Array is sorted:`);
console.log(places)

// Sort the array and then reverse it (this modifies the original array)
places.sort().reverse();
console.log(`\nOriginal Array is sorted and reversed:`);
console.log(places)
