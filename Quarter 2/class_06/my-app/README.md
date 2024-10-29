# Class 06 Summary

In this class, we covered key concepts in Next.js related to routing, component layout, and React hooks.

## Topics Covered

1. **Route Grouping**
   - We learned how to create an organized structure for routes by using folders with names inside parentheses `()`.
   - This setup allows for dynamic routing. When a subfolder is created within these parent folders, it will open dynamically in the app, improving navigation and scalability.

2. **Dynamic Layouts**
   - Adding a `layout.tsx` file in dynamic folders enables consistent content display across specific routes.
   - Any elements written before or after the `children` prop within `layout.tsx` will appear in routes within that dynamic folder, ensuring a unified layout.

3. **useState Hook**
   - We practiced using the `useState` hook to manage component state.
   - A variable named `name` was created, and a button was added to update this variable's value on click, demonstrating interactive state management with `useState`.

4. **useEffect Hook**
   - We explored the `useEffect` hook and the role of its second parameter, the dependency array.
   - Different behaviors were observed by varying the dependency array:
     - No dependencies: `useEffect` runs on every render.
     - Empty array: `useEffect` runs only once when the component mounts.
     - Specific dependencies (e.g., `name`): `useEffect` runs only when those dependencies change.

## Notes

- This class emphasized building clean and structured code, handling dynamic layouts, and using React hooks effectively for interactivity and lifecycle management.
- Practicing these concepts will enhance file organization and user experience in Next.js projects.

