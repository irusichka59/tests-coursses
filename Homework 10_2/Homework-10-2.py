class Reader:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.data = None

    def read_file(self):
        with open(self.__file_path, 'r') as f:
            self.data = f.read()


class Writer:
    def __init__(self, file_path):
        self.__file_path = file_path

    def write_to_file(self, data):
        with open(self.__file_path, 'a') as f:
            f.write(data + '\n')


class ProxyReaderWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = Reader(file_path)
        self.writer = Writer(file_path)
        self.data = None
        self.previous_row = None

    def read(self):
        if self.data is None:  # Зчитувати файл лише якщо даних немає
            self.reader.read_file()
            self.data = self.reader.data

    def write(self, row):
        if row != self.previous_row:  # Перевіряємо, чи поточний рядок не дорівнює попередньому
            self.writer.write_to_file(row)
            self.previous_row = row


proxy_rw = ProxyReaderWriter(file_path='data2.txt')

proxy_rw.read()  # файл читається, текст повертається
proxy_rw.read()  # файл НЕ читається, текст повертається
proxy_rw.write('Marina,Wernadska,65,4000')  # запис в файл відбувається
proxy_rw.read()  # файл читається, текст повертається
proxy_rw.write('Marina,Wernadska,65,4000')  # запис в файл НЕ відбувається
proxy_rw.read()  # файл НЕ читається, текст повертається
proxy_rw.write('Oleksandr,Simach,32,30000')  # запис в файл відбувається
proxy_rw.read()  # файл читається, текст повертається
proxy_rw.write('Marina,Wernadska,65,4000\n ')  # запис в файл відбувається

print(proxy_rw.data)
