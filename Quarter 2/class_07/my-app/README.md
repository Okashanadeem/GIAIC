### Class 7: Understanding Tailwind CSS

---

#### What is Tailwind CSS?
Tailwind CSS is a utility-first CSS framework that provides a set of pre-defined classes to style HTML elements quickly. It allows developers to build responsive and customizable user interfaces without having to write custom CSS. Tailwind focuses on flexibility and speed, providing utilities for common styling tasks such as margins, paddings, colors, typography, and more.

For more information, visit the [Tailwind CSS official documentation](https://tailwindcss.com/). The documentation explains everything in detail and provides examples on how to use Tailwind to its full potential.

---

#### Typography in Tailwind CSS
Tailwind CSS allows you to change fonts and apply various font styles using utility classes. Here are a few examples:

- **Font family**:
  ```html
  <p class="font-sans">This is a paragraph with the sans-serif font family.</p>
  <p class="font-serif">This is a paragraph with the serif font family.</p>
  ```

- **Font sizes**:
  ```html
  <p class="text-xs">Extra Small Text</p>
  <p class="text-sm">Small Text</p>
  <p class="text-base">Base Text</p>
  <p class="text-lg">Large Text</p>
  <p class="text-xl">Extra Large Text</p>
  <p class="text-2xl">Double Extra Large Text</p>
  ```

- **Font weights**:
  ```html
  <p class="font-light">Light Font Weight</p>
  <p class="font-normal">Normal Font Weight</p>
  <p class="font-medium">Medium Font Weight</p>
  <p class="font-semibold">Semi Bold Font Weight</p>
  <p class="font-bold">Bold Font Weight</p>
  ```

- **Font styles**:
  ```html
  <p class="italic">This text is italicized.</p>
  <p class="not-italic">This text is not italicized.</p>
  ```

---

#### Web Layout with Tailwind CSS
Tailwind provides built-in responsive breakpoints to create layouts that adapt to different screen sizes. Here is how you define breakpoints in your Tailwind configuration file (`tailwind.config.ts`):

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  theme: {
    screens: {
      'sm': '640px',
      // => @media (min-width: 640px) { ... }

      'md': '768px',
      // => @media (min-width: 768px) { ... }

      'lg': '1024px',
      // => @media (min-width: 1024px) { ... }

      'xl': '1280px',
      // => @media (min-width: 1280px) { ... }

      '2xl': '1536px',
      // => @media (min-width: 1536px) { ... }
    }
  }
}
```

These breakpoints allow you to create responsive designs by applying different styles for different screen sizes. For example:

- `lg`: styles applied for screens with a minimum width of 1024px
- `xl`: styles applied for screens with a minimum width of 1280px
- `2xl`: styles applied for screens with a minimum width of 1536px

---

### Assignment

For your assignment, you need to:

1. **Create a portfolio using Tailwind CSS**:
   - Building a portfolio will help you practice various TypeScript and Next.js topics such as routing, state management, and component reusability.
   - Checkout the project which I have made: ([Link](https://github.com/Okashanadeem/GIAIC/tree/main/Quarter%202/class-07/Assignment/Portfolio))

2. **Design a FaceBook login page with Tailwind and CSS**:
   - Creating this page will allow you to practice styling and integrating forms with Tailwind, and understand how to create responsive layouts.
   - Checkout the project which I have made: ([Link](https://github.com/Okashanadeem/GIAIC/tree/main/Quarter%202/class-07/my-app/src/app/facebook))

3. **Build a Todo Application using Tailwind CSS**:
   - Developing a Todo Application will teach you about CRUD operations (Create, Read, Update, Delete) in Next.js while enhancing your ability to use Tailwind for responsive and interactive UIs.
   - Checkout the project which I have made: ([Link](https://github.com/Okashanadeem/GIAIC/tree/main/Quarter%202/class-07/my-app/src/app/todo))

These projects will also reinforce your understanding of React, Next.js, and Tailwind CSS, enhancing your ability to create efficient and appealing web applications.

For detailed tutorials and examples, check out these links:
- **Portfolio**: [YouTube Tutorial](https://youtu.be/XrES0mj_07w?si=4gCnB2YhwQCDbEed)
- **FaceBook login page**: [YouTube Tutorial](https://youtu.be/XrES0mj_07w?si=4gCnB2YhwQCDbEed)
- **Todo Application**: [YouTube Tutorial](https://youtu.be/053kfsm9CdE)

These tutorials will guide you through the process step-by-step, helping you utilize Tailwind effectively to create responsive and visually appealing designs.