# Class 09: Understanding Components and APIs

## Topics Covered

### 1. Using Shadcn UI Components
We explored various basic components from Shadcn UI. Below are the components we discussed:
- **Theme**  
- **Accordion**  
- **Alert Dialog**  
- **Card**  
- **Calendar**  
- **Combo Box**  
- **Sheet**  
- **Command**  
- **Table**

For more details about these components, you can refer to the [Shadcn UI Documentation](https://ui.shadcn.dev/).

---

### 2. Introduction to APIs
We learned the fundamentals of APIs (Application Programming Interfaces).

- **Definition**:  
  APIs are sets of rules, protocols, and tools that allow different software applications to communicate with each other. They act as intermediaries, enabling data exchange and task execution between systems.

---

### 3. Working with an API Using Postman
- We used a simple books API provided by Postman for practice.
- **API Documentation**: [Simple Books API](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md)
- **Base API URL**: [https://simple-books-api.glitch.me/](https://simple-books-api.glitch.me/)

---

### 4. API Endpoints
APIs have endpoints, which are specific URLs used to access certain functionalities. Examples include:
- **Get All Books**: `https://simple-books-api.glitch.me/books`
- **Get a Specific Book**: `https://simple-books-api.glitch.me/books/4`
- **Data Not Found Example**:  
  If a resource is not found, you may encounter an error. For example:
  - `https://simple-books-api.glitch.me/books/40`
  - Returns: **Status 404** (Not Found)

---

### 5. HTTP Methods
We learned about different HTTP methods:
- **GET**: Retrieve data.
- **POST**: Send new data.
- **PUT**: Update existing data.
- **DELETE**: Remove data.

---

### 6. API Status Codes
- **200**: OK (The request was successful).
- **404**: Not Found (The requested resource does not exist or the URL is incorrect).
- **401**: Unauthorized (Authentication is required).
- **400**: Bad Request (The request is malformed or invalid).
- **201**: Created (The request was successful, and a resource was created).

---

### API Interaction Examples

1. **Create a new client**:
   ```http
   POST https://simple-books-api.glitch.me/api-clients
   {
     "clientName": "Okasha Nadeem",
     "clientEmail": "okashanadeem0101@gmail.com"
   }
   ```
   **Response**:
   - Status: **201 Created**

2. **Order a book**:
   ```http
   POST https://simple-books-api.glitch.me/orders
   {
     "bookId": 3,
     "customerName": "Okasha Nadeem"
   }
   ```
   - **Authorization**: Use the bearer token obtained from the last step.
   - **Response**:
     - Status: **201 Created**
     - `{"created": true, "orderId": "T_wTCahMHby-OwILVFljR"}`

3. **Get all orders**:
   ```http
   GET https://simple-books-api.glitch.me/orders
   ```
   - **Authorization**: Use the bearer token.
   - **Response**:
     - Status: **200 OK**
     - `[
       {
         "id": "T_wTCahMHby-OwILVFljR",
         "bookId": 3,
         "customerName": "Okasha Nadeem",
         "createdBy": "d7837dd22bbadc54ebdaf5bb38d99f2c9dbdc63779b09fa1ada42c08e515a81f",
         "quantity": 1,
         "timestamp": 1734336466384
       }
     ]`

4. **Get a specific order**:
   ```http
   GET https://simple-books-api.glitch.me/orders/T_wTCahMHby-OwILVFljR
   ```
   - **Authorization**: Use the bearer token.
   - **Response**:
     - Status: **200 OK**
     - `{
       "id": "T_wTCahMHby-OwILVFljR",
       "bookId": 3,
       "customerName": "Okasha Nadeem",
       "createdBy": "d7837dd22bbadc54ebdaf5bb38d99f2c9dbdc63779b09fa1ada42c08e515a81f",
       "quantity": 1,
       "timestamp": 1734336466384
     }`

5. **Update an order**:
   ```http
   PATCH https://simple-books-api.glitch.me/orders/T_wTCahMHby-OwILVFljR
   {
     "customerName": "Ratan Lal"
   }
   ```
   - **Authorization**: Use the bearer token.
   - **Response**:
     - Status: **204 No Content**

6. **Delete an order**:
   ```http
   DELETE https://simple-books-api.glitch.me/orders/T_wTCahMHby-OwILVFljR
   ```
   - **Authorization**: Use the bearer token.
   - **Response**:
     - Status: **204 No Content**

---

### Final Verification After Deletion
- **Verify the deletion**:
  ```http
  GET https://simple-books-api.glitch.me/orders/T_wTCahMHby-OwILVFljR
  ```
  - **Authorization**: Use the bearer token.
  - **Response**:
    - Status: **404 Not Found**
    - `{"error": "No order with id T_wTCahMHby-OwILVFljR."}`


### Figma Practice Project

In this class, we also had a Figma practice project. Below is the link to the Figma design for reference:

**Figma Project Link**:  
[My FirstWebsite](https://www.figma.com/design/4rWP2iWijt9Unky39tzLyD/My-FirstWebsite?node-id=0-1&t=5ohw3sQnJ24ZyxcU-1)

Feel free to explore and use this design as a basis for your practice or real project development!

### picture gallery
[Youtube link of IT Mate for cloudinary](https://www.youtube.com/playlist?list=PLplW4d4HPsEJC7XVLYgbKL4iZFyRN1rBk)