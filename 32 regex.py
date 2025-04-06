# Scenario: Finding all email addresses in a text.
import re
text = "Contact us at abc@gmail.com or support@another.org."
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(f"Found emails: {emails}")