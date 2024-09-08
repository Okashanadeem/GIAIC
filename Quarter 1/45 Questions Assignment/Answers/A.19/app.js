// 19. Dinner Guests: Working with one of the programs from Exercises 14 through 18, print a message indicating the number of people you are inviting to dinner.
//Excersise 17
// Initial array from Exercise 16
let guests = ["Urooj", "Shahzaib", "Armughan", "Yousra", "Ali", "Ayesha", "Alishba", "Shanzay"];
// Print message saying you can only invite two people
console.log("Unfortunately, I can invite only two people for dinner.\n");
// Remove guests until only two remain
while (guests.length > 2) {
    let removedGuest = guests.pop();
    console.log(`Sorry, ${removedGuest}, I can't invite you to the dinner.`);
}
// Print a message to the two people still on the list
for (let i = 0; i < guests.length; i++) {
    console.log(`Hello! ${guests[i]}. You are still invited to my Birthday Party.`);
}
// Remove the last two names from the list to make it empty
guests.pop();
guests.pop();
// Confirm the list is empty
console.log("\nGuest list after removing everyone:", guests);
//Excersise 17
//print a message indicating the number of people you are inviting to dinner.
console.log(`I'm inviting ${guests.length} Guests to Dinner.`);
export {};
