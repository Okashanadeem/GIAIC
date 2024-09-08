class personclass {
    name!: string;
    age: number | undefined;
}
const personvar = new personclass();
personvar.name = "Ali";
personvar.age = 20;
console.log(personvar);


// lets make a student data saver

class student {
    name: string
    gender: string
    age: number
    rollNum: number

    constructor(n: string, g: string, a: number, r: number) {
        this.name = n
        this.gender = g
        this.age = a
        this.rollNum = r
    }
    studentdata() {
        return console.log(`student name is ${this.name} and his/her gender is ${this.gender}. age is ${this.age}. Roll Number is ${this.rollNum} `)
    }
}

const stud1 = new student ("Okasha","Boy",17,100)
const stud2 = new student ("Ayesha","girl",16,101)

console.log(stud1)
console.log(stud2)

// redeclaration  
stud1.rollNum = 102

// now suppose we have made a container and we can store all the data of students in it 

let studentArr:student[] = []

studentArr.push(stud1)
studentArr.push(stud2)

console.log(studentArr)

// now calling the function 
console.log(stud1.studentdata())