# Django-Blog
# Django-Blog
Features:

**1. User Authentication:**

Admin users can log in to manage blog posts.
Regular users can register and log in to view posts but cannot add new ones.
![image](https://github.com/user-attachments/assets/326d502e-900d-4159-b58a-45fe6a6be905)

**2. Blog Post Management:**

Admins can create, edit, and delete blog posts.
Blog posts will include fields like title, content, author, and publication date.
![image](https://github.com/user-attachments/assets/65443e4e-5b41-4795-b42b-46ed6bb6238a)

**3. Viewing Posts:**

All users can view a list of all published blog posts.
Users can click on individual posts to read the full content.
![image](https://github.com/user-attachments/assets/3a726cd0-14a9-4ea7-82cb-79e1d047fd2c)

**4. Frontend:**

Basic HTML templates for listing posts and viewing individual posts.
A user-friendly interface for easy navigation.
**5. Models:**

A Post model with attributes for title, content, author (ForeignKey to User), and created_at timestamp.
**6. URLs and Views:**

URL patterns to handle different views (e.g., list of posts, detail view of a single post).
Views to handle the logic for displaying posts and processing form submissions for admins.

**Add Blog**
![image](https://github.com/user-attachments/assets/3f660e4b-531e-4ac8-9a9e-6d618f0ad604)

**Update Blog**
![image](https://github.com/user-attachments/assets/81f106b8-2e24-46e0-a3b7-e58b6be21bc1)


