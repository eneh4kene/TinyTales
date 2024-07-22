import os
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from data_models import db, Author, Book

app = Flask(__name__)

# Ensure the 'data' directory exists for the SQLite database file
if not os.path.exists('data'):
    os.makedirs('data')

# Set up the SQLAlchemy database URI to point to a file in the 'data' directory
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data/library.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Secret key for session management and flash messages
app.secret_key = 'your_secret_key'

# Initialize SQLAlchemy with the Flask app
db.init_app(app)


@app.route('/')
def home():
    """
    Home route that displays a list of books.
    Sorts books by title or author based on query parameters.
    """
    search_query = request.args.get('search')
    # Get the sort parameter from the query string (default is 'title')
    sort_by = request.args.get('sort', 'title')

    # Fetch books sorted by author name if 'sort' is 'author', otherwise sort by title
    if search_query:
        books = Book.query.join(Author).filter(Book.title.ilike(f'%{search_query}%')).order_by(
            Book.title if sort_by == 'title' else Author.name).all()
    else:
        books = Book.query.join(Author).order_by(Book.title if sort_by == 'title' else Author.name).all()

    # Render the home template with the list of books
    return render_template('home.html', books=books)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    """
    Route to add a new author to the database.
    Handles both GET and POST requests.
    """
    if request.method == 'POST':
        # Extract data from the form
        name = request.form['name']
        birth_date_str = request.form['birth_date']
        date_of_death_str = request.form['date_of_death']

        # Convert date strings to Python date objects, if provided
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date() if birth_date_str else None
        date_of_death = datetime.strptime(date_of_death_str, '%Y-%m-%d').date() if date_of_death_str else None

        # Create a new Author instance
        new_author = Author(name=name, birth_date=birth_date, date_of_death=date_of_death)

        # Add and commit the new author to the database
        db.session.add(new_author)
        db.session.commit()

        # Flash a success message
        flash('Author added successfully!')

        # Redirect to the same page to clear form data and avoid re-submission
        return redirect(url_for('add_author'))

    # Render the form for adding a new author
    return render_template('add_author.html')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    """
    Route to add a new book to the database.
    Handles both GET and POST requests.
    """
    if request.method == 'POST':
        # Extract data from the form
        isbn = request.form['isbn']
        title = request.form['title']
        publication_year = request.form['publication_year']
        author_id = request.form['author_id']

        # Create a new Book instance
        new_book = Book(isbn=isbn, title=title, publication_year=publication_year, author_id=author_id)

        # Add and commit the new book to the database
        db.session.add(new_book)
        db.session.commit()

        # Flash a success message
        flash('Book added successfully!')

        # Redirect to the same page to clear form data and avoid re-submission
        return redirect(url_for('add_book'))

    # Fetch all authors to populate the author selection in the form
    authors = Author.query.all()

    # Render the form for adding a new book
    return render_template('add_book.html', authors=authors)


@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    author_id = book.author_id
    db.session.delete(book)
    db.session.commit()

    # Check if the author has any other books
    other_books = Book.query.filter_by(author_id=author_id).count()
    if other_books == 0:
        author = Author.query.get(author_id)
        db.session.delete(author)
        db.session.commit()

    flash('Book deleted successfully.', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    # Create all database tables defined in the models
    with app.app_context():
        db.create_all()

    # Run the Flask app on port 5002 with debug mode enabled
    app.run(port=5002, debug=True)
