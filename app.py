from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
books = {
    'fiction': [
        {'id': 1, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'description': 'A novel about racial injustice.'},
        {'id': 2, 'title': '1984', 'author': 'George Orwell', 'description': 'A dystopian novel about totalitarianism.'},
    ],
    'nonfiction': [
        {'id': 3, 'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'description': 'A brief history of humankind.'},
        {'id': 4, 'title': 'Educated', 'author': 'Tara Westover', 'description': 'A memoir about growing up in a strict and abusive household in rural Idaho.'},
    ],
    'mystery': [
        {'id': 5, 'title': 'Gone Girl', 'author': 'Gillian Flynn', 'description': 'A thriller about a woman who disappears on her wedding anniversary.'},
        {'id': 6, 'title': 'The Girl with the Dragon Tattoo', 'author': 'Stieg Larsson', 'description': 'A mystery involving a journalist and a hacker.'},
    ]
}

favorites = []

@app.route('/')
def home():
    genre_list = books.keys()
    return render_template('genres.html', genres=genre_list,  is_home=True)

@app.route('/genres')
def genres():
    genre_list = books.keys()
    return render_template('genres.html', genres=genre_list,  is_home=False)

@app.route('/recommendations/<genre>')
def recommendations(genre):
    if genre in books:
        genre_books = books[genre]
        return render_template('recommendations.html', genre=genre, books=genre_books)
    else:
        return "Genre not found.", 404

@app.route('/book/<int:book_id>')
def book_details(book_id):
    for genre in books.values():
        for book in genre:
            if book['id'] == book_id:
                return render_template('book_details.html', book=book)
    return "Book not found.", 404

@app.route('/favorites', methods=['GET', 'POST'])
def favorite_books():
    if request.method == 'POST':
        book_id = request.form.get('book_id')
        for genre in books.values():
            for book in genre:
                if book['id'] == int(book_id):
                    favorites.append(book)
                    return redirect(url_for('favorite_books'))
    return render_template('favorites.html', favorites=favorites)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
