ML_pl.py

A simple script for identifying Polish words that start with the most common Polish letters.

Most common Polish letters for word beginnings:

    a
    i
    e
    o
    n
    r

Usage:
Python

from ML_pl import MyClass

lst = ['gas', 'oil', 'water', 'chem', 'ala', 'ela']

for item in lst:
    obj = MyClass(item)
    obj.check_and_append(MyClass.letters)
    print(obj)


This script will print a list of words that start with one of the most common Polish letters. For example:

['ala']
['ela']
