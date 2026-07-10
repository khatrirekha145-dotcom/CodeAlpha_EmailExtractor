import re

# Read input file
with open("emails.txt", "r") as file:
    content = file.read()

# Extract emails
emails = re.findall(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    content
)

# Remove duplicates
unique_emails = list(set(emails))

# Save emails
with open("extracted_emails.txt", "w") as file:
    for email in unique_emails:
        file.write(email + "\n")

# Display statistics
print("\n----- EMAIL EXTRACTION REPORT -----")
print("Total emails found:", len(emails))
print("Unique emails:", len(unique_emails))
print("Saved to extracted_emails.txt")