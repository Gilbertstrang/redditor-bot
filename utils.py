import json
import os
import random
import markovify
import re
import emoji

def markov():
        with open("./data/sentences.txt", encoding="utf8") as f:
            text = f.read()

        text_model = markovify.Text(text)

        for i in range(random.randint(1,4)):
            return text_model.make_sentence()
    
def jokes():
        with open("./data/jokes.json", encoding="utf8") as f:
            data = json.load(f)
            l = random.randint(0, len(data) - 1)
            while(data[l]["score"] < 1000):
                l = random.randint(0, len(data) - 1)
            joke = data[l]["title"] +" " + data[l]["body"] + "   Total upvotes: %d" % data[l]["score"]
            return joke
        
        
    

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)

def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']

    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')

    text = last_replace(text, '!', '! {}'.format(random.choice(smileys)))
    text = last_replace(text, '?', '? owo')
    text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))

    for v in vowels:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format('Y' if v.isupper() else 'y', v))

    return text

def dice_roll(numb):
    sub = "--19"
    one = "--r1"
    re1 = False
    if sub in numb:
        crit19 = True
        numb.replace("--19", "")
    if one in numb:
        re1 = True
        numb.replace("--r1", "")
    
    p = re.compile('(\d+)?d(\d+)([\+\-]\d+)?')
    matchobj = p.match(numb)
    
    faces = list()
    if matchobj:
        #die = re.findall("\d+", matchobj.group(2))
        #die = int(die)
        crit = 0
        reroll = 0
        die = int(matchobj.group(2))
        for i in range(1, int(matchobj.group(1)) + 1):
            n = random.randrange(1, die+1)
            
            if n == 20:
                crit = 1
            elif n == 19 and crit19:
                crit = 1
            
            if n == 1 and re1 and die > 1:
                reroll += 1
                n = random.randrange(1, die+1)
            
            faces.append(n)

        if(matchobj.group(3)):
            mod = int(matchobj.group(3))
        else:
            mod = 0
        return faces, mod, crit, reroll

def adv_roll(numb):
    faces, mod = dice_roll(numb)
    faces2, x = dice_roll(numb)
    ls = []
    
    for i in range(0, int(len(faces))):
        ls.append([faces[i], faces2[i]])
        ls[i].sort()
    total = 0
    for i in range(0, int(len(faces))):
        total += ls[i][-1]
    s = ', '.join(str(e) for e in ls)
    
    return total, mod, s
    

def dadv_roll(numb):
    faces, mod = dice_roll(numb)
    faces2, x = dice_roll(numb)
    ls = []
    
    for i in range(0, int(len(faces))):
        ls.append([faces[i], faces2[i]])
        ls[i].sort()
    total = 0
    for i in range(0, int(len(faces))):
        total += ls[i][0]
    s = ', '.join(str(e) for e in ls)
    return total, mod, s 
    