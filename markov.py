import time
import re
import random
from tqdm import tqdm
text = ''
with open('gisli.txt', 'r', encoding="utf8") as f:
    for line in f:
        text += line
order = 5
# text = 'Testing for the ultra testing purposes of purple testing for words that have very wordular meanings'
ngrams = []
start = time.time()
print("Initializing... ")
print("Please wait for 'Seed:'")
length = len(text)-order-1
length_10 = length/10
num = int(length/length_10)

for i in tqdm(range(len(text)-order)):
    # num_i = int((length-i)/length_10)
    # if num_i != num:
    #     print(num_i+1)
    #     num = num_i

    gram = text[i:i+order]

    array = re.finditer(re.escape(gram), text)
    match_pos = [match.start()
                 for match in array if match.start() <= len(text)-1-order]

    next_chars = [text[i+order] for i in match_pos]

    if not [gram, next_chars] in ngrams:
        ngrams.append([gram, next_chars])


print('Initialization took', time.time()-start, 'seconds')


def markov(ngrams, length):
    global order
    while(True):
        state = True
        a = input("Seed: ")
        if a == "":
            break
        result = a
        if len(a) > order:
            a = a[-order:]
        currentGram = a
        if state:
            for i in range(length):
                index = -1
                for p, items in enumerate(ngrams):
                    if items[0] == currentGram:
                        index = p
                possibilities = ngrams[index][1]
                if possibilities == []:
                    state = False
                next_string = random.choice(possibilities)

                result += next_string
                currentGram = result[-order:]
                if (next_string == '.' or next_string == '!' or next_string == '?') and i > 0.95*length:
                    break
        print(result)


length = 1000
markov(ngrams, length)
