from random import choice, randint
from webbrowser import open

for _ in range(99999999):
    sauce = 'https://nhentai.net/g/'
    sauce += choice([str(randint(1, 3)), ''])
    for _ in range(5):
        sauce += str(randint(0, 9))
    open(sauce)
