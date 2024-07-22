```markdown
# TinyTales

TinyTales is an initiative to encourage young children to become future authors by providing them a platform to write, share, and showcase their stories. This web application allows children to create their own books, view books written by others, and engage in the joy of storytelling.

## Features

- **Add Authors**: Allows users to add new authors.
- **Add Books**: Enables users to add new books written by the authors.
- **Search Books**: Provides a search functionality to find books by title.
- **Sort Books**: Allows sorting of books by title or author.
- **Delete Books**: Enables deletion of books, and also deletes the author if they have no other books.
- **User-Friendly Interface**: A simple and intuitive interface for children to navigate and use.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/tinytales.git
    cd tinytales
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Run the application:
    ```bash
    flask run
    ```

6. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

```
TinyTales/
├── app.py                # The main Flask application
├── data_models.py        # Database models for Authors and Books
├── templates/
│   ├── home.html         # Main page template
│   ├── add_author.html   # Template for adding a new author
│   ├── add_book.html     # Template for adding a new book
└── static/
    └── style.css         # CSS styles (if any)
```

## Routes

- **Home (`/`)**: Displays the list of books with search and sort functionalities.
- **Add Author (`/add_author`)**: Page to add a new author.
- **Add Book (`/add_book`)**: Page to add a new book.
- **Delete Book (`/book/<int:book_id>/delete`)**: Endpoint to delete a book.

## Future Enhancements

- **User Authentication**: Add user authentication to allow personalized experiences.
- **Book Reviews**: Enable users to leave reviews for books.
- **Rating System**: Implement a rating system for books.
- **Advanced Search**: Include advanced search functionalities like searching by author, genre, etc.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Flask community for their amazing support and resources.
- Inspired by the need to foster creativity and literacy among young children.

```
