from _collections_abc import Sequence
from typing import Iterator

PAIRS = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


class DNA(Sequence):
    def __init__(self, chain) -> None:
        self.first_chain = chain
        self.dna = []
        for el in chain:
            self.dna.append(tuple((el, PAIRS[el])))

    def __str__(self):
        return self.first_chain

    def __getitem__(self, index):
        return self.dna[index]

    def __len__(self):
        return len(self.dna)

    def __iter__(self) -> Iterator:
        yield from self.dna

    def __reversed__(self) -> Iterator:
        return reversed(self.dna)

    def __contains__(self, value: object) -> bool:
        return value in self.first_chain

    def __eq__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return self.first_chain == value.first_chain
        return NotImplemented

    def __neq__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return self.first_chain != value.first_chain
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.first_chain+other.first_chain)
        return NotImplemented

# INPUT DATA:


# TEST_1:
dna = DNA('AGTC')

print(dna[0])
print(dna[1])
print(dna[2])
print(dna[3])
print(dna[-1])
print(dna[-2])

# TEST_2:
dna = DNA('AGT')

print(dna)
print(len(dna))
print('A' in dna)
print('C' in dna)

# TEST_3:
dna1 = DNA('ACG')
dna2 = DNA('TTTAAT')
dna3 = dna1 + dna2
dna4 = dna2 + dna1

print(dna3, type(dna3))
print(dna4, type(dna4))

# TEST_4:
dna1 = DNA('ACG')
dna2 = DNA('TTTAAT')
dna3 = DNA('TTTAAT')

print(dna1 == dna2)
print(dna2 == dna3)
print(dna1 != dna3)
print(dna2 != dna3)

# TEST_5:
dna = DNA('TGAACCTGACCTCGATTTCAAGGG')

print(*dna)
print(*reversed(dna))
print('A' in dna)
print('C' not in dna)

# TEST_6:
dna = DNA('ACG')
not_supported = [1, 2.23, [1, 2, 3], {1: 'one'}, {
    4, 5, 6}, True, False, 'CTA', (7, 8, 9)]

for item in not_supported:
    print(item == dna)

# TEST_7:
dnas = ['TAAAACCCCATCGGCTCTGACAATGAAC', 'AGATGTTCCCTCTAATATCTATACGAAT', 'ACGACGCACTGCATACAATACAATAGTG',
        'TCCCAGTCAGGATCGGATTGGTATAATC', 'TACACGCATAGTGCCCAACTCCTACCCG', 'TCACCGCTGAAAACATGTTCTGGAGGGC',
        'CCCAGGATAGACCTATTTGCCGTATCCA', 'ATCGATCGTGCGGGAAATCCTGCCATAT', 'AGACCAACTTATTGGGCACACGCTCCGG',
        'CGCGTCCCCCATATCAACGCGTGAATGC', 'AGTCACGATCAGCTGGACGTAGTGGCAA', 'GTGTAGGGTCAAGGGACACCTGATATCT',
        'AAAAGACGAAAATTGCTAAGTGGCAGTC', 'TGGAGGCCGAGCTCGCGTTGGAAATAGT', 'AAGTCTGCCGAGGCGGGTCGGGAGCGCC',
        'ATTATCCAATCCAGTCACGTATTGAATA', 'ATTGTGAACCTTATACGTTAGTAATACC', 'AGACAATCATGCTATTAGGTATGACGTT',
        'ATCACTGAGGCAGAGACTAGCCGCGCTT', 'TATGGGTGGTATCCTAAGCATTCAATGG']

for base in dnas:
    dna = DNA(base)
    print(*dna)

# TEST_8:
dna = DNA('ACG')
print(dna.__eq__(1))
print(dna.__ne__(1.1))
print(dna.__add__([1, 2, 3]))
