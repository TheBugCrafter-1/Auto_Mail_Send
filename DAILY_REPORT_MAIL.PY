import webbrowser
import urllib.parse
from datetime import datetime

# ===== USER INPUT =====

to = "ashishberiya11@gmail.com"
cc = "witcher000000000@gmail.com,ashishberiy@gmail.com,ashishberiya10@gmail.com"

# Aaj ki date automatically
today = datetime.now().strftime("%d-%m-%Y")

subject = input(f"Subject (Press Enter for default): ")
if subject == "":
    subject = f"Daily Report | {today} | Napo Exports "

print("\nWrite your email body.")
print("Press Enter twice when finished.\n")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

body = "\n".join(lines)

# ===== URL ENCODE =====


params = {
    "view": "cm",
    "fs": "1",
    "to": to,
    "cc": cc,
    "su": subject,
    "body": body
}

url =  "https://mail.google.com/mail/?" + urllib.parse.urlencode(params)

print("\nOpening Gmail Draft...")

webbrowser.open(url)