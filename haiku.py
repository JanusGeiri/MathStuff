import time
from tqdm import tqdm

text = ''
with open('bee.txt', 'r', encoding="utf8") as f:
    for line in f:
        text += line

words = text.split()
print(words)
