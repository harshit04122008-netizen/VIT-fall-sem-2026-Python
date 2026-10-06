n = int(input())
short_books = []
medium_books = []
long_books = []
for i in range(n):
    book = input()
    no_pages = int(input())
    if no_pages < 100:
        term = book, no_pages
        short_books.append(term)
    elif no_pages >= 100 and no_pages <= 300:
        term = book, no_pages
        medium_books.append(term)
    else:
        term = book, no_pages
        long_books.append(term)
short_books.sort(key = lambda x: x[1])
medium_books.sort(key = lambda x: x[1])
long_books.sort(key = lambda x: x[1])
if len(short_books) != 0:
    print("Short Read Books:")
    for i in range(len(short_books)):
        print(short_books[i][0],"-",short_books[i][1],"pages")
if len(medium_books) != 0:
    print("Medium Read Books:")
    for i in range(len(medium_books)):
        print(medium_books[i][0],"-",medium_books[i][1], "pages")
if len(long_books) != 0:
    print("Long Read Books:")
    for i in range(len(long_books)):
        print(long_books[i][0],"-",long_books[i][1],"pages")