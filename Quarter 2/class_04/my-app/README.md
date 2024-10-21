## Class 04 Overview

### Key Learning Objectives:
1. Completing the topics from Class 03 that were left unfinished (view Class 03 code [here](https://github.com/Okashanadeem/GIAIC/tree/main/Quarter%202/class_03)).
2. Fetching data from the JSON Placeholder API and displaying it as a product listing.
3. Understanding the `map` method deeply, including its three parameters.
4. Creating dynamic routes for products using Next.js.

### Steps Covered:

1. **Fetching Data from JSON Placeholder:**
   - Fetched data from the JSON Placeholder API.
   - Displayed a product listing using the fetched data, showing key details such as title, body, and ID.

2. **Understanding the `map` Method:**
   - Explored the `map` method and its three parameters:
     - **First Parameter (Element):** Represents the current element being processed in the array.
     - **Second Parameter (Index):** The index of the current element within the array.
     - **Third Parameter (Array):** The entire array that the `map` method is called on.
   - Demonstrated the use of `map` to loop through the product list and render each item dynamically.

3. **Displaying Product Details:**
   - Set up functionality where, upon clicking a product, the user is taken to a detail page.
   - The detail page displays the `product.title`, `product.body`, and `product.id`.

4. **Dynamic Routes for Products:**
   - Created a dynamic route by naming the folder as `[product]` inside the `products` directory.
   - This allows users to visit a URL like `/products/[product]` and be redirected to the corresponding product's detail page.
   - If the product doesn't exist, no details (title, body, or ID) are shown.

5. **Working with Objects and Arrays Using `map`:**
   - Learned how to use the `map` method to convert arrays into objects and vice versa.
   - Created a `map method` folder inside the `src` directory, and a `map.ts` file within it to showcase different examples of using the `map` method for transformations.

### Key Takeaway:
- This class provided a deeper understanding of the `map` method, dynamic routing in Next.js, and the process of fetching and displaying data from an API. It also covered transforming arrays and objects using the `map` method, enhancing data manipulation skills.
