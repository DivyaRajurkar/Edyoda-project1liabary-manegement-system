# -*- coding: utf-8 -*-
"""
Created on on Tue Nov 25 12:05:03 2020


@author: DIVYA
"""from BookReserveReturn import BookReserveReturn
from Catalog import Catalog

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        
    def viewBooks(self):
        Catalog.displayAllBooks()
        
class Librarian(User):
    def __init__(self, name, location, age, aadhar_id, employee_id):
        super().__init__(name, location, age, aadhar_id)
        self.employee_id = employee_id
        
    def __repr__(self):
        return self.name + " " + self.location + " " + self.employee_id
    
    def addBook(self, title, author, category, publication_date):
        Catalog.addBook(title, author, category, publication_date)
        
    def addBookItem(self, title, isbn, rack):
        Catalog.addBookItem(title, isbn, rack)
    
    def removeBook(self, rem_book):
        Catalog.removeBook(rem_book)
        
    def removeBookItem(self, rem_bookitem):
        Catalog.removeBookItem(rem_bookitem)
        
    def addMember(self, name, location, age, aadhar_id, student_id):
        Member(name, location, age, aadhar_id, student_id)
    
    def removeMember(self, name):
        for member in Member.members_list:
            if member.name == name:
                Member.members_list.remove(member)
                print("{} was successfully removed from the library!".format(name))
                break
        else:
            print("No member exists by this name")
            
    def viewMembers(self):
        for member in Member.members_list:
            print(member)
        
    def searchMember(self, name):
        for member in Member.members_list:
            if member.name == name:
                print(member)
                for book_item in member.issued_books_list:
                    print(book_item.book.title, book_item.isbn)
                break
        else:
            print("There are no registered members in this library by this name.")
            
    def viewReservedBookItems(self):
        Catalog.viewReservedBookItems()
        
    def viewIssuerInfo(self):
        isbn = input("Please enter isbn of the book for which you'd like to view issuer information for: ")
        Catalog.viewIssuerInfo(isbn)
    
class Member(User):
    members_list = []
    
    @classmethod
    def addMemberList(cls, member):
        cls.members_list.append(member)
    
    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issued_books_list = []
        Member.addMemberList(self)
        print("Welcome to Honest Members Library {}!".format(name))
        
    def __repr__(self):
        return self.name + " " + self.location + " " + self.student_id
        
    def searchByTitle(self, title):
        Catalog.searchByTitle(title)
    
    def searchByAuthor(self, author):
        Catalog.searchByAuthor(author)
        
    def searchByCategory(self, category):
        Catalog.searchByCategory(category)
    
    def searchByPublicationDate(self, publication_date):
        Catalog.searchByPublicationDate(publication_date)
    
    def reserveBook(self, book_title):
        days = 0
        max_days = 10
        condition1 = [False, "Sorry.. your membership has been revoked.\nContact librarian for further details."]
        for member in Member.members_list:
            if member == self:
                condition1[0] = True
                days = int(input("For how many days would you like to issue this book? "))
                
        condition2 = [False, "Sorry! You can issue a book for a maximum of {} days".format(max_days)]
        if days <= max_days:
            condition2[0] = True
            
        condition3 = [False, "You can issue a maximum of 5 books at a time"]
        if len(member.issued_books_list) < 5:
            condition3[0] = True
        
        conditions = [condition1, condition2, condition3]
        
        for condition in conditions:
            if condition[0] == False:
                print(condition[1])
                break
        else:
            book_item = BookReserveReturn.reserveBook(self.name, self.student_id, book_title, days)
            self.issued_books_list.append(book_item)
            print("Book reserved successfully!")
            print("Grab your copy {} from rack {}".format(book_item.isbn, book_item.rack))
        
    def returnBook(self):
        print("BOOKS CURRENTLY ISSUED BY YOU: ")
        for book_item in self.issued_books_list:
            print(book_item.book.title, book_item.isbn)
        isbn = input("Which book would you like to return? Enter isbn: ")
        days = int(input("How many days has it been since you issued this book? Be honest! "))
        for book_item in self.issued_books_list:
            if book_item.isbn == isbn:
                ret_book_item = book_item
            else:
                print("Sorry.. the book you're trying to return is not issued by you!")
        BookReserveReturn.returnBook(ret_book_item, days)
        self.issued_books_list.remove(ret_book_item)
        
    def extendDates(self):
        print("BOOKS CURRENTLY ISSUED BY YOU: ")
        for book_item in self.issued_books_list:
            print(book_item.isbn)
        isbn = input("Please enter isbn of the book for which you'd like to extend dates: ")
        ext_days = int(input("Please enter the number of days you'd like to extend for: "))
        for book_item in self.issued_books_list:
            if book_item.isbn == isbn:
                BookReserveReturn.extendDates(book_item, ext_days)