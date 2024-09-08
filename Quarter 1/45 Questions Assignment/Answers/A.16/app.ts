// 16. More Guests: You just found a bigger dinner table, so now more space is
// available. Think of three more guests to invite to dinner.

// • Start with your program from Exercise 15. Add a print statement to the end of your program informing people that you found a
// bigger dinner table.

// • Add one new guest to the beginning of your array.

// • Add one new guest to the middle of your array.
// • Use append() to add one new guest to the end of your list.
// • Print a new set of invitation messages, one for each person in your list.


//Excersise 15
let guests : string[] = ["Shahzaib", "Armughan", "Ali","Ayesha" , "Alishba"];
let index = guests.indexOf("Ali"); //finding the index of Ali
if (index !== -1){
   guests[index] = "Ismail"        //Replace
};
// Sending invitations after replacement
for (let i = 0; i < guests.length; i++){
    console.log(`Hello! ${guests[i]}. I would be happy if you come to my Birthday Party.`);
};
console.log("\nGreat news! We found a bigger dinner table, so we can invite more guests.");
//Excersise 15

//NOW

// • Add one new guest to the beginning of your array.
guests.unshift("Urooj");
// • Add one new guest to the middle of your array.
let midIndex = Math.floor(guests.length / 2);
guests.splice(midIndex,0,"Yousra");
// • Use append() to add one new guest to the end of your list.
guests.push("Shanzay");
// • Print a new set of invitation messages, one for each person in your list.
for (let i = 0; i < guests.length; i++){
    console.log(`Hello! ${guests[i]}. I would be happy if you come to my Birthday Party.`);
};