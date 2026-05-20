class Logger:
    def Log(self, message):
        print("\033[92m" + message + "\033[0m")

    def Error(self, message):
        print("\033[91m" + message + "\033[0m")

    def Warn(self, message):
        print("\033[93m" + message + "\033[0m")

class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def Write(self, text):
        with open(self.filename, "a") as f:
            f.write(text)

    def WriteLine(self, text):
        with open(self.filename, "a") as f:
            f.write(text + "\n")

class FileLoggerAdapter:
    def __init__(self, file_writer):
        self.file_writer = file_writer

    def Log(self, message):
        self.file_writer.WriteLine("[LOG] " + message)

    def Error(self, message):
        self.file_writer.WriteLine("[ERROR] " + message)

    def Warn(self, message):
        self.file_writer.WriteLine("[WARN] " + message)

if __name__ == "__main__":
    console_logger = Logger()
    console_logger.Log("This is a success message")
    console_logger.Error("This is an error message")
    console_logger.Warn("This is a warning message")

    writer = FileWriter("log.txt")
    file_logger = FileLoggerAdapter(writer)
    file_logger.Log("Saved info to file")
    file_logger.Error("Saved error to file")