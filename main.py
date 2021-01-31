import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
book = pd.read_csv("GoodreadsBooks.csv", error_bad_lines=False)

print(book.isnull().sum())
print(book.dtypes)
books = book.drop(columns=['bookID', 'isbn', 'isbn13', 'publisher'], axis=1)
print(books.head())
print(books.shape)

missing_values_count = books.isnull().sum()
print(missing_values_count)

drop_duplicates = books.drop_duplicates()
print(books.shape,drop_duplicates.shape)

books.replace(to_replace='J.K. Rowling/Mary GrandPré', value='J.K. Rowling', inplace=True)

total_cells = np.product(books.shape)
total_missing = (missing_values_count.sum())
percent_missing = (total_missing/total_cells)
print(percent_missing)

most_common_authors = books['authors'].value_counts()[:40]
print(most_common_authors)
print(most_common_authors['John Grisham'])

top_books = books[books['ratings_count'] > 100000]
top_20 = top_books.sort_values('average_rating', ascending=False).head(20)
print(top_20)

most_rated = top_books.sort_values('ratings_count', ascending=False).head(20)
print(most_rated)

top_5 = top_20.iloc[[0,1,2,3,4],[0,1,2]]
print(top_5)