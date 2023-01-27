import re
from currency import check_currency
from date import check_date
from phone_numbers import check_phone_number
from tags import exclude_html_tags


def main():
    with open("input.txt", "r") as f:
        text = f.read()
        text = exclude_html_tags(text)
        for i in text.split("\n"):
            i = i.strip()
            if i != "":
                if check_currency(i) in i:
                    print("Valid Currency: ", i)
                elif check_date(i) in i:
                    print("Valid Date: ", i)
                elif check_phone_number(i) in i:
                    print("Valid PhoneNumber: ", i)
                else:
                    print("Invalid String: ", i)


if __name__ == "__main__":
    main()
