import re


def check_phone_number(text):
    patterns = ["(?:\d{3}-)(?:\d{3}-)(?:\d{3}-)\d{4}",
                "(?:\+1\s)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match and match.group().strip() == text.strip():
            return match.group().strip()
    return "No phone number found"
