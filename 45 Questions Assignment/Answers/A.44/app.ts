// 44. Sandwiches: Write a function that accepts a array of items a person wants
// on a sandwich. The function should have one parameter that collects as many
// items as the function call provides, and it should print a summary of the sandwich
// that is being ordered. Call the function three times, using a different number
// of arguments each time.

// Function that accepts a variable number of items for a sandwich
let make_sandwich = (...items: string[]): void => {
    console.log("\nSandwich order summary:");
    console.log(`You ordered a sandwich with the following items: ${items.join(", ")}`);
}

// Call the function three times with different numbers of arguments
make_sandwich("Lettuce", "Tomato");
make_sandwich("Cheese", "Ham");
make_sandwich("Chicken", "Mayo", "Turkey", "Onion", "Mustard");
