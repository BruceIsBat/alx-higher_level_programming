import json
import doctest

def save_to_json_file(my_obj, filename):
    """
    Serialize an object and save it as a JSON representation in a text file.

    Args:
        my_obj: The object to be serialized and saved.
        filename (str): The name of the file to which the JSON representation
                        of the object will be saved.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

if __name__ == "__main__":
    doctest.testfile('5-save_to_json_file.txt')
