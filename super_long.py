import random
import webbrowser

for i in range(383759):

    d1 = random.choice([str(random.randint(1, 3)), ''])
    d2 = str(random.randint(0, 9))
    d3 = str(random.randint(0, 9))
    d4 = str(random.randint(0, 9))
    d5 = str(random.randint(0, 9))
    d6 = str(random.randint(0, 9))

    sauce = f'https://nhentai.net/g/{d1 + d2 + d3 + d4 + d5 + d6}/'

    webbrowser.open(sauce)
    print(sauce)
