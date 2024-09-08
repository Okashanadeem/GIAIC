// Nested Function 
let myfunc1 = () => {

    function func1() {

        let myname : string = "okasha"

    }
    function func2() {

        let greet : string = "hello ", myname;
        console.log(greet)
    }
}
console.log(myfunc1())

// The result is undefine 