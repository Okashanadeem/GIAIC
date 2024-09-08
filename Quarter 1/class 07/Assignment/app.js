// Nested Function 
var myfunc1 = function () {
    function func1() {
        var myname = "okasha";
    }
    function func2() {
        var greet = "hello ", myname;
        console.log(greet);
    }
};
console.log(myfunc1());
