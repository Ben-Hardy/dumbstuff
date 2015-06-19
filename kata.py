import math

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

def main():
    #print pattern2(5)
    #for i in range(1,1000):
     #   if (math.factorial(i-1)+1) % i == 0:
      #      print i 
    print f(37131802, 75843520)

if __name__ == "__main__":
    main()