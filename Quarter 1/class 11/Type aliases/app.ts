// Type aliases 

// This a very lengthy pocess 

let stud1: {
    name: string;
    age: number;
    Location: string;
}={
    name : "ali",
    age : 18,
    Location : "Karachi"
}

let stud2: {
    name: string;
    age: number;
    Location: string;
}={
    name : "Khan",
    age : 68,
    Location : "Peshawar"
}


// where this is a short way to write 
// Where we a reserved key word called type 

type stud = {
    name : string,
    age : number,
    Location : string
}

let stud3 : stud = {
    name : "Amar",
    age : 68,
    Location : "Kolkata"
}
let stud4 : stud = {
    name : "Saba",
    age : 68,
    Location : "Kashmir"
}


// Also we use interface 

interface Req {
    name1 : string,
    Age : number
}
// and now i want to add another type in this abovew interface so i can do this 

interface Req1 extends Req {
    PhNo : number,
}

let stud5 : Req1 = {
    name1 : "ali",
    Age : 20,
    PhNo : 546646464
}