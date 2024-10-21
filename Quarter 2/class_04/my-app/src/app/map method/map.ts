let arr = [1,2,3,4,5]; //Original Array
console.log("original Array: ", arr)


let newArr1 = arr.map((val)=>{
    console.log("newArr1: ",val)
});
//first param is the value in which the map is working on

let newArr2 = arr.map((val , i)=>{
    console.log("newArr2: ",val , i)
});
//second param shows the index of value on which map is working

let newArr3 = arr.map((val , i , origArr)=>{
    console.log("newArr3: ",val , i , origArr)
});
//third param is used to print the original array with each value on which map is working on.



// Now we would work on Array of object 
let arrOfObj = arr.map((elem,i,origArr)=>{
    return {
        elemVal : elem,
        elemIndex : i,
        refArr : origArr
    }
})
console.log("arrOfObj: ",arrOfObj)

// now make the array again through object 
let duplicateArr = arrOfObj.map((elem) => {
    return elem.elemVal
})
console.log("duplicateArr: ",duplicateArr)