import re

# I. Extract all email addresses from a given text
def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

# II. Validate a date in the format "YYYY-MM-DD"
def validate_date(date_string):
    date_pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
    return bool(re.match(date_pattern, date_string))

# III. Replace all occurrences of a word with another word in a string
def replace_word(text, old_word, new_word):
    return re.sub(rf'\b{re.escape(old_word)}\b', new_word, text)

# IV. Split a string by all non-alphanumeric characters
def split_by_non_alphanumeric(text):
    return re.split(r'\W+', text)

# --- Demo Section ---

# Task I
sample_text = "Contact us at support@example.com, admin123@mail.co.uk or visit our site."
emails = extract_emails(sample_text)
print("Extracted Emails:", emails)

# Task II
date_input = "2025-04-05"
print(f"Is '{date_input}' a valid date?", validate_date(date_input))

# Task III
original_text = "Python is powerful. I love Python!"
replaced_text = replace_word(original_text, "Python", "Java")
print("Replaced Text:", replaced_text)

# Task IV
split_text = "Hello, world! Let's code in Python3."
split_result = split_by_non_alphanumeric(split_text)
print("Split Result:", split_result)
