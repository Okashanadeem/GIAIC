var personclass = /** @class */ (function () {
    function personclass() {
    }
    return personclass;
}());
var personvar = new personclass();
personvar.name = "Ali";
personvar.age = 20;
console.log(personvar);
// lets make a student data saver
var student = /** @class */ (function () {
    function student(n, g, a, r) {
        this.name = n;
        this.gender = g;
        this.age = a;
        this.rollNum = r;
    }
    student.prototype.studentdata = function () {
        return console.log("student name is ".concat(this.name, " and his/her gender is ").concat(this.gender, ". age is ").concat(this.age, ". Roll Number is ").concat(this.rollNum, " "));
    };
    return student;
}());
var stud1 = new student("Okasha", "Boy", 17, 100);
var stud2 = new student("Ayesha", "girl", 16, 101);
console.log(stud1);
console.log(stud2);
// redeclaration  
stud1.rollNum = 102;
// now suppose we have made a container and we can store all the data of students in it 
var studentArr = [];
studentArr.push(stud1);
studentArr.push(stud2);
console.log(studentArr);
// now calling the function 
console.log(stud1.studentdata());
