// 45. Cars: Write a function that stores information about a car in a Object.
// The function should always receive a manufacturer and a model name. It
// should then accept an arbitrary number of keyword arguments. Call the function
// with the required information and two other name-value pairs, such as a
// color or an optional feature. 
// Print the Object that’s returned to make sure all the information was
// stored correctly.
// Function to store information about a car, allowing arbitrary keyword arguments
// Function to store information about a car, allowing arbitrary keyword arguments
var carData = function (manufacturer, model) {
    var additionalInfo = [];
    for (var _i = 2; _i < arguments.length; _i++) {
        additionalInfo[_i - 2] = arguments[_i];
    }
    // Base car info
    var car = {
        manufacturer: manufacturer,
        model: model
    };
    // Add additional info properties to the car object manually
    additionalInfo.forEach(function (info) {
        for (var key in info) {
            if (info.hasOwnProperty(key)) {
                car[key] = info[key];
            }
        }
    });
    return car;
};
// Call the function with required information and additional key-value pairs
var car1 = carData("Honda", "Civic", { color: "Red", year: 2024 });
var car2 = carData("Toyota", "Supra", { color: "White", year: 1999, engine: "V6" });
var car3 = carData("Dodge", "Challenger", { color: "Black", year: 1996, horsepower: 485, type: "Muscle Car" });
// Print the car objects
console.log(car1);
console.log(car2);
console.log(car3);
