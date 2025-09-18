text = "Hello,,, Data---Engineer!!   Welcome123   "

# Remove all non-alphabetic characters
# Trim extra spaces
# The final result is lowercase words separated by a single space

import re
text = text.lower()

# Replace every non alphabet with space ' '

text = re.sub(r'[^a-z]', ' ', text)
text = re.sub(r'\s+', ' ', text)
text = text.strip()

print(text)