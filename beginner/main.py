    # main.py
    # This assumes utility.py is in the same directory or on the Python path.
import utility

    # Using a function from utility.py
message = utility.greet("Alice")
print(message)

    # Using a class from utility.py
obj = utility.MyClass(10)
print(f"Doubled value: {obj.get_value()}")