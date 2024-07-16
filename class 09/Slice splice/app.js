// Slice 
// Main Array 
var studArr = ["ali", "Okasha", "Saad", "bilal"];
console.log(studArr);
// the slice method would return the selected element in an array as a new array 
// the slice method does not change the original array 
// it has two arrguments first one is from where you want to start 
// and second one is till where you want to end but it would end before the last one
var student1 = studArr.slice(1, 3);
console.log(student1);
// it would give the result as 
// ["Okasha", "Saad"] 
// original array is not change 
console.log(studArr);
// Splice
var studArr2 = ["Ali", "saad", "asad", "okasha"];
console.log(studArr2);
// splice method add and remove array Element 
// the splice method overwrite the original array
// returns deleted element in array 
var student2 = studArr2.splice(0, 3, "Ayesha");
console.log(student2);
// original array changed 
console.log(studArr2);
