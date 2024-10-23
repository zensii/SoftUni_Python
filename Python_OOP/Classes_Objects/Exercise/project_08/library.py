from typing import Dict, List
from project_08.user import User


class Library:
    def __init__(self):
        self.user_records: List['User'] = []
        self.books_available: Dict[str, List[str]] = {}
        self.rented_books: Dict[str, Dict[str, int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: 'User'):
        if author in self.books_available:
            if book_name in self.books_available[author]:
                self.books_available[author].remove(book_name)
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {book_name: days_to_return}
                self.rented_books[user.username][book_name] = days_to_return
                user.books.append(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"
            for cur_user in self.rented_books:
                if book_name in self.rented_books[cur_user]:
                    time_to_return = self.rented_books[cur_user][book_name]
                    return (f'The book "{book_name}" is already rented and will be available in'
                            f' {time_to_return} days!')

    def return_book(self, author:str, book_name:str, user: 'User'):
        if user.username in self.rented_books:
            if book_name in self.rented_books[user.username]:
                self.rented_books[user.username].pop(book_name)
                user.books.remove(book_name)
                self.books_available[author].append(book_name)
                return
        return f"{user.username} doesn't have this book in his/her records!"



