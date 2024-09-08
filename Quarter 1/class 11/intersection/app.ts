type personalDetail1 = {
    name : string,
    gendre : String,
    age : number
};
type personalDetail2 = {
    education : string,
    job : string,
    experience : number
};
type person = personalDetail1 & personalDetail2;  //two types are intersected here in one type 

let user : person = {
    name : "Okasha",
    age : 18,
    gendre : "boy",
    education : "1st year",
    job : "website developer",
    experience : 2
};