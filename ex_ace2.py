"""
ACE2(アンジオテンシン変換酵素2)には
angiotensin-converting enzyme 2 isoform 1 precursor
angiotensin-converting enzyme 2 isoform 2 precursor
angiotensin-converting enzyme 2 isoform 3 precursor
angiotensin-converting enzyme 2 precursor
の4つがあり、それぞれを抽出します
"""

with open("protein.faa","r",encoding="utf8", errors='ignore') as f:
    l = []
    protein_l = []
    sub_l = ""
    protein = ""
    for align in f:
        if ">" in align:
            if "angiotensin-converting enzyme 2" in protein:
                protein_l.append(protein)
                l.append(sub_l)
                sub_l = ""
            protein = align
        if "angiotensin-converting enzyme 2" in protein:
            if ">" not in align:
                align = align.strip()
                sub_l += align
            



# for i in range(4):
#     with open("ace2_"+str(i+1)+".fasta","w") as f:
#         f.write(protein_l[i])
#         f.write(l[i])
