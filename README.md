# Flask CRUD API

This is a simple Flask CRUD (Create, Read, Update, Delete) API for managing contacts. Contacts are stored in a JSON file.

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/user/crud.git

2. Install dependencies:

   ```bash
      pip install Flask

## Usage

1. Run the Flask application:

   ```bash
     python app.py

2. Access the API endpoints:

   Create a contact:
   ```bash
   curl -X POST http://127.0.0.1:5000/contacts -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com", "phone": "123-456-7890"}'
   ```
  Get all contact:
   ```bash
    curl http://127.0.0.1:5000/contact
   ```
Get specific contact
  ```bash
  curl http://127.0.0.1:5000/contacts/1
  ```

  Update contact:
  ```bash
  curl -X PUT http://127.0.0.1:5000/contacts/1 -H "Content-Type: application/json" -d '{"name": "John Smith"}'
  ```

  Delete a contact:
  ```bash
  curl -X DELETE http://127.0.0.1:5000/contacts/1\
  ```
