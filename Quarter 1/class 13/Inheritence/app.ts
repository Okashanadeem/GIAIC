class parentClass1 {
    name : string
    age : number | string
}
class childClass1 extends parentClass1 {
    gender : "male" | "female" 
}

let myClass1 = new childClass1

myClass1.name = "Okasha"
myClass1.age = 20
myClass1.gender = "male"

console.log(myClass1)


class parentClass2 {
    returnName (name:string){
         return console.log(name)
    }
}
class childClass2 extends parentClass2{
    returnAge(num){
    return console.log(num)
    }
}
let myClass2 = new childClass2
myClass2.returnName("Okasha")
myClass2.returnAge(18)


// Class Inheritance with Method Properties

class parentClass3 {
    constructor() {
        this.myname = "";
    }

    returnName(myname) {
        this.myname = myname;
        console.log(myname);
    }
}

class childClass3 extends parentClass3 {
    constructor() {
        super();
        this.myage = 0;
    }

    returnAge(num) {
        this.myage = num;
        console.log(num);
    }
}

let myClass3 = new childClass3();
myClass3.returnName("Okasha");
myClass3.returnAge(18);
console.log(myClass3);
