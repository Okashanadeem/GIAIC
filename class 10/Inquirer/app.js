import inquirer from 'inquirer';
let ans = await inquirer.prompt([
    {
        type: "input",
        message: "what is your name?",
        name: "userName"
    },
    {
        type: "number",
        message: "what is your age?",
        name: "userAge"
    },
    {
        type: "list",
        message: "where do you live?",
        name: "Location",
        choices: ["In Karachi", "In other city of Pakistan", "Abroad"]
    },
    {
        type: "checkbox",
        message: "Which skill do you have?",
        name: "Skills",
        choices: ["Programer", "Graphic Designer", "Others"]
    },
]);
console.log(ans);
