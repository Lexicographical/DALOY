import os

inside = os.path.abspath(os.path.join(os.path.join(os.path.abspath(__file__), os.pardir), "daloy/test.txt"))

print(inside)