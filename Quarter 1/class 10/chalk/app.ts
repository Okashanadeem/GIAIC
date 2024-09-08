import chalk from "chalk"
let yourname = prompt(`what is your Name?`)
let fatherName = prompt(`What is your father name?`)
console.log(chalk.underline.yellow(`your name is:`),chalk.bold.greenBright(yourname))
console.log(chalk.underline.yellow(`your Father name is:`),chalk.bold.greenBright(fatherName))