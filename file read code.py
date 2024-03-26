import shutil
class FileUtility:
    @staticmethod
    def read_text_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print("File not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def write_text_file(file_path, content):
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            print("Write operation successful.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def copy_file(source_path, destination_path):
        try:
            shutil.copyfile(source_path, destination_path)
            print("Copy operation successful.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


content = FileUtility.read_text_file("example.txt")
print("Content read from file:")
print(content)
content_to_write = "Hello, World!\nThis is a test file."
FileUtility.write_text_file("example_output.txt", content_to_write)
FileUtility.copy_file("example.txt", "example_copy.txt")
