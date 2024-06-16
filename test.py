import pytest

from main import BooksCollector


# проверяем добавление новой книги
def test_add_new_book_added_correctly():
    books_collector = BooksCollector()
    books_collector.add_new_book('Мастер и Маргарита')
    assert 'Мастер и Маргарита' in books_collector.books_genre

# проверяем установку жанра книге
def test_set_book_genre_added_correctly():
    books_collector = BooksCollector()
    books_collector.add_new_book('Приключения рождественского пудинга')
    books_collector.set_book_genre('Приключения рождественского пудинга', 'Детективы')
    assert books_collector.books_genre['Приключения рождественского пудинга'] == 'Детективы'

# проверяем получение жанра книги по её имени
def test_get_book_genre_correctly():
    books_collector = BooksCollector()
    books_collector.add_new_book('Рождество на Ганимеде')
    books_collector.set_book_genre('Рождество на Ганимеде', 'Фантастика')
    assert books_collector.get_book_genre('Рождество на Ганимеде') == 'Фантастика'

# проверяем вывод списка книг с определённым жанром
@pytest.mark.parametrize('name, genre', [
    ('Рождество на Ганимеде', 'Фантастика'),
    ('Рождество без Родни', 'Фантастика'), ])
def test_get_books_with_specific_genre_correctly(name, genre):
    books_collector = BooksCollector()
    books_collector.add_new_book(name)
    books_collector.set_book_genre(name, genre)
    books_collector.add_new_book(name)
    books_collector.set_book_genre(name, genre)
    assert name in books_collector.get_books_with_specific_genre(genre)

# проверяем получение словаря books_genre
@pytest.mark.parametrize('name, genre', [
    ('Рождество на Ганимеде', 'Фантастика'),
    ('Рождество без Родни', 'Фантастика'), ('Приключения рождественского пудинга', 'Детективы') ])
def test_get_books_genre_correctly(name, genre):
    books_collector = BooksCollector()
    books_collector.add_new_book(name)
    books_collector.set_book_genre(name, genre)
    assert books_collector.get_books_genre()[name] == genre

# проверяем возвращение книги, подходящие детям
def test_get_books_for_children_returns_correctly():
    books_collector = BooksCollector()
    books_collector.add_new_book('Винни-Пух')
    books_collector.set_book_genre('Винни-Пух', 'Мультфильмы')
    assert 'Винни-Пух' in books_collector.get_books_for_children()

# проверяем добавление книги в Избранное
def test_add_book_in_favorites_added_correctly():
    books_collector = BooksCollector()
    books_collector.add_new_book('Винни-Пух')
    books_collector.set_book_genre('Винни-Пух', 'Мультфильмы')
    books_collector.add_book_in_favorites('Винни-Пух')
    assert 'Винни-Пух' in books_collector.favorites

# проверяем удаление книги из Избранного
def test_delete_book_from_favorites_deleted_correctly():
    books_collector = BooksCollector()
    books_collector.add_new_book('Винни-Пух')
    books_collector.set_book_genre('Винни-Пух', 'Мультфильмы')
    books_collector.add_book_in_favorites('Винни-Пух')
    books_collector.delete_book_from_favorites('Винни-Пух')
    assert 'Винни-Пух' not in books_collector.favorites

# проверяем получение списка Избранных книг
@pytest.mark.parametrize('name, genre', [
    ('Рождество на Ганимеде', 'Фантастика'),
    ('Рождество без Родни', 'Фантастика'), ('Приключения рождественского пудинга', 'Детективы') ])
def test_get_list_of_favorites_books_added_corretly(name, genre):
    books_collector = BooksCollector()
    books_collector.add_new_book(name)
    books_collector.set_book_genre(name, genre)
    books_collector.add_book_in_favorites(name)
    assert name in books_collector.get_list_of_favorites_books()

