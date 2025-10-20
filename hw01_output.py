import json


with open('c:\\Users\\anna\\Documents\\alice.txt','r', encoding='utf-8') as file:
    text = file.read()

text = text.lower()
text = text.replace(' ', '')    
text = text.replace('\n', '')

znak_counts = {}


for znak_textu in text:
    if znak_textu not in znak_counts:
        znak_counts[znak_textu] = 0
    else:
        znak_counts[znak_textu] = znak_counts[znak_textu] + 1

with open('hw01_output.json', 'w', encoding='utf-8') as f:
    json.dump(znak_counts, f, ensure_ascii=False, indent=4)