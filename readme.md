
# FastAPI CRUD Application 

This is a basic FastAPI application that demonstrates a CRUD (Create, Read, Update, Delete) setup with SQLite using SQLAlchemy and Pydantic for data validation.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Endpoints](#endpoints)
- [Running the Application](#running-the-application)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shahjalal-bu/fast-api-blog.git
   cd fast-api-blog
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create the SQLite database:**
   The database will automatically be created when you run the application.

## Project Structure

```
Root folder
├── venv/                 # Virtual environment
├── app/
│   ├── __init__.py       # Package init file
│   ├── main.py           # Main FastAPI application
│   ├── database.py       # Database configuration with SQLAlchemy
│   └── schemas.py        # Pydantic models for request/response validation
└── README.md             # Project readme
```

## Endpoints

The application includes the following endpoints:

- **`POST /blog`**: Create a new blog post.
- **`GET /blogs`**: Retrieve a list of blog posts.
- **`GET /blog/{id}`**: Retrieve a single blog post by ID.
- **`PUT /blog/{id}`**: Update a blog post by ID.
- **`DELETE /blog/{id}`**: Delete a blog post by ID.

### Example Requests

To test the API endpoints, you can use [curl](https://curl.se/), [Postman](https://www.postman.com/), or [httpie](https://httpie.io/).

#### Create a Blog Post

```http
POST /blog
Content-Type: application/json

{
  "title": "My Blog Title",
  "body": "This is the content of my blog post."
}
```

#### Get All Blog Posts

```http
GET /blogs
```

## Running the Application

1. **Run the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the interactive API documentation:**
   Open your browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view the automatically generated API documentation.

## License

This project is provided **without a license**. You are free to use, modify, and distribute this code as you see fit. No attribution or additional permissions are required.
