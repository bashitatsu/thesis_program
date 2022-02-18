import pickle
import numpy as np

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
        # print(protein)

    return l

def count_scs(l):
    d = {}
    scs = 6
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
    with open("../ncbi_dataset/refseq/refseq_dic.pickle", "rb") as f:
        refseq_dic = pickle.load(f)
    return refseq_dic

def hdic_load():
    with open("../hdic.pickle", "rb") as f:
        hdic = pickle.load(f)
    return hdic

def make_distance(path1,path2):
    target1_dic = make_dict(path1)
    target1_key = list(target1_dic.keys())
    target2_dic = make_dict(path2)
    target2_key = list(target2_dic)
    refseq_dic = p_load()
    refseq_key = list(refseq_dic.keys())

    scs_vector1 = [0] * len(refseq_key)
    scs_vector2 = [0] * len(refseq_key)

    for refseqkey in range(len(refseq_key)):
        if refseq_key[refseqkey] in target1_key:
            scs_vector1[refseqkey] = 1
        if refseq_key[refseqkey] in target2_key:
            scs_vector2[refseqkey] = 1

    vec1 = np.array(scs_vector1)
    vec2 = np.array(scs_vector2)
    vec12 = vec1 & vec2
    return sum(vec12)

def make_distance_34(path1,path2,refseq):
    target1_dic = make_dict(path1)
    target1_key = list(target1_dic.keys())
    target2_dic = make_dict(path2)
    target2_key = list(target2_dic)
    refseq_dic = refseq
    refseq_key = list(refseq_dic.keys())

    scs_vector1 = [0] * len(refseq_key)
    scs_vector2 = [0] * len(refseq_key)

    for refseqkey in range(len(refseq_key)):
        if refseq_key[refseqkey] in target1_key:
            scs_vector1[refseqkey] = 1
        if refseq_key[refseqkey] in target2_key:
            scs_vector2[refseqkey] = 1

    vec1 = np.array(scs_vector1)
    vec2 = np.array(scs_vector2)
    vec12 = vec1 & vec2
    return sum(vec12)


# ヒトベース、refseqと変異株
def h_sars(path):
    # ヒト
    hdic = hdic_load()
    h_key = list(hdic.keys())
    # refseq
    refseq_dic = p_load()
    refseq_key = list(refseq_dic.keys())
    scs_vector1 = [0]*len(h_key)
    # 変異株
    mutant_dic = make_dict(path)
    mutant_key = list(mutant_dic.keys())
    scs_vector2 = [0]*len(h_key)

    for hkey in range(len(h_key)):
        if h_key[hkey] in refseq_key:
            scs_vector1[hkey] = 1
        if h_key[hkey] in mutant_key:
            scs_vector2[hkey] = 1

    vec1 = np.array(scs_vector1)
    vec2 = np.array(scs_vector2)
    vec12 = vec1 & vec2
    print(sum(vec12))


def sars_sars(path1,path2):
    # ヒト
    hdic = hdic_load()
    h_key = list(hdic.keys())
    # refseq
    refseq_dic = make_dict(path1)
    refseq_key = list(refseq_dic.keys())
    scs_vector1 = [0]*len(h_key)
    # 変異株
    mutant_dic = make_dict(path2)
    mutant_key = list(mutant_dic.keys())
    scs_vector2 = [0]*len(h_key)

    for hkey in range(len(h_key)):
        if h_key[hkey] in refseq_key:
            scs_vector1[hkey] = 1
        if h_key[hkey] in mutant_key:
            scs_vector2[hkey] = 1

    vec1 = np.array(scs_vector1)
    vec2 = np.array(scs_vector2)
    vec12 = vec1 & vec2
    print(sum(vec12))

# path1 = "../ncbi_dataset/spike/alpha1.fasta"
# path2 = "../ncbi_dataset/spike/beta1.fasta"
# sars_sars(path1,path2)


protein = ["ORF1ab","ORF1a","スパイク","ORF3a","エンベロープ","膜タンパク質","ORF6","ORF7a","ORF7b","ORF8","ヌクレオカプシド","ORF10"]

refseqq = [7096,4405,1273,275,75,222,61,121,43,121,419,38]

refseq = make_dict("../ncbi_dataset/refseq/sequences.fasta")
for i in range(len(protein)):
    path1 = "../ncbi_dataset/alpha/sequence-"+str(i+1)+".fasta"
    path2 = "../ncbi_dataset/beta/sequence-"+str(i+1)+".fasta"

    scs_distance = make_distance_34(path1,path2,refseq)
    print(protein[i],"&",scs_distance,"&",round(scs_distance/refseqq[i],3),r"\\")
    print("\hline")
