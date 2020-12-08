# -*- coding: utf-8 -*-
"""
Created on on Tue Nov 25 12:05:03 2020


@author: DIVYA
"""
from BookItem import BookItem

class Book:
        
    def __init__(self, title, author, category, publication_date):
        self.title = title
        self.author = author
        self.category = category
        self.publication_date = publication_date
        self.total_count = 0
        self.book_item = []
        
    def addBookItem(self, isbn, rack):
        b = BookItem(self, isbn, rack)
        self.book_item.append(b)
        self.total_count +=1
        
    def printBook(self):
        print ("{} by {}".format(self.title, self.author))
        for book_item in self.book_item:
            print ("Isbn: {}, Rack: {}".format(book_item.isbn, book_item.rack))
            
    def viewReservedBookItems():
        if len(BookItem.reserved_book_items) >= 1:
            for item in BookItem.reserved_book_items:
                print(item.isbn)
        else:
            print("No books are reserved at the moment!")
            
    def viewIssuerInfo(isbn):
        for book_item in BookItem.reserved_book_items:
            if book_item.isbn == isbn:
                print("Issued by: " + book_item.info["Name"])
                print("Student ID: " + book_item.info["Student ID"])
                print("Issued for: " + str(book_item.info["Days"]) + " days")
                
    def updateIssuerInfo(book_item, name, student_id, days):
        BookItem.updateIssuerInfo(book_item, name, student_id, days)
        
    def addToReservedList(book_item):   
        BookItem.addToReservedList(book_item)
        
    def clearIssuerInfo(ret_book_item):
        BookItem.clearIssuerInfo(ret_book_item)
        
    def removeFromReservedList(ret_book_item):
        BookItem.removeFromReservedList(ret_book_item)
        
    def extendDates(book_item, ext_days):
        BookItem.extendDates(book_item, ext_days)