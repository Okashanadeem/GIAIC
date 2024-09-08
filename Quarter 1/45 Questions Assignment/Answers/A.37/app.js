// 37. Large Shirts: Modify the make_shirt() function so that shirts are large
// by default with a message that reads I love TypeScript. Make a large shirt and a
// medium shirt with the default message, and a shirt of any size with a different
// message.
function make_shirt(size, message) {
    if (size === void 0) { size = "large"; }
    if (message === void 0) { message = "I love TypeScript"; }
    console.log("the size of the t-shirt should be ".concat(size, " and the message on t-shirt should be this: ").concat(message));
}
make_shirt("medium");
make_shirt("large", "Keep Calm and Code On");
