import os
import time
import smtplib
import urllib
import shutil
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def find_n(s, ss, n):
    i = -1
    for _ in range(n):
        i = s.find(ss, i + len(ss))
        if i == -1:
            break
    return i

def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def getImages(term, img_num, ftype):
    tmplst = []
    data = urllib.urlopen("https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + term + "&rsz=" + str(img_num)).read()
    print(data)
    for b in range(1, data.count("unescapedUrl")):
        url = data[find_n(data, "\"unescapedUrl\":\"", b):find_n(data, "\",\"url", b)]
        url= url[16:]
        tmplst += url
	print(url)
        try:
            contents = urllib.urlopen(url).read()
            if not os.path.exists("resources/images/" + term):
                os.mkdir("resources/images/" + term)
            pic = open("resources/images/"  + term + "/image" + str(b) + "." + ftype, "w+")
            pic.write(contents)
        except Exception, e:
            print(e)

def clearImages(term):
    shutil.rmtree("resources/images/" + term)

def post(server, port, mail_u, mail_p, sendto, tags, img_num, ftype, perm):
    msg = MIMEMultipart()
    msg['Subject'] = str(tags) + str(perm)
    msg['From'] = mail_u
    msg['To'] = sendto
    
    body = ""
    for a in range(0, len(tags)):
        body += str("#" + tags[a] + " ")
    body += " ".join(tags)
    text = MIMEText(body)
    msg.attach(text)
    print("Posting"),
    for a in range(0, img_num):
	if not os.path.exists("resources/images/" + " ".join(tags)):
	    os.mkdir("resources/images/" + " ".join(tags))
	try:
	    img_data = open("resources/images/" + " ".join(tags) + "/" + "image" + str(a) + "."  + ftype, 'rb').read()
            print("."),
            image = MIMEImage(img_data, name=os.path.basename("resources/images/" + " ".join(tags) + "/" + "image" + str(a) + "." + ftype))
            msg.attach(image)
	except Exception:
	    pass
    try:
        s = smtplib.SMTP(serv, port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(user, passw)
        s.sendmail(user, sendto, msg.as_string())
        s.quit()
        print("Success!")
    except Exception:
        print("Failed!")
