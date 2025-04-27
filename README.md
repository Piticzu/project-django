# Django Chatbot Page

A simple Django-based chatbot page with HTMX integration.  
Built for personal learning and experimentation with session management, dynamic UI updates, and backend structure.

## Features

- Django backend for message handling
- HTMX for dynamic message loading without full page reloads
- Session-based chat history
- Automatic scroll to the latest message
- Basic user input escaping for security

## Technologies Used

- Python 3
- Django
- HTMX
- TailwindCSS (optional, for styling)

## Project Structure

- `views.py` — Handles user input, chat history, and bot responses
- `templates/` — Contains modular HTML fragments
- `urls.py` — Defines routing for chat actions

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/Piticzu/project-django-chatbotpage.git
    cd project-django-chatbotpage
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the server:

    ```bash
    python manage.py runserver
    ```

5. Open your browser at `http://127.0.0.1:8000/`

## Notes
- Focus areas: Django session handling, HTMX dynamic updates, clean code organization.
- No advanced features like user authentication or external database connections are included.

## License

This project is open for personal use and learning.

