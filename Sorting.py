data = {"A": 70, "B": 90, "C": 50}

sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))

print(sorted_data)
