def elim(word, pat):
    matches = []
    contains = []
    notin = ""
    for i, c in enumerate(pat):
        if c == "m":
            matches.append([word[i], i])
        elif c == "c":
            contains.append([word[i], [i]])
        else:
            notin += word[i]
    
    return matches, contains, notin

def matches(placements, contains, not_contains, bank, duplicates):
    matches = []
    for word in bank:
        match = True
        for c in placements:
            if c[0] not in word:
                match = False 
                break
            elif word[c[1]] != c[0]:
                match = False
                break   
        if match:
            matches.append(word)
                    
    matches2 = []
    for word in matches:
        match = True
        for c in contains:
            if c[0] not in word:
                match = False 
                break
            for p in c[1]:
                if word[p] == c[0]:
                    match = False
        if match:
            matches2.append(word)
            
    matches3 = []
    for word in matches2:
        match = True
        for c in not_contains:
            if c in word:
                match = False 
                break
        if match:
            matches3.append(word)
    
    matches4 = []
    for word in matches3:
        match = True
        for c in word:
            if not duplicates and word.count(c) > 1:
                match = False 
                break
        if match:
            matches4.append(word)
    
    def vowel_count(w):
        vs = ["a", "e", "i", "o", "u", "y"]
        c = 0
        for v in vs:
            c += w.count(v)
        return c
    
    matches4.sort(key=vowel_count, reverse=True)
    
    
    return matches4


with open("words_alpha.txt", "r") as f: 
    lines = f.readlines()

five = []
for line in lines:
    line = line[:-1]
    if len(line) == 5:
        five.append(line)


contains = []
match = []
notin = ""
dub = False
while True:
    ms = matches(match, contains, notin, five, dub)
    i = 0
    for m in ms:
        print(i, m)
        i += 1
        if i > 5:
            break

    if input("y/n allow duplicates > ") == "y":
        dub = True
        continue

    i = int(input("selct word > ")) 
    p = input("result > ")
    m, c, n = elim(ms[i], p)
    match += m
    contains += c
    notin += n
