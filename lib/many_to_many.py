class Author:
    all=[]
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception('Name must be a string')
        self.name=name
        # Keeps track of all authors with a class variable 
        Author.all.append(self)
        
    def contracts(self):
        #  Returns a list of contracts related to the author.
        return[contract for contract in Contract.all if contract.author==self]
    def books(self):
        #  Returns a list of books related to the author through contracts.
        return [contract.book for contract in self.contracts()]
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])

class Book:
    all=[]
    def __init__(self, title):
        self.title=title
        Book.all.append(self)
    def authors(self):
        return([contract.author for contract in self.contracts()])
    def contracts(self):
        return[contract for contract in Contract.all if contract.book==self]

class Contract:
    all=[]
    def __init__(self, author, book, date, royalties):
        self.author=author
        self.book=book
        self.date=date
        self.royalties=royalties
        Contract.all.append(self)
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception('Author must be an instance of Author class')
        self._author=value
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception('Date must be a string')
        self._date=value
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception('Royalties must be a number')
        self._royalties=value

    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception('book must be an instance of Book class')
        self._book=value

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date==date]