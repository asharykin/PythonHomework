class Buffer:
    def __init__(self):
        self.buffer = []

    def add_data(self, data):
        self.buffer.append(data)
        if len(self.buffer) >= 5:
            print("Переполнение буфера. Буфер будет очищен")
            self.buffer.clear()

    def get_data(self):
        if not self.buffer:
            print("Буфер пуст")
            return None
        return self.buffer
