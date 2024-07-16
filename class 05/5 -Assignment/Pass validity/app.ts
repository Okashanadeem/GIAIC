let useName: string = "okasha";
let pass: number = 123;
function passfunc(name: string, passcode: number) {
    if (name === useName) {
        console.log("welcome ", useName)
    } else {
        console.log("Wrong user name")
    }

    if (passcode === pass) {
        console.log("password (", pass, ")is correct")
    } else {
        console.log("password (", passcode, ")is incorrect")
    }
}


// entre the username first and then password
passfunc("okasha", 123)