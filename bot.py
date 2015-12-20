import os
import time
import smtplib
import urllib
import shutil
import func
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Variable Definition
lst = open("resources/config.txt").read().splitlines()
tags = open("resources/tags.txt").read().splitlines()
port = int(lst[1])
image_num = int(lst[5])
loop_out = int(lst[6])
loop_in = int(lst[7])
post_sum = int(lst[8])
sleep_t = float(lst[10])
server = lst[0]
mail_u = lst[2]
mail_p = lst[3]
sendto = lst[4]
ftype = lst[9]
permtag = lst[11]
lst.close()


# Primary Loop
for a in range(loop_out, len(tags)):
    temp0 = list(func.permutations(tags, a))
    open("resources/data.txt", "w").close()
    for b in range(0, len(temp0)):
        temp1 = " ".join(temp0[b])
        open("resources/data.txt", "a").write(temp1 + "\n")
    data = open("resources/data.txt", "r").read().splitlines()
    # Secondary Loop
    for b in range(loop_in, len(data)):
        ctag = data[b]
        func.getImages(ctag, image_num, ftype)
        post(server, port, mail_u, mail_p, sendto, ctag.split(), image_num, ftype, permtag)
        # Write variables to config and clear images
        func.clearImages(ctag)
        post_sum += 1
        lst = open("resources/config.txt").read().splitlines()
        lst[6] = loop_out
        lst[7] = loop_in
        lst[8] = post_sum
    time.sleep(3600 * sleep_t)
# loop1(outer loop variable +1){
#  clear data;
#  write tags to data.txt(a);
#  split data.txt to list;
#  loop2(inner loop variable +1){
#   ctag = data[inner loop variable];
#   download images from tags(inner loop variable);
#   post images with tags;
#   write variables to config;
#  }
#  sleep;
# }
