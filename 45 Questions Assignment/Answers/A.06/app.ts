// 6. Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name after striping the white spaces.

//  \t and \n 
// \t is for adding a block of space and \tn is use for moving to next line in console, its like a <br/> tag 
console.log("Okasha is\ta Website developer. \nOkasha is a typescript developer.")


//.trim()
let person_name = "            Okasha  ";
let trim_name = person_name.trim();
console.log(person_name);