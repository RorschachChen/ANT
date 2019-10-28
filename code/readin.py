path = '../dataset/test_data/dna_rat_10/dna_rat_10_BZ135269.fasta'
with open(path, 'r+') as f:
    seq={}
    for line in f:
        if line.startswith('>'):
            name=line.replace('>','').split()[0]
            seq[name]=''
        else:
            seq[name]+=line.replace('\n','').strip()

print(len(seq['gi|23776216|gb|BZ135269.1|BZ135269']))

# print(len('AATTGGAATTCTCTCTTCCTGGTCTGTCTAAGATGGGGATAAATTGGTGTAAAAAAAAAAAAAAAAAAAA'))
