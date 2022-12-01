

class Book:
    def __init__(self, index, name, author, bookType, length, dir):
        self.index = index
        self.name = name
        self.author = author
        self.bookType = bookType
        self.length = length
        self.dir = dir
    def getIndex(self):
        return self.index
    def getName(self):
        return self.name
    def getAuthor(self):
        return self.author
    def getBookType(self):
        return self.bookType
    def getLength(self):
        return self.length
    def getDir(self):
        return self.dir
    def getFull(self):
        return f"{self.index}-{self.name}-{self.author}-{self.bookType}-{self.length}-{self.dir}"

class BookManager:
    def __init__(self):
        self.books = []
        # Last line of file must be a line break
        filename = "./DataIndex/DataIndex.txt"
        # Index of book, start from 1
        tt = 0

        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file:
                agrs = line.split(' - ')
                tt = tt + 1
                # Tên sản phẩm - tác giả - thể loại - thời lượng - đường dẫn tới speech file
                index = tt
                name = agrs[0]
                author = agrs[1]
                bookType = agrs[2]
                length = agrs[3]
                dir = agrs[4][:-1]
                book = Book(index, name, author, bookType, length, dir)
                self.addBook(book)
    def addBook(self, book):
        self.books.append(book)
    def deleteBook(self, list_book):
        if (type(list_book) == Book):
            if list_book in self.books:
                self.books.remove(list_book)
                return
        for book in list_book:
            if book in self.books:
                self.books.remove(book)
    def getListOfBook(self):
        for book in self.books:
            print(book.getFull())
    def searchByIndex(self, index):
        return self.books[index-1]
    def searchByName(self, name):
        # name_decode = unidecode.unidecode(name)
        list_book = []
        for x in self.books:
            if (x.name == name):
                list_book.append(x)
        return list_book
    def searchByAuthor(self, author):
        # author_decode = unidecode.unidecode(author)
        list_book = []
        for x in self.books:
            if (x.author == author):
                list_book.append(x)
        return list_book
    def searchByNameAndAuthor(self, name, author):
        list_book = []
        list_book_by_name = self.searchByName(name)
        for x in list_book_by_name:
            if (x.author == author):
                list_book.append(x)
        return list_book
    