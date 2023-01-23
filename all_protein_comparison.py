import pickle
import re
import csv

def make_list(path):
    with open(path, "r", encoding="utf8", errors='ignore') as f:
        l = []
        annotation_l =[]
        sub_l = ""
        for align in f:
            if ">" not in align:      
                align = align.strip()
                sub_l += align
            else:
                annotation_l.append(align)
                l.append(sub_l)
                sub_l = ""

        l.append(sub_l)
        l.pop(0)

    return annotation_l, l

def count_scs(l,scs_length=5):
    d = {}
    scs = scs_length
    for sub in l:
        for i in range(len(sub) - scs + 1):
            if sub[i:i+scs] not in d.keys():
                d[sub[i:i+scs]] = 1
            else:
                d[sub[i:i+scs]] += 1

    return d


with open("mizuno_add.csv","r") as f:
    reader = csv.reader(f)
    count = 0
    protein_list = []
    for row in reader:
        if count == 0:
            first_column = row
            count += 1
            break
            # continue
    #     protein_list.append(row[0])
    # with open("protein_list.pickle","wb") as f2:
    #     pickle.dump(protein_list,f2)
        
with open("protein_list.pickle","rb") as f:
    protein_list = pickle.load(f)

annotation_l,human_l = make_list("../protein.faa")
hdic = count_scs([human_l[0]])
_,clist = make_list("/Users/e185714/k22research/workplace/program/ncbi_dataset/reference/sequence.fasta")

main = []
scs = 5
for p in protein_list:
    sub = []
    isoform = 0
    length = 0
    commonscs = 0
    for an in range(len(annotation_l)):
        if p in annotation_l[an]:
            isoform += 1
            length += len(human_l[an])
            hdic = count_scs([human_l[an]])
            for i in range(len(clist[0])):
                c_scs = clist[0][i:i+scs]
                if c_scs in hdic.keys(): # 自己なら
                    commonscs += 1
    avg_length = length/isoform
    avg_commonscs = commonscs/isoform
    avg_scsaa = avg_commonscs/avg_length
    sub.append(p)
    sub.append(isoform)
    sub.append(avg_commonscs)
    sub.append(avg_length)
    sub.append(avg_scsaa)
    main.append(sub)

# print(main[0:5])
with open("refer_all_protein.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(first_column)
    for row in main:
        writer.writerow(row)

                            