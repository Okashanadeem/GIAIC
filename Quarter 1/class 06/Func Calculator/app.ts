function calc(n1: number, n2: number, sign: string) {
    if (sign == "+") {
        console.log(n1 + n2);
    }
    else if (sign == "-") {
        console.log(n1 - n2);
    }
    else if (sign == "*") {
        console.log(n1 * n2);
    }
    else if (sign == "/") {
        console.log(n1 / n2);
    }
    else {
        console.log("invalid sign");
    };
}
calc(2, 10, "+");
calc(2, 10, "-");
calc(2, 10, "*");
calc(2, 10, "/");