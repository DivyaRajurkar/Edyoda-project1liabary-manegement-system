# -*- coding: utf-8 -*-
"""
Created on on Tue Nov 25 12:05:03 2020


@author: DIVYA
"""
from Catalog import Catalog
from Billing import Billing

class BookReserveReturn:
    
    def reserveBook(name, student_id, book_title, days):
        for book in Catalog.books_list:
            if book.title == book_title and len(book.book_item) != 0:
                book_item = book.book_item.pop()
                book.total_count -= 1
                Catalog.updateIssuerInfo(book_item, name, student_id, days)
                Catalog.addToReservedList(book_item)
                return book_item
        else:
            print("The book you're trying to reserve is unavailable.")
    
    def returnBook(ret_book_item, days):
        for book in Catalog.books_list:
            if book == ret_book_item.book:
                book.book_item.append(ret_book_item)
                book.total_count += 1
        Catalog.clearIssuerInfo(ret_book_item)
        Catalog.removeFromReservedList(ret_book_item)
        Billing.calcBill(days)
        
    def extendDates(book_item, ext_days):
        Catalog.extendDates(book_item, ext_days)
