def read_numeric_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.readlines()
    for line in data:
        stripped_line = line.strip()
        if stripped_line.isdigit():
            print(stripped_line)
        else:
            raise TypeError(f"'{stripped_line}' не является числом")


if __name__ == "__main__":
    read_numeric_lines("data.txt")  # При отсутствии такого файла FileNotFoundError будет выброшена сама