import re

name_regex = re.compile(r"^[A-Z][a-z]*(?:['-][A-Z][a-z]+| [A-Z][a-z]+)*$")

phone_regex = re.compile(
    r"^(?:\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
)

email_regex = re.compile(
    r"^[a-z]+(?:\.[a-z0-9]+)*@[a-z]+\.[a-z]+$"
)
