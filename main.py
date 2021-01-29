import pandas as pd
import numpy as np
book = pd.read_csv("GoodreadsBooks.csv", error_bad_lines=False)

print(book.isnull().sum())

print(book.dtypes)

books = book.drop(columns=['isbn', 'isbn13', 'publication_date', 'publisher'], axis=1)

print(books.describe())

books.replace(to_replace='J.K. Rowling/Mary GrandPré', value='J.K. Rowling', inplace=True)

print(books.isnull().sum())

top_rated = books.sort_values('average_rating', ascending=False)

print(top_rated)
