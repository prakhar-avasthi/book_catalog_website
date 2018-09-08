from app import db
from app.catalog import main
from app.catalog.forms import EditBookForm, AddBookForm
from app.catalog.models import Book, Publication
from flask import render_template, flash, redirect, request, url_for
from flask_login import login_required


@main.route('/display')
@login_required
def display_books():
    books = Book.query.all()
    return render_template('home.html', books=books)


@main.route('/display/publisher/<publisher_id>')
@login_required
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id=publisher.id).all()

    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)


@main.route('/book/delete/<book_id>', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash('Book deleted successfully')
        return redirect(url_for("main.display_books"))

    return render_template('delete_book.html', book=book, book_id=book_id)


@main.route('/book/edit/<book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get(book_id)
    form = EditBookForm(obj=book)

    if form.validate_on_submit():
        book.title = form.title.data
        book.format = form.format.data
        book.num_pages = int(form.num_pages.data)
        db.session.add(book)
        db.session.commit()
        flash('Book edited successfully')
        return redirect(url_for("main.display_books"))

    return render_template('edit_book.html', form=form)


@main.route('/book/add/<pub_id>', methods=['GET', 'POST'])
@login_required
def add_book(pub_id):
    form = AddBookForm()
    form.pub_id.data = pub_id

    if form.validate_on_submit():
        book = Book(title=form.title.data,
                    author=form.author.data,
                    rating=form.avg_rating.data,
                    format=form.format.data,
                    image=form.image.data,
                    pages=form.num_pages.data,
                    pub_id=form.pub_id.data,)
        db.session.add(book)
        db.session.commit()
        flash('Book added successfully')
        return redirect(url_for("main.display_publisher", publisher_id=pub_id))

    return render_template('add_book.html', form=form)