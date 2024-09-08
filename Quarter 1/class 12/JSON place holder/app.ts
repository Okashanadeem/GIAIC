async function fetchDataFunc1 () {
    try{
    let url = "https://jsonplaceholder.typicode.com/todos/1"
    let fetchdata = await fetch(url)
    let responce = await fetchdata.json()
    console.log(responce)
    } catch(error){
        console.log("Please Handle The Error")
    }
}
fetchDataFunc1();

async function fetchDataFunc2() {
    let url = "https://jsonplaceholder.typicode.com/todos/1"
    let fetchData = await fetch(url)//fetching the data from the Url
    let responce = await fetchData.json() //.JSON() to organise the data
    console.log(responce)
}
