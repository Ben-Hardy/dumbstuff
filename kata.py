import math

import unittest

def getWinner(listOfBallots):
  #your code
  candidates = set(listOfBallots)
  tally = []
  for i in candidates:
      tally.append([i, listOfBallots.count(i)])
  print tally
  
  for i in tally:
      if i[1] > len(listOfBallots) / 2:
          return i[0]
  return None
  
  
def reverseNumber(n):
  return int(str(n)[::-1])

def palindrome_chain_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    flipCounter = 0
    cur = n
    while cur != reverseNumber(cur):
        flip = reverseNumber(cur)
        cur = cur + flip
        flipCounter += 1
    return flipCounter
    
    
    
acids = {# Phenylalanine
    'UUC':'F', 'UUU':'F',
    # Leucine
    'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L','CUA':'L','CUG':'L', 
    # Isoleucine
    'AUU':'I', 'AUC':'I', 'AUA':'I', 
    # Methionine
    'AUG':'M', 
    # Valine
    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V', 
    # Serine
    'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S', 
    # Proline
    'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 
    # Threonine
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    # Alanine
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 
    # Tyrosine
    'UAU':'Y', 'UAC':'Y', 
    # Histidine
    'CAU':'H', 'CAC':'H',
    # Glutamine
    'CAA':'Q', 'CAG':'Q', 
    # Asparagine
    'AAU':'N', 'AAC':'N', 
    # Lysine
    'AAA':'K', 'AAG':'K',
    # Aspartic Acid
    'GAU':'D', 'GAC':'D', 
    # Glutamic Acid
    'GAA':'E', 'GAG':'E',
    # Cystine
    'UGU':'C', 'UGC':'C',
    # Tryptophan
    'UGG':'W', 
    # Arginine
    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 
    # Glycine
    'GGU':'G',  'GGC':'G', 'GGA':'G', 'GGG':'G', 
    # Stop codon
    'UAA':'Stop', 'UGA':'Stop', 'UAG':'Stop'
    }
def protein(rna):
    res = ""
    for i in range(0, len(rna), 3):
        if acids[rna[i:i+3]] == "Stop":
            return res
        else:
            res += acids[rna[i:i+3]]
    return res


vals = { 'A':1, 'B':2,  'C':3,  'D':4,  'E':5,  'F':6, 'G':7,  'H':8,  'I':9,
         'J':10,  'K':11,  'L':12,  'M':13,  'N':14,  'O':15,  'P':16,  'Q':17,
         'R':18,  'S':19,  'T':20,  'U':21,  'V':22,  'W':23,  'X':24,  'Y':25,  'Z':26 }
'''def ride(group,comet):
    gtotal = 1
    for i in range(group):
        gtotal *= vals[group[i]]
    ctotal = 1
    for i in range(comet):
        ctotal *= vals[comet[i]]
'''
    #return 'GO' if ctotal % 47 == gtotal % 47 else return 'STAY'

def pattern(n):
    s = ""
    for i in range(1,n+1):
        s += "".join(str(i) for j in range(1,i+1))
        if i < n:
            s += "\n"
    return s

def pattern2(n):
    s = "".join(str(i) for i in range(1,n)[::-1])
    l = len(s)
    for i in range(1,n+1):
        s += "\n" + s[l - i]
    return s 

def f(n, m):
  return sum([i % m for i in xrange(1, n+1)])

def pig_it(text):
    words = text.split(" ")
    
    res = []
    for word in words:
        if word.isalpha():
            tmp = word[1:] + word[0] + "ay"
            res.append(tmp)
        else: res.append(word)
    return " ".join(res)

def pig_it2(text):
    return " ".join(i[1:] + i[0] + "ay" if i.isalpha() else i for i in text.split(" "))


def hamming(a, b):
    return len(a) - sum([a[i] == b[i] for i in range(len(a))])
    
    
def triangle_number_generator(n):
    a = 0
    l = []
    for i in range(1, n):
        a += i
        l.append(a)
    return l

# Caesar Cipher. SO UGLY
# This is by far the ugliest solution I've come up with for a kata. UUGGHHHHHHH
def encryptor(key, message):

    # Chop off everything else past 26 so we only have numbers < 26. Gets rid of cases where key is > 26
    if key > 0:
        key = key % 26
    else:
        key = (abs(key) % 26) * -1 # gotta handle modulo for negatives too

    if len(message) == 0:
        return ""
    else:
        codes = [ord(i) for i in message]
        res = []
        for i in codes:
            if i < 65 or i > 122 or (i > 90 and i < 97):
                res.append(i)
            elif i > 96:
                if i + key > 122:
                    res.append(i + key - 26)
                elif i + key < 97:
                    res.append(i + key + 26)
                else: res.append(i + key)
            elif i >= 65 and i < 91:
                if i + key > 90:
                    res.append(i + key - 26)
                elif i + key < 65:
                    res.append(i + key + 26)
                else: res.append(i + key)
        
        return "".join([chr(i) for i in res])



def is_divisible(*nums):
    return len(nums) == sum([nums[0] % i == 0 for i in nums])

def main():
    #print pattern2(5)
    #for i in range(1,1000):
     #   if (math.factorial(i-1)+1) % i == 0:
      #      print i 
    #print f(37131802, 75843520)
    
    #print(pig_it2('Pig latin is cool') == 'igPay atinlay siay oolcay')
    #print(pig_it('This is my string') == 'hisTay siay ymay tringsay')
    #print hamming("I like turtles","I like turkeys") == 3
    #print triangle_number_generator(10000).index(1001820)
    #print triangle_number_generator(100000)[-5]
    print is_divisible(3,3,4)


if __name__ == "__main__":
    main()
