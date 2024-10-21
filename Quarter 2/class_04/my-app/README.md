## Class 03 Overview

### Key Learning Objectives:
- Creating simple page navigation and routes in Next.js.
- Using the `Link` component for easy navigation.
- Learning how to make dynamic routes by using brackets (e.g., placing the folder name inside `[ ]` to create dynamic routes).
- Fetching data from a JSON API to display a product listing using the `map` function.
- Navigating to a product's detail page when clicking on it and displaying the product's ID and title on the detail page.

### Steps Covered:
1. **Heading for Home Page:**
   - Added a basic heading to indicate that it’s the home page.

2. **Creating an About Page:**
   - Created an `about` folder.
   - Added a `page.tsx` file within the folder to establish an `/about` route.
   - Accessed the About page by appending `/about` to the localhost URL.

3. **Building a Navigation Bar:**
   - To simplify navigation, created a `Navbar` component.
   - Displayed the `Navbar` component within the `layout.tsx` so that it appears on every page, enabling easy navigation across the site.

4. **Working with Sub-Routes:**
   - Practiced creating sub-routes by adding `/products/proct01` and `/products/proct02`.

5. **Implementing Dynamic Routes:**
   - Learned how to create dynamic routes by naming the folder inside the `products` folder as `[productId]`. This allows navigation to dynamic routes like `/products/[productId]`, making the routes flexible for different products.

6. **Fetching Data with JSON API:**
   - Used a JSON API to fetch and display a list of 100 products. The products were rendered on the product listing page using the `map` function.
   - Each product links to its own detail page, where the product's ID and title are displayed dynamically.

7. **Using the `Link` Component:**
   - All navigation between routes was handled using the `Link` component, imported from Next.js for efficient navigation.

### Key Takeaway:
This class focused on creating basic and dynamic routes, fetching and displaying product data from an API, and improving site navigation using the `Link` component in Next.js. The key emphasis was on working with dynamic content and routing.

