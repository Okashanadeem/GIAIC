// 31. No Users: Add an if test to Exercise 28 to make sure the list of users is not empty.
// • If the list is empty, print the message We need to find some users!
// • Remove all of the usernames from your array, and make sure the correct message is printed.
var user_names = []; // empty array
if (user_names.length === 0) {
    console.log("We need to find some users!");
}
else {
    user_names.forEach(function (user_name) {
        if (user_name === "Admin") {
            console.log("Hello ".concat(user_name, ", would you like to see a status report?"));
        }
        else {
            console.log("Hello ".concat(user_name, ", thank you for logging in again."));
        }
    });
}
