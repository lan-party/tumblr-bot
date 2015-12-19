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
    data = urllib.urlopen("https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + term + "&rsz=" + img_num)
    for b in range(1, data.count("unescapedUrl")):
        url = data[find_n(data, "\"unescapedUrl\":\"", b):find_n(data, "\",\"url", b)]
        url= url[16:]
        tmplst += url
        try:
            contents = urllib.urlopen(url).read()
            if not os.path.exists("resources/images/" + term):
                os.mkdir("resources/images/" + term, 0755)
            pic = open("resources/images/"  + term + "/image" + str(b) + "." + ftype, "w+")
            pic.write(contents)
        except Exception, e:
            print(e)

def clearImages(term):
    shutil.rmtree("resources/images/" + term)

def post(server, port, mail_u, mail_p, sendto, tags, img_num, ftype, perm):
    tag = tags.split()
    img_data = open("resources/images/" + tags + "/" + "image" + a + "."  + ftype, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] += str(tags) + perm
    msg['From'] = user
    msg['To'] = sendto
    
    body = ""
    for a in range(0, len(tag)):
        body += str("#" + tag[a] + " ")
    body += tags
    text = MIMEText(body)
    msg.attach(text)
    for a in range(0, len(img_num)):
        image = MIMEImage(img_data, name=os.path.basename("resources/images/" + tags + "/" + "image" + a + "." + ftype))
        msg.attach(image)
    
    s = smtplib.SMTP(serv, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(user, passw)
    s.sendmail(user, sendto, msg.as_string())
    s.quit()
