# This module handles the email client in order to download the data.

# solution from: https://www.thepythoncode.com/article/reading-emails-in-python


# import libraries
import imaplib
import email
import os

# account credentials
username = "ashurbanipal.dev@gmail.com"
password = "Ashurbanipal2021Q2"


def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

# connect to the IMAP server:
# create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)

status, messages = imap.select("INBOX")
# number of top emails to fetch
N = 25
# total number of emails
messages = int(messages[0])

if N>messages:
    N = messages

for i in range(messages, messages-N, -1):
    # fetch the email message by ID
    res, data = imap.fetch(str(i), "(RFC822)")
    email_msg = email.message_from_bytes(data[0][1])

    if email_msg.is_multipart():
        # Itterate through email pats
        for part in email_msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                body = body.decode()

                # Save the file
                folder_name = "data_base"
                if not os.path.isdir("data_base"):
                    # make a folder for this email/data
                    os.mkdir("data_base")
                filename = "key_data_" + str(i) + ".txt"
                filepath = os.path.join(folder_name, filename)
                # write the file
                open(filepath, "w", newline='').write(body)

            else:
                continue


# close the connection and logout
imap.close()
imap.logout()