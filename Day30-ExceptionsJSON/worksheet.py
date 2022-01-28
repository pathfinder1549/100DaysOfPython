# test crash
# try, except, else, finally

try:
    file = open("some_file.txt")
    some_dict = {"key": "value"}
    print(some_dict["other_key"])
except FileNotFoundError:
    file = open("some_file.txt", "w")
    file.write("new file created")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file closed")

# custom exceptions

height = float(input("height: "))
weight = float(input("weight: "))

if height > 3:
    raise ValueError("Height should not be more than 3 meters")

bmi = weight / height ** 2
print(f"BMI: {bmi}")