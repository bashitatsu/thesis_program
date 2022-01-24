import pickle
import re

def make_list(path):
    with open(path, "r", encoding="utf8", errors='ignore') as f:
        l = []
        sub_l = ""
        for align in f:
            if ">" not in align:      
                align = align.strip()
                sub_l += align
            else:
                protein = align # 1つの時用
                l.append(sub_l)
                sub_l = ""

        l.append(sub_l)
        l.pop(0)
        print(protein)

    return l

def count_scs(l):
    d = {}
    scs = 5
    for sub in l:
        for i in range(len(sub) - scs + 1):
            if sub[i:i+scs] not in d.keys():
                d[sub[i:i+scs]] = 1
            else:
                d[sub[i:i+scs]] += 1
    
    return d

# make_list + count_scs
def make_dict(path):
    l = make_list(path)
    d = count_scs(l)

    return d

# refseqの辞書をload
def p_load():
    with open("refseq_dic.pickle", "rb") as f:
        refseq_dic = pickle.load(f)
    return refseq_dic

def hdic_load():
    with open("hdic.pickle", "rb") as f:
        hdic = pickle.load(f)
    return hdic

def make_distance(path):
    target_dic = make_dict(path)
    refseq_dic = p_load()
    scs_vector = [0] * len(refseq_dic.keys())
    refseq_keys = list(refseq_dic.keys())
    for refkey in range(len(refseq_dic.keys())):
        if refseq_keys[refkey] in target_dic.keys():
            scs_vector[refkey] = 1
    
    scs_distance = sum(scs_vector)

    return len(refseq_keys), scs_distance

def h_distance(path):
    target_dic = make_dict(path)

    for i in range(4):
        hdic = make_dict("./ncbi_dataset/ace2_"+str(i+1)+".fasta")
        commonscs = []
        scs_vector = [0] * len(hdic.keys())
        hdic_keys = list(hdic.keys())
        for hkey in range(len(hdic_keys)):
            if hdic_keys[hkey] in target_dic.keys():
                scs_vector[hkey] = 1
                commonscs.append(hdic_keys[hkey])
        
        scs_distance = sum(scs_vector)

        print("commonscs = ",scs_distance)
        print(commonscs)
        print("-"*80)
        

path = "ncbi_dataset/alpha1.fasta"
mutant = "imput name:"

# refseq_keys,scs_distance = make_distance(path)

# print("refseq_scs_num:",refseq_keys)
# print(mutant,scs_distance)

h_distance(path)