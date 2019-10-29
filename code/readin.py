import os

def readin(dirpath='../dataset/test_data/dna_rat_10/'):
    # path = '../dataset/test_data/dna_rat_10/dna_rat_10_BZ135269.fasta'
    # dirpath = '../dataset/test_data/dna_rat_10/'
    files= os.listdir(dirpath)
    SR = ["" for i in range(len(files))]
    print(files)
    for i in range(len(files)):
        with open(dirpath+files[i], 'r+') as f:
            for line in f:
                if line.startswith('>'):
                    continue
                else:
                    SR[i]+=line.replace('\n','').strip()

    # print(len(seq['gi|23776216|gb|BZ135269.1|BZ135269']))

    # print(len('AATTGGAATTCTCTCTTCCTGGTCTGTCTAAGATGGGGATAAATTGGTGTAAAAAAAAAAAAAAAAAAAA'))
    # for i in range(len(files)):
    #   print(len(SR[i]))
    return SR
