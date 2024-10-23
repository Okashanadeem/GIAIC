## Class 05 Overview

### Key Learning Objectives:
1. Understanding the difference between static and dynamic pages in Next.js.
2. Making requests either dynamically or statically using fetch.
3. Implementing loading states in a Next.js application.
4. Handling errors gracefully in Next.js.
5. Adding images to pages and styling them with Tailwind.
6. Utilizing a fake API to fetch dynamic data and displaying it on the page.

### Differences Between Static and Dynamic Pages:
- **Static Pages:**
  - Content is generated at build time.
  - The same content is served for every request until the next build.
  - Can be cached for improved performance.

- **Dynamic Pages:**
  - Content is generated at request time.
  - Different content can be served based on the request.
  - Typically involves fetching data from an API or server on each request.

### Fetching Data in Next.js:
- For dynamic requests, use:
  ```javascript
  const fetchData = await fetch(`https://jsonplaceholder.typicode.com/posts/${params.product}`, {cache: "no-store"});
  ```
- For static requests, use:
  ```javascript
  const fetchData = await fetch(`https://jsonplaceholder.typicode.com/posts/${params.product}`, {next: {revalidate: 2000}});
  ```

### Steps Covered:

1. **Implementing Loading States:**
   - Created a `loading.tsx` file with the following code:
     ```javascript
     export default function Loading() {
       return <h3>Data is being fetched, please wait...</h3>;
     }
     ```
   - This allows a loading message to display while waiting for data when navigating from the product listing.

2. **Error Handling:**
   - Implemented error handling by copying the code from Next.js documentation to ensure the application can gracefully handle any issues during data fetching.

3. **Adding Images to Pages:**
   - Learned to add images by:
     - Importing the image and using it in the `src` attribute.
     - Using the `require` method to specify the image's location.
   - Applied basic styling using Tailwind CSS to enhance the image presentation.

4. **Using a Fake API:**
   - Utilized the fake API: 
     ```
     https://fakerapi.it/api/v1/persons?_locale=en_US&_quantity=1
     ```
   - Explained the second parameter of the fetch method and its importance.
   - Printed the fetched array in the console and displayed the first name and last name of the user on the page.
   - Made the page dynamic, so refreshing it fetches new data.

### Key Takeaway:
This class focused on understanding static versus dynamic content, implementing loading and error handling in Next.js, adding images, and using an external API to create a dynamic user experience.
