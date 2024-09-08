// first parameter in promise is resolved and secoud is Rejected.
// So, first we would do resolve and then after reject. 
// Resolved
let myPromise1 = new Promise((resolved, rejected) => {
    console.log("promise pending");
    setTimeout(() => {
        console.log("Promise resolved");
        resolved(["Ali", "Okasha"]);
    }, 2000);
});
myPromise1.then((res) => { console.log(res); }).catch((err) => { console.log(err); });
// Rejected
let myPromise2 = new Promise(function (resolved, rejected) {
    console.log("promise pending");
    setTimeout(function () {
        console.log("Promise Rejected");
        rejected(new Error("An unknown Erroe occured"));
    }, 2000);
});
myPromise2.then(function (res) { console.log(res); }).catch(function (err) { console.log(err); });
export {};
