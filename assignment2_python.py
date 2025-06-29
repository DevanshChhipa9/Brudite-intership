
#*task-1
'''Turn the following snippet into a function:
numbers = [1,2,3,4,5]
 squares = []
 for n in numbers:
    squares.append(n*n)
 print(squares)
 Requirements:
 Create def compute_squares(nums: list[int]) -> list[int]
 Add a docstring and type hints
 Call it on at least two different lists'''

#?def compute_squares(nums: list[int]) -> list[int]:

  #?  squares = []
    #?for n in nums:
      #?  squares.append(n * n)
    #?return squares

#? print(compute_squares([1, 2, 3, 4, 5]))   
#? print(compute_squares([10, 20, 30])) 


#*task2
"""
Write a function that reads a text file and returns its
 lines.
 
 Use with open(...) as f:
 Catch and handle FileNotFoundError with a user-friendly message.
 From main(), prompt user for file name, call read_lines, then print line
 count"""

#! def read_lines(filename):
#!    try:
#!         with open(filename, 'r') as f:
#!           return f.readlines()
#!    except FileNotFoundError:
#!        print("File not found. Please check the name.")
#!        return []

#!def main():
#!   name = input("Enter file name: ")
#!   lines = read_lines(name)
#!print("Total lines:", len(lines))

#!main()

#* task3 

import os

file = "scores.csv"

def loadScores():
    data = []
    if os.path.exists(file):
        with open(file, 'r') as f:
            for line in f:
                if ',' in line:
                    name, score = line.strip().split(',')
                    if score.isdigit():
                        data.append((name, int(score)))
    return data

def saveScores(data):
    with open(file, 'w') as f:
        for name, score in data:
            f.write(f"{name},{score}\n")

def showTop(data):
    try:
        n = int(input("How many top scores? "))
        top = sorted(data, key=lambda x: x[1], reverse=True)[:n]
        print("\nTop Scores:")
        for name, score in top:
            print(f"{name}: {score}")
    except:
        print("Please enter a valid number.")

def addScore(data):
    name = input("Enter name: ")
    try:
        score = int(input("Enter score: "))
        data.append((name, score))
        saveScores(data)
        print("Score added.")
    except:
        print("Score must be a number.")

def menu():
    data = loadScores()
    while True:
        print("\n1. Show Top Scores\n2. Add Score\n3. Exit")
        choice = input("Choose (1-3): ")
        if choice == '1':
            showTop(data)
        elif choice == '2':
            addScore(data)
        elif choice == '3':
            print("Bye!")
            break
        else:
            print("Invalid choice.")

menu()
