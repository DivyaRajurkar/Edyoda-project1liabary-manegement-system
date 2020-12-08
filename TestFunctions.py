# -*- coding: utf-8 -*-
"""
Created on on Tue Nov 25 12:05:03 2020


@author: DIVYA
"""
from User import Member
from User import Librarian

lib = Librarian("John Doe", "Mumbai", 30, "AJSK8549", "EMP58964")
print(lib)
lib.addBook('Shoe Dog','Phil Knight', "Biography", '2015')
lib.addBookItem("Shoe Dog", "123pk", "H1B1")
lib.addBookItem("Shoe Dog", "124pk", "H1B2")
lib.addBook('Kafka On The Shore','Haruki Murakami', "Fiction", "2002")
lib.addBookItem("Kafka On The Shore", "854hm", "C1B1")
lib.addBookItem("Kafka On The Shore", "685hm", "C1B2")
lib.addBook('The Fault In Our Stars','John Green', "Romance", "2012")
lib.addBookItem("The Fault In Our Stars", "957jg", "R1B1")
lib.addBookItem("The Fault In Our Stars", "985jg", "R1B2")
lib.viewBooks()
lib.removeBookItem("985jg")
lib.viewBooks()
lib.removeBook("The Fault In Our Stars")
lib.viewBooks()

member1 = Member("Niel", "Mumbai", 23, "ABCD4321", "STUD4321")
member2 = Member("Nitin", "Mumbai", 23, "DCBA4321", "STUD8765")
print(member2)
member1.viewBooks()
member1.searchByTitle("Kafka On The Shore")
member1.searchByTitle("Rich Dad Poor Dad")
member1.searchByAuthor("Phil Knight")
member1.searchByAuthor("Robert Kiyosaki")
member1.searchByCategory("Fiction")
member1.searchByCategory("Self Help")
member1.searchByPublicationDate("2015")
member1.searchByPublicationDate("2013")
member1.reserveBook("Shoe Dog")
member2.reserveBook("Kafka On The Shore")
member1.viewBooks()

lib.viewReservedBookItems()
lib.viewIssuerInfo()

member1.returnBook()
member2.returnBook()
member1.viewBooks()

member2.reserveBook("Kafka On The Shore")
member2.extendDates()


lib.addMember("Mukesh", "Mumbai", "23", "PQRS6789", "STUD6789")
lib.viewMembers()
lib.searchMember("Mukesh")
lib.removeMember("Niel")
member1.reserveBook("Kafka On The Shore")
