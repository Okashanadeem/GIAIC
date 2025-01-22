```markdown
# Marketplace Project (Marketplace_Builder_Hackathon_2025)

## Day 6 (Deployment Preparation and Staging Environment Setup)

## Project Overview
The **Marketplace Project** is an e-commerce platform designed to display and sell various products. It offers a user-friendly interface with features like product listing, search functionality, and cart management. The project utilizes **Next.js**, **Sanity CMS** for content management, and **ShadCN** for UI components. It is deployed on **Vercel** for a seamless experience. The goal is to create a robust, responsive, and dynamic marketplace platform.

## Deployment

### Staging URL
- **[Staging Environment](https://marketplace-builder-hackathon-2025-proje-okashanadeems-projects.vercel.app/)**

### Deployment Steps
1. **Vercel Setup:**
   - Connected the GitHub repository to Vercel.
   - Deployed using **Next.js** with default build and deployment settings.

2. **Environment Variables:**
   - Configured environment variables in `.env.local` and Vercel for secure API access.
   - Key variables:
     - `NEXT_PUBLIC_SANITY_PROJECT_ID`: Sanity project ID
     - `NEXT_PUBLIC_SANITY_DATASET`: Sanity dataset (e.g., `production`)
     - `SANITY_API_KEY`: Sanity API key

## Features
- **Product Listing:** Displays products fetched from Sanity CMS.
- **Search Functionality:** Allows users to search for products by name or category.
- **Cart Operations:** Users can add, modify quantities, and remove items from the cart.
- **ShadCN Components:** Utilizes pre-built responsive UI components like buttons, input fields, and labels for a polished user experience.

## How to Test or Use the Project

### 1. **Access the Live Demo**
You can view the live version of the marketplace in both the staging and production environments:
- **[Staging Environment](https://marketplace-builder-hackathon-2025-proje-okashanadeems-projects.vercel.app/)**

### 2. **Testing the Application Locally**

#### Prerequisites
- **Node.js** (version 14 or higher)
- **npm** (Node Package Manager)

#### Steps to Test Locally:
1. **Clone the Repository:**
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Okashanadeem/Marketplace_Builder_Hackathon_2025-project-deploy.git
   cd marketplace-project
   ```

2. **Install Dependencies:**
   Install required dependencies:
   ```bash
   npm install
   ```

3. **Set Up Environment Variables:**
   Create a `.env.local` file and add the necessary environment variables:
   ```env
   NEXT_PUBLIC_SANITY_PROJECT_ID=your_project_id
   NEXT_PUBLIC_SANITY_DATASET=production
   SANITY_API_KEY=your_api_key
   ```

4. **Run the Development Server:**
   Start the development server:
   ```bash
   npm run dev
   ```
   The application will be available at `http://localhost:3000`.

5. **Test the Application:**
   - Check key functionalities:
     - **Product Listing**: Ensure products are listed and displayed correctly.
     - **Dynamic Product Detail**: Click any product to view its details.
     - **Search**: Test the search functionality.
     - **Cart Operations**: Add/remove items in the cart.
     - **ShadCN Components**: Ensure buttons, modals, and input fields work correctly.

#### Testing Features:
- **Functional Tests:** Verify key features like product listing, search, and cart management.
- **Performance Tests:** Use Lighthouse to ensure the app loads quickly and is responsive.
- **Security Tests:** Ensure input sanitization, HTTPS, and secure handling of sensitive data.

### 3. **Running Tests**

If automated tests are set up, run them using the following tools:

- **Cypress (for functional testing):**
   ```bash
   npm run cypress:open
   ```

- **Performance Testing (Lighthouse, GTmetrix):**
   - **Lighthouse:** Use Chrome DevTools to generate a performance report.
   - **GTmetrix:** Visit [GTmetrix](https://gtmetrix.com/) to test the website’s performance.

- **Postman (for API testing):**
   Use Postman to verify API endpoints, ensuring proper backend integration with Sanity CMS.

### 4. **Submitting Feedback or Issues**
If you encounter issues or have feedback:
- Check the [Issues](https://github.com/Okashanadeem/Marketplace_Builder_Hackathon_2025-project-deploy/issues) section on GitHub.
- Open a new issue for bugs or feature requests.

---

## File Structure
The project files are organized as follows:

```
marketplace-project/
│
├── documents/
│   └── (Day 1) Marketplace Business Goals - Ecommerce furniture platform
│   └── (Day 2) Marketplace Technical Foundation - Ecommerce Furniture platform
│   └── (Day 3) API Integration Report - Ecommerce Furniture platform
│   └── (Day 4) Building Dynamic Frontend Components for Your Marketplace - Ecommerce Furniture platform
│   └── (Day 5) Testing, Error Handling, and Backend Integration Refinement - Ecommerce Furniture platform
│
├── test-case-report.csv  (located in the Day 5 folder)
├── performance-report.pdf
└── README.md
```

- **`documents/`**: Contains all documentation files (test reports, performance reports).
- **`src/`**: Source code (React components, API integration, etc.).
- **`components/`**: Reusable UI components built with **ShadCN**.
- **`public/`**: Static assets (images, icons, etc.).
- **`.env.local`**: Environment variables (e.g., Sanity API keys).

## Conclusion
This project demonstrates the creation of a marketplace platform using **Next.js**, **Sanity CMS**, and **ShadCN** components. Key features include product management, user authentication, UI components, and testing. The project is successfully deployed, and all tests have been documented for further validation.

For more information, please refer to the [GIAIC](https://github.com/Okashanadeem/GIAIC/tree/main/Quarter%202/Hackathons/Hackathon%2003%20(Sanity%20%26%20mokeApi)/Hackathon).

> Above is the official repo where I post my daily work or everything related to GIAIC, with well-organized files and clear documentation.
