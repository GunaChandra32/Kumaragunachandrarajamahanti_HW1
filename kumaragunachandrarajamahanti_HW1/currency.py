import re


# def check_currency(text):
#     pattern = r"(?i)(\$|USD|\+\$|-\$|USD|\$|K|B|M)[0-9,]*(\.\d{1,2})?"
#     match = re.search(pattern, text)
#     if match:
#         return match.group()
#     return "No currency found"


def check_currency(text):
    pattern = r"(?i)(?:\$|USD|\+\$|-\$|USD)?[0-9,]+(?:\.[0-9]{2})?(?:[MK]|[B])?"
    match = re.search(pattern, text)
    if match and match.group().strip() == text.strip():
        return match.group().strip()
    return "No currency found"
