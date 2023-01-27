import re


def exclude_html_tags(text):
    return re.sub(r'<.*?>', '', text)
