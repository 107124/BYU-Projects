"""
File: L12_Team_Activity
Authors: Kent Taylor, Jose Carlitos, Jacob Buffington, Hyrum Leishman, KC Williamson

Purpose: Find items in a file.
"""
largest = ""
book_of_mormon = []
largest_value = []

volume = input("Which volume of scriptures would you like to learn about? ")
with open("books_and_chapters.txt") as books_and_chapters:
  # books_and_chapters = books_and_chapters.strip()


  for book_entry in books_and_chapters:
    book_entry = book_entry.strip()
    book_entry = book_entry.split(":")

    book = book_entry[0]
    chapters = int(book_entry[1])
    scripture = book_entry[2]


    if scripture.lower() == volume.lower():
      if largest == "":
        largest = chapters
        largest_value = book_entry

      if chapters > largest:
        largest = chapters
        largest_value = book_entry

    if scripture.lower() == "book of mormon":
      book_of_mormon.append(book_entry)




    # for i in book:
    #   print(i)
    # print(f"Scripture: {book[2]}, Books: {book[0]}, Chapters: {book[1]}")
print(largest, largest_value[0])


# for books in book_of_mormon:
#   print(f"{books[0]}")
# for i in range(len(book_of_mormon)):
#   print(book_of_mormon[i][0])
