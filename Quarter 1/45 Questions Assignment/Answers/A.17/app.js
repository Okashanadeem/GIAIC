// 17. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
// • Start with your program from Exercise 16. Add a new line that prints a message saying that you can invite only two people for dinner.
// • Remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print
// a message to that person letting them know you’re sorry you can’t invite them to dinner.
// • Print a message to each of the two people still on your list, letting them know they’re still invited.
// • Remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end
// of your program.
// ANSWER:
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
export {};
