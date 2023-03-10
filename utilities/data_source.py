from utilities import read_utils
test_invalid_login_data = [
    ("Admin1", "admin1", "Invalid credentials"),
    ("Admin2", "admin2", "Invalid credentials")
]

test_valid_login_data = [
    ("Admin", "admin123")
]

test_add_valid_employee_data = [
    ["Admin", "admin123", "John", "J", "Wick", "John Wick", "John"],
    ["Admin", "admin123", "Peter", "p", "Wick", "Peter Wick", "Peter"]
]

test_invalid_login_data=read_utils.get_csv_as_list("../test_data/test_invalid_login_data.csv")