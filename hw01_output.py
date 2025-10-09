import json


with open('c:\\Users\\anna\\Documents\\alice.txt','r', encoding='utf-8') as file:
    text = file.read()

text = text.lower()
text = text.replace(' ', '')    
text = text.replace('\n', '')

# znak_counts = {
#     "!": 0,
#     "(": 0,
#     ")": 0,
#     "*": 0,
#     ",": 0,
#     "-": 0,
#     ".": 0,
#     ":": 0,
#     ";": 0,
#     "?": 0,
#     "[": 0,
#     "]": 0,
#     "_": 0,
#     "a": 0,
#     "b": 0,
#     "c": 0,
#     "d": 0,
#     "e": 0,
#     "f": 0,
#     "g": 0,
#     "h": 0,
#     "i": 0,
#     "j": 0,
#     "k": 0,
#     "l": 0,
#     "m": 0,
#     "n": 0,
#     "o": 0,
#     "p": 0,
#     "q": 0,
#     "r": 0,
#     "s": 0,
#     "t": 0,
#     "u": 0,
#     "v": 0,
#     "w": 0,
#     "x": 0,
#     "y": 0,
#     "z": 0,
#     "ù": 0,
#     "—": 0,
#     "‘": 0,
#     "’": 0,
#     "“": 0,
#     "”": 0,
# }

znak_counts = {}


for znak_textu in text:
    if znak_textu not in znak_counts:
        znak_counts[znak_textu] = 0
    else:
        znak_counts[znak_textu] = znak_counts[znak_textu] + 1

with open('hw01_output.json', 'w', encoding='utf-8') as f:
    json.dump(znak_counts, f, ensure_ascii=False, indent=4)


































    # if znak_textu in znak_counts:
    #     # pismenko je ve slovniku -> pridej jedna
    #     znak_counts[znak_textu] = znak_counts[znak_textu] + 1
    # else:
    #      # pismenko neni ve slovniku -> pridam pismenko do slovniku a dam mu hodnotu jedna
    #     znak_counts[znak_textu] = 1


   

print(znak_counts)

with open('hw01_output.json', 'w', encoding='utf-8') as f:
    json.dump(znak_counts, f, ensure_ascii=False, indent=4)