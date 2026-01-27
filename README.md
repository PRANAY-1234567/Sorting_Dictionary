📊 Sort a Dictionary by Value in Python
📌 Description

This program sorts a dictionary based on its values in ascending order.
It is a common Python interview and practice problem that helps you understand dictionaries, sorting, and lambda functions.

🧩 Problem Statement

Given a dictionary:

{"A": 50, "B": 90, "C": 70}


Sort the dictionary by its values.

✅ Code
data = {"A": 50, "B": 90, "C": 70}

sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))

print(sorted_data)

🧠 Explanation

data.items() converts the dictionary into key-value pairs

sorted() sorts these pairs

key=lambda x: x[1] tells Python to sort using the value

dict() converts the sorted pairs back into a dictionary

The result is a dictionary sorted by values

🖨 Example Output
{'A': 50, 'C': 70, 'B': 90}

🛠 Concepts Used

Dictionaries

sorted() function

Lambda functions

Key-value pairs

🎯 Use Cases

Interview preparation

Ranking and scoring systems

Data analysis basics

Dictionary manipulation

🚀 Possible Improvements

Sort in descending order

Sort by keys instead of values

Convert into a function

Handle large datasets

👨‍💻 Author

Pranay Jadhao
