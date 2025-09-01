# 📚 Book Collection API
My first Django REST API project with full CRUD operations. Built this to practice creating, reading, updating, and deleting data through REST endpoints.
Features books from some of my favorite authors like Stephen King and J.K. Rowling.

## Technology Stack
- Python 3.x
- Django
- Django REST Framework
- SQLite

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/sanjay-s22/Book-collection_DRF.git
   cd book-collection_DRF
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books/` | Retrieve all books |
| POST | `/api/books/` | Create a new book |
| GET | `/api/books/{id}/` | Retrieve a specific book |
| PUT | `/api/books/{id}/` | Update a specific book |
| DELETE | `/api/books/{id}/` | Delete a specific book |

## Example Response

```json
{
  "id": 1,
  "title": "The Shining",
  "author": "Stephen King",
  "publication_year": 1977,
  "genre": "Horror"
}
```

## Testing
All endpoints have been tested using Postman to ensure proper functionality and correct HTTP status codes.

---
**Built by [S.Sanjay]** | https://github.com/sanjay-s22
