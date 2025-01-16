import random as r, string as s, os, discord, requests
def contra(largo):
    elements = s.ascii_letters+s.ascii_lowercase+s.ascii_uppercase+s.digits+s.punctuation
    password = ''
    for i in range(largo):
        password += r.choice(elements)
    return password
def coin():
    moneda = ["aguila", "sol"]
    select = r.choice(moneda)
    return select

def meme():
    with open("img/memes1.jfif", "rb") as img:
        pic = discord.File(img)
    return pic

def momo():
    listmeme = r.choice(os.listdir("img"))
    with open(f"img/{listmeme}", "rb") as img:
        pic = discord.File(img)
    return pic

def duck_image():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data[ url ]