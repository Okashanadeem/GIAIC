// 38. Cities: Write a function called describe_city() that accepts the name of
// a city and its country. The function should print a simple sentence, such as
// Karachi is in Pakistan. Give the parameter for the country a default value.
// Call your function for three different cities, at least one of which is not in the
// default country.
var describe_city = function (cityName, countryName) {
    if (countryName === void 0) { countryName = "Pakistan"; }
    console.log("".concat(cityName, " is in the ").concat(countryName));
};
describe_city("Islamabad");
describe_city("Peshawar");
describe_city("Mumbai", "India");
