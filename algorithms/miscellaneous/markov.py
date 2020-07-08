import codecs
import random

MAX_LETTERS = 2000

def readFile(f, mp, k):
    seed = ''
    mostFreqSeed = seed
    mostFreq = 1
    for line in f:
        for ch in line:
            seed, mostFreq, mostFreqSeed = processSeed(seed, mostFreqSeed, mostFreq, ch, k, mp)
    return mostFreqSeed
                
def processSeed(seed, mostFreqSeed, mostFreq, ch, k, mp):
    seed += ch
    if len(seed) == k+1:
        oldSeed = seed[:-1]
        mp.setdefault(oldSeed, []).append(ch)
        if mostFreq < len(mp[oldSeed]):
            mostFreq, mostFreqSeed =  len(mp[oldSeed]), oldSeed
        seed = seed[1:]
    return seed, mostFreq, mostFreqSeed

def generateText(mp, mostFreqSeed):
    text, curSeed = mostFreqSeed, mostFreqSeed
    while (len(text) < MAX_LETTERS):
        ch = random.choice(mp[curSeed])
        text, curSeed = text+ch, curSeed+ch
        curSeed = curSeed[1:]
    return text

def main():
    fileName = input("Enter the file name: ") + ".txt"
    f = codecs.open(fileName, encoding='utf-8')
    k = int(input("Enter the Markov order [1-10]: "))
    assert (k >= 1 and k <= 10)
    mp = {}
    mostFreqSeed = readFile(f, mp, k)
    f.close()
    text = generateText(mp, mostFreqSeed)
    print(text)
    result = codecs.open("result.txt", "w", encoding='utf-8')
    result.write(text)
    result.close()

if __name__ == "__main__":
    main()