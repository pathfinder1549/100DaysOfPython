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

