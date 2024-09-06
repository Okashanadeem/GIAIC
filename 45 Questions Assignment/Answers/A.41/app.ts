// 41. Magicians: Make a array of magician’s names. Pass the array to a function
// called show_magicians(), which prints the name of each magician in the array.

let magicianName : string[] = ["Ali","Okasha","Shahzaib","Armughan"]
let printName = () => {
    magicianName.forEach(name =>{
        console.log(name)
    })
}
printName()