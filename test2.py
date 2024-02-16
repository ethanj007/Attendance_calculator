import streamlit as st
import math

# ADDED A SIMPLE CALCULATION IN COMMAND LINE INTERFACE
attendance = float(input("Enter the minimum attendance percentage:"))
total = int(input("enter total number of classes"))
current_classes = int(input("enter the number of classes completed till date"))
current_attendance = float(input("enter ur current attendance percentage"))
a = math.floor(current_attendance)
b = int((a/100)*current_classes)
user_classes = math.floor(int(current_classes) -((a/100)*current_classes)) # number of classes user has bunked till date  5
minimum_classes = total - int((attendance/100)*total) #minimum number of classes user has to attend to maintain minimum attendance 10
final =float(((total - minimum_classes) / total) * 100)

while True:
    final = float(((total - minimum_classes) / total) * 100)

    if final >= attendance:
        break

    else:
        minimum_classes = minimum_classes - 1

print(final)
print(minimum_classes)

print(user_classes)


if user_classes < minimum_classes:
    a = minimum_classes-user_classes
    print(f"u can only bunk {a} classes")

if user_classes == minimum_classes:
    print(f"you have to attend all classes to maintain {attendance}%")

if user_classes > minimum_classes:
    print(f"you cannot maintain {attendance}%")


