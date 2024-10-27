from datetime import datetime

class Contract:
    all = []  

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)  

    @classmethod
    def contracts_by_date(cls, search_date):
        """Returns a list of contracts that match the given date, sorted by the date."""
        search_date_obj = datetime.strptime(search_date, "%d/%m/%Y").date()
        
        matching_contracts = [
            contract for contract in cls.all 
            if datetime.strptime(contract.date, "%d/%m/%Y").date() == search_date_obj
        ]
        
        return matching_contracts

class Author:
    def __init__(self, name):
        self.name = name

    def sign_contract(self, book, date, royalties):
        """Creates a contract for the author and a book."""
        return Contract(self, book, date, royalties)

    def contracts(self):
        """Returns a list of contracts associated with the author."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Returns a list of books associated with the author."""
        return [contract.book for contract in self.contracts()]

    def total_royalties(self):
        """Calculates the total royalties from all contracts."""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        """Returns a list of contracts associated with the book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Returns a list of authors associated with the book."""
        return [contract.author for contract in self.contracts()]
