library = []
num_of_books = int(input("no. of books = "))
for i in range(num_of_books):
    book = {
        "title": input("title = "),
        "author": input("author = "),
        "year": input("year = ")
    }
    library.append(book)
print(library)
