import string

with open ('data.txt','rt') as file:
    text=file.read()

def occur(text):
    dict={}
    mots_brute=text.split()
    mots=[mot.strip(string.punctuation) for mot in mots_brute ]
    for mot in mots :
        dict[mot]=mots.count(mot)
    return dict

def longueur_moy(text):
    longuer=[len(mot) for mot in occur(text)]
    return sum(longuer)/len(longuer)

def moin_util(text):
    dict = occur(text)
    minimum=min(dict.values())
    return [mot for mot in dict if dict[mot]==minimum]

def plus_util(text):
    dict=occur(text)
    maximum=max(value for value in dict.values())
    return [mot for mot in dict if dict[mot] == maximum]

def nbr_phrs(text):
    return len(text.split(','))

def palind(text):
    dict=occur(text)
    return [mot for mot in dict if mot == mot[::-1] ]

def phrases(text):
    for sep in ".,!?;":
        text=text.replace(sep,'.')
    phrases=text.split('.')
    phrases=[phrase.strip(' ') for phrase in phrases if phrase.strip()]
    return phrases

def len_phrs(text):
    return {phrase : sum(1 for c in phrase if c.isalpha()) for phrase in phrases(text) }

def type_punct(text):
    return set ([punct for punct in text if punct in string.punctuation])

def plus_longu_phrs(text):
    phras = phrases(text)
    lettres_par_phrase = [sum(1 for c in phrase if c.isalpha()) for phrase in phras]
    maximum = max(lettres_par_phrase)
    return [phrase for phrase, lettres in zip(phras, lettres_par_phrase) if lettres == maximum]



print('Le frequence des mots est :',occur(text))
print('le longuer moyene et :',longueur_moy(text))
print('Les mot moins utilise est :',moin_util(text))
print('Les mot plus utilise est :',plus_util(text))
print('nombre des phrases est :',nbr_phrs(text))
print('les palindromes dans ce text est :',palind(text))
print('Le nombre des phrases est :',len(phrases(text)))
print('le lounguer des phrases :',len_phrs(text))
print('Les punctiation utilse sont :',type_punct(text))
print('La plus longue phrase est :',plus_longu_phrs(text))
