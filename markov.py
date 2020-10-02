import time
import random
text = ''
with open('bee.txt', 'r', encoding="utf8") as f:
    for line in f:
        text += line
order = 5
ngrams = []
start = time.time()
print("Initializing... ")
print("Please wait for 'Seed:'")
length = len(text)-order-1
length_10 = length/10
num = int(length/length_10)

for i in range(len(text)-order-1):
    num_i = int((length-i)/length_10)
    if num_i != num:
        print(num_i+1)
        num = num_i

    gram = text[i:i+order]
    index = -1
    P = True
    for j, item in enumerate(ngrams):
        if gram == item[0]:
            P = False
            index = j
    if P:
        ngrams.append([gram, [text[i+order]]])
    else:
        ngrams[index][1].append(text[i+order])

print('0')
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
