class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Returns a list of contracts related to this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Returns a list of authors related to this book through contracts."""
        return [contract.author for contract in self.contracts()]

    def __repr__(self):
        return f"Book(title={self.title})"


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.name = name
        self._contracts = []  # Store contracts related to this author
        Author.all.append(self)

    def contracts(self):
        """Returns a list of contracts related to the author."""
        return self._contracts

    def books(self):
        """Returns a list of books related to the author through contracts."""
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        """Creates a new contract for this author with the specified book."""
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        """Returns the total royalties earned by the author."""
        return sum([contract.royalties for contract in self._contracts])


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        
        # Add contract to the author's contracts list
        author._contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Returns all contracts signed on the given date."""
        return [contract for contract in cls.all if contract.date == date]

    def __repr__(self):
        return f"Contract(author={self.author.name}, book={self.book.title}, date={self.date}, royalties={self.royalties})"
