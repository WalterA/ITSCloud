from Lezione8.Library_Management_System import Book, Member, Library
import unittest

class TestLibrary(unittest.TestCase):
    def setUp(self):
        # Create instances of books
        self.book1 = Book.from_string("1984, George Orwell, 9780451524935")
        self.book2 = Book.from_string("Il Signore degli Anelli, J.R.R. Tolkien, 9780618640157")
        self.book3 = Book.from_string("Il Piccolo Principe, Antoine de Saint-Exupéry, 9780156013987")

        # Create instances of members
        self.member1 = Member.from_string("Mario Rossi, M001")
        self.member2 = Member.from_string("Luigi Bianchi, M002")

        # Create a library
        self.library = Library()

    def test_add_book(self):
        # Add books to the library
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

        # Assert that the books are added successfully
        self.assertEqual(self.library.total_books, 2)
        self.assertIn(self.book1, self.library.books)
        self.assertIn(self.book2, self.library.books)

    def test_register_member(self):
        # Register members to the library
        self.library.register_member(self.member1)
        self.library.register_member(self.member2)

        # Assert that the members are registered successfully
        self.assertEqual(len(self.library.members), 2)
        self.assertIn(self.member1, self.library.members)
        self.assertIn(self.member2, self.library.members)

    def test_lend_book(self):
        # Add books to the library
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

        # Register members to the library
        self.library.register_member(self.member1)
        self.library.register_member(self.member2)

        # Lend books to members
        self.library.lend_book(self.book1, self.member1)
        self.library.lend_book(self.book2, self.member2)

        # Assert that the books are lent successfully
        self.assertIn(self.book1, self.member1.borrowed_book)
        self.assertIn(self.book2, self.member2.borrowed_book)

    def test_return_book(self):
        # Add books to the library
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

        # Register members to the library
        self.library.register_member(self.member1)
        self.library.register_member(self.member2)

        # Lend books to members
        self.library.lend_book(self.book1, self.member1)
        self.library.lend_book(self.book2, self.member2)

        # Return books to the library
        self.library.member1.return_book(self.book1)
        self.library.member2.return_book(self.book2)

        # Assert that the books are returned successfully
        self.assertNotIn(self.book1, self.member1.borrowed_book)
        self.assertNotIn(self.book2, self.member2.borrowed_book)


if __name__ == '__main__':
    unittest.main()
