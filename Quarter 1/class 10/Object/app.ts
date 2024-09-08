// Object 

// Object has a key and a value 
// you can add amount of data you want 

let obj = {
    name: "ali",
    gendre : "boy",
    age : 20,
    happy : true,
    cars : ["civic","Gtr","Rx-8","audi R8"],
    salary : () => (1000),
    skills : {
        skill1 : "website developer",
        skill2 : "Graphic designer",
        skill3 : "Digital marketer"
    }
}

// main abj 
console.log(obj);

// you can also call each of them 
console.log(obj.name);
console.log(obj.age);
console.log(obj.happy);
console.log(obj.cars);
console.log(obj.cars[2]);
console.log(obj.salary());
console.log(obj.skills);
console.log(obj.skills.skill1)

// if you want to add a new content in onject then do this 
obj.address = "Hno-G223";
console.log(obj.address);

// if you want to delete any content from an object then 
delete obj.gendre;
console.log(obj);

// if you want to check any content in abject then 
console.log("gendre" in obj);