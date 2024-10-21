var arr = [1, 2, 3, 4, 5]; //Original Array
console.log("original Array: ", arr);
var newArr1 = arr.map(function (val) {
    console.log("newArr1: ", val);
});
//first param is the value in which the map is working on
var newArr2 = arr.map(function (val, i) {
    console.log("newArr2: ", val, i);
});
//second param shows the index of value on which map is working
var newArr3 = arr.map(function (val, i, origArr) {
    console.log("newArr3: ", val, i, origArr);
});
//third param is used to print the original array with each value on which map is working on.
// Now we would work on Array of object 
var arrOfObj = arr.map(function (elem, i, origArr) {
    return {
        elemVal: elem,
        elemIndex: i,
        refArr: origArr
    };
});
console.log("arrOfObj: ", arrOfObj);
// now make the array again through object 
var duplicateArr = arrOfObj.map(function (elem) {
    return elem.elemVal;
});
console.log("duplicateArr: ", duplicateArr);
