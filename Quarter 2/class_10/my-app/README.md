# Overview of Class 10

In this class, we covered the following topics:

## API Integration

We integrated an API into our project to fetch and display data dynamically. The API we used is:

**API URL:** [https://simple-books-api.glitch.me/books](https://simple-books-api.glitch.me/books)

To understand how to use this API, refer to its documentation:
[Simple Books API Documentation](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md).

### Dynamic API Fetching

We created a generic API fetcher that accepts any API URL. This fetcher allows us to reuse the logic for fetching data from different APIs. Here's how it works:

1. **Provide the API URL**: Pass the desired API URL to the fetcher.
2. **Dynamic Fetching**: The fetcher retrieves data from the API.
3. **Render Data**: We applied the `map()` method to the fetched data to render it on the page.

This process makes our code modular and efficient for handling various data sources.

## Sanity CMS

### What is Sanity?
Sanity is a modern, flexible, and highly customizable **Content Management System (CMS)**. It allows developers to define content structures, manage content, and fetch it for use in various applications.

### What is a CMS (Content Management System)?
A **Content Management System** is a software platform that enables users to create, manage, and modify content on a website without requiring technical expertise. It provides tools to:

- Organize content.
- Streamline workflows.
- Collaborate on content creation.

### Other CMS Platforms
Here are some popular CMS platforms:
- **WordPress**
- **Drupal**
- **Joomla**
- **Ghost**
- **Shopify**
- **Contentful**

### Why is Sanity a Good CMS?
Sanity stands out due to:
- **Customizable Content Models**: Define your schemas and tailor them to your needs.
- **Real-time Collaboration**: Multiple users can edit content simultaneously.
- **Headless Architecture**: Fetch content via APIs for use across platforms.
- **Extensibility**: Add plugins and extend functionality effortlessly.
- **Structured Content**: Content is stored as JSON, making it easy to query and use.

### Setting Up Sanity
We created a Sanity project by running the following command:

```bash
npm create sanity@latest -- --project myID --dataset production --template clean
```

This initialized Sanity in our project with a clean template.

### Understanding Sanity's Structure
Sanity projects are organized into:
- **Schemas**: Define the structure of your content.
- **Datasets**: Collections of content.
- **Content Studio**: A user-friendly interface for managing content.

### Creating Schemas
We created our first schema and explored the different field types available in Sanity, such as:
- Text
- Number
- Boolean
- Image
- Reference
- Array

### GROQ Query Language
We studied **GROQ** (Graph-Relational Object Queries), the query language used in Sanity. It allows us to retrieve content efficiently.

For more details, refer to the GROQ cheat sheet:
[GROQ Query Cheat Sheet](https://www.sanity.io/docs/query-cheat-sheet).

## Summary
This class provided hands-on experience with API integration and Sanity CMS. We learned how to:
1. Fetch and render data dynamically using APIs.
2. Set up and use Sanity CMS for managing structured content.
3. Query data using GROQ for efficient retrieval.

With these tools and techniques, we can create dynamic, content-rich applications efficiently.

