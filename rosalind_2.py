######################################################################################################
#Problem 26
#Perfect Matchings and RNA Secondary Structures

# from math import factorial as fac

# def perfect_matchings(rna):
#    return fac(rna.count('A')) * fac(rna.count('C'))

# from Bio import SeqIO
# reads = []
# for rec in SeqIO.parse("c:/Users/Matt/downloads/rosalind_pmch.txt", "fasta"):
#     reads.append(str(rec.seq))

# for x in reads:
#     print(x)
#     print(perfect_matchings(x))

######################################################################################################
#Problem 27
#Partial Permutations

# from math import factorial as fac

# with open("c:/Users/Matt/downloads/rosalind_pper.txt") as f: 
#     protein = f.read()

# print(protein)
# n, k = protein.split()
# n, k = int(n), int(k)

# print(n, k)
# # n = 99
# # k = 9

# print(fac(n) / fac(n-k) % 1000000)

######################################################################################################
#Problem 28
#Introduction to Random Strings

import math

s = "ACGATACAA"
arr = [0.129]
# arr = [0.129, 0.287, 0.423, 0.476, 0.641, 0.742, 0.783]

def rand_string_calc(s, arr):

    GC = (arr/2)
    AT = ((1 - arr) / 2)

    print(GC, AT)

    C = (s.count('C'))
    G = (s.count('G'))
    A = (s.count('A'))
    T = (s.count('T'))

    print(math.log10(GC**(C+G)) + (math.log10(AT ** (A+T))))

for x in arr:
    rand_string_calc(s, x)