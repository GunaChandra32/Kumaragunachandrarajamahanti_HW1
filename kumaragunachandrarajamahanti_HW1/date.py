import re


# def check_date(text):
#     pattern = r"(0[1-9]|1[0-2])[-/](0[1-9]|[12][0-9]|3[01])[-/](19|20)\d{2}"
# match = re.search(pattern, text)
# if match:
#     return match.group()
# pattern = r"(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?) (0[1-9]|[12][0-9]|3[01]), (19|20)\d{2}"
# match = re.search(pattern, text)
# if match:
#     return match.group()
# pattern = r"(0[1-9]|1[0-2])[-/](0[1-9]|[12][0-9]|3[01])[-/](\d{2})"
# match = re.search(pattern, text)
# if match:
#     return match.group()
# return "No date found"


import re


def check_date(text):
    patterns = [
        "(?P<month>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)\s+(?P<day>\d{1,2})\s*,\s*(?P<year>\d{4})",
        "(?P<day>\d{1,2})[-/](?P<month>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*),\s*(?P<year>\d{4})",
        "(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})",
        "(?P<month>\d{1,2})[/-](?P<day>\d{1,2})[/-](?P<year>\d{2}|\d{4})",
        "(?P<month>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)\s+(?P<day>\d{1,2})\s*,\s*(?P<year>\d{4})",
        "(?P<day>\d{1,2})[-/](?P<month>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*),\s*(?P<year>\d{4})",
        "(?P<month>\d{1,2})[/-](?P<day>\d{1,2})[/-](?P<year>\d{2}|\d{4})",
        "(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})",
        "(?P<month>January)\s+(?P<day>\d{1,2})\s*,\s*(?P<year>\d{4})",

    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match and match.group().strip() in text.strip():
            return match.group().strip()
    return "No date found"
