import os
import smtplib
import urllib
import func
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

tags = open("resources/tags.txt", "r").read().splitlines()


for b in range(1, len(tags)+1):
    test = func.permutations(tags, b)
    test = list(test)
    for a in range(0, len(test)):
        temp = " ".join(test[a])
        open("resources/data.txt", "a").write(temp + "\n")
