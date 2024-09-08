"use strict";
class parentClass1 {
}
class childClass1 extends parentClass1 {
}
let myClass1 = new childClass1;
myClass1.name = "Okasha";
myClass1.age = 20;
myClass1.gender = "male";
console.log(myClass1);
class parentClass2 {
    returnName(name) {
        return console.log(name);
    }
}
class childClass2 extends parentClass2 {
    returnAge(num) {
        return console.log(num);
    }
}
let myClass2 = new childClass2;
myClass2.returnName("Okasha");
myClass2.returnAge(18);
// Class Inheritance with Method Properties
class parentClass3 {
    constructor() {
        this.name = "";
    }
    returnName(name) {
        this.name = name;
        console.log(name);
    }
}
class childClass3 extends parentClass3 {
    constructor() {
        super();
        this.age = 0;
    }
    returnAge(num) {
        this.age = num;
        console.log(num);
    }
}
let myClass3 = new childClass3();
myClass3.returnName("Okasha");
myClass3.returnAge(18);
console.log(myClass3);
