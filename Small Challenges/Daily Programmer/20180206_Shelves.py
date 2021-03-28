if __name__ == "__main__":
    inStr = "x"
    shelves = [int(shelf) for shelf in input().split()]
    books = []
    while len(inStr.strip()) != 0:
        inStr = raw_input();
        books.append(inStr.split(' ', 1))

    books.pop()
    books = [(int(book[0]), book[1]) for book in books]
    books = sorted(books, key = lambda book: book[0])
    shelves = sorted(shelves)

    # Check impossible situations
    if books[-1][0] > shelves[-1] or sum([b[0] for b in books])>sum(shelves):
        books = []

    # Main loop: add books to minimise wasted space greedily
    # Not necessarily complete
    counter = 0
    while len(books) > 0:
        # Fit as many other books onto biggest shelf as possible
        biggestBook = -1
        while biggestBook >= (-1 * len(books)):
            if books[biggestBook][0] <= shelves[-1]:
                nextBook = books.pop(biggestBook)
                biggestBook = -1
                shelves[-1] -= nextBook[0]
            else:
                biggestBook -= 1
        else: # Remove shelf and increment counter
            shelves.pop()
            counter += 1
        # End loop

print(str(counter) if counter > 0 else "impossible")
