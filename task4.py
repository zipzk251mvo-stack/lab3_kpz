import re


class TextReader:
    def read_text_file(self, filename):
        pass


class SmartTextReader(TextReader):
    def read_text_file(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        result = []
        for line in lines:
            result.append(list(line.replace("\n", "")))
        return result


class SmartTextChecker(TextReader):
    def __init__(self, reader):
        self.reader = reader

    def read_text_file(self, filename):
        print("Logging: Opening file " + filename)
        try:
            matrix = self.reader.read_text_file(filename)
            print("Logging: File " + filename + " read successfully")

            total_lines = len(matrix)
            total_chars = sum(len(line) for line in matrix)
            print("Logging: Total lines: " + str(total_lines) + ", Total characters: " + str(total_chars))

            return matrix
        finally:
            print("Logging: Closing file " + filename)


class SmartTextReaderLocker(TextReader):
    def __init__(self, reader, pattern):
        self.reader = reader
        self.pattern = pattern

    def read_text_file(self, filename):
        if re.search(self.pattern, filename):
            print("Access denied!")
            return None
        return self.reader.read_text_file(filename)


if __name__ == "__main__":
    with open("public_data.txt", "w") as f:
        f.write("Hello World\nLine Number Two")

    with open("secret_data.txt", "w") as f:
        f.write("Top Secret Content")

    base_reader = SmartTextReader()

    print("--- Testing Checker Proxy ---")
    checker_proxy = SmartTextChecker(base_reader)
    data = checker_proxy.read_text_file("public_data.txt")
    print("Result matrix:", data)

    print("\n--- Testing Locker Proxy ---")
    locker_proxy = SmartTextReaderLocker(base_reader, r"secret")

    print("Trying to read public file:")
    locker_proxy.read_text_file("public_data.txt")

    print("Trying to read secret file:")
    locker_proxy.read_text_file("secret_data.txt")