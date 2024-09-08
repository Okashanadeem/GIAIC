async function fetchDataFunc() {
    let url = "https://jsonplaceholder.typicode.com/todos/1";
    let fetchdata = await fetch(url);
    let responce = await fetchdata.json();
    console.log(responce);
}
fetchDataFunc();
export {};
