// 32. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.

// • Make a list of five or more usernames called current_users.

// • Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.

// • Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a
// new username. If a username has not been used, print a message saying that the username is available.

// • Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.

let current_users: string[] = ["Okasha", "Ali", "Urooj", "Yousa", "Ayesha"];
let new_users: string[] = ["Okasha", "Shahzaib", "Armughan", "Ayesha", "Nadeem"];

// Convert current usernames to lowercase for case-insensitive comparison
const currentUsersLowerCase = current_users.map(user => user.toLowerCase());

new_users.forEach(new_user => {
    // Convert new user to lowercase
    const newUserLowercase = new_user.toLowerCase();

    if (currentUsersLowerCase.includes(newUserLowercase)) {
        console.log(`The username "${new_user}" is already taken. Please select another name.`);
    } else {
        console.log(`The username "${new_user}" is available.`);
    }
});
