from datetime import datetime


def current_datetime():
    now = datetime.now()
    return now


def calculate_date_difference(date1, date2):
    difference = date2 - date1
    return difference.days


def convert_string_to_datetime(date_str, date_format):
    dt = datetime.strptime(date_str, date_format)
    return dt


if __name__ == "__main__":
    print(current_datetime())

    str1 = "2024-01-01 12:00:00"
    str2 = "2024-02-01 12:00:00"
    str_format = "%Y-%m-%d %H:%M:%S"

    dt1 = convert_string_to_datetime(str1, str_format)
    dt2 = convert_string_to_datetime(str2, str_format)

    print(calculate_date_difference(dt1, dt2))
