var mycalc = function (n1, n2, sign) {
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
    }
    ;
};
mycalc(40, 10, "*");
