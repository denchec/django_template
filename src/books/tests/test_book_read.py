import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def author(mixer):
    return mixer.blend("books.Author", name="J. K. Rowling")


@pytest.fixture
def book(mixer, author):
    return mixer.blend("books.Book", name="Harry Potter", author=author)


def test_book_read(api, book, author):
    result = api.get("/api/v1/books/")

    assert result[0]["id"] == book.id
    assert result[0]["name"] == "Harry Potter"
    assert result[0]["author"]["id"] == author.id
    assert result[0]["author"]["name"] == "J. K. Rowling"
