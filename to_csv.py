import os




# 改行文字の処理
def make_list(path):
    with open(path, "r", encoding="utf8", errors='ignore') as f:
        l = []
        sub_l = ""
        for align in f:
            if ">" not in align:      
                align = align.strip()
                sub_l += align
            else:
                l.append(sub_l)
                sub_l = ""

        l.append(sub_l)
        l.pop(0)

    return l

# scsの出現回数を数える
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

# 1番多いのはHTGEKで18073回出現
# keys = [k for k,v in d.items() if v == 18073]



#実質main
def write_csv():
    DataPath = "./protein.faa"
    CDataPath = "./ncbi_dataset/"
    writePath = "./"

    scs = 5
    # ヒト
    hlist = make_list(DataPath)
    hdic = count_scs(hlist)

    fn = os.listdir(CDataPath)
    for f_path in fn:
        clist = make_list(CDataPath + f_path)
        # sp_name = f_path.split("_")
        sp_name = f_path.split(".")
        with open(writePath + sp_name[0] + ".csv", "w") as f:
            for i in range(len(clist)):
                for ii in range(len(clist[i])):

                    if ii < (len(clist[i]) - scs + 1):
                        c_scs = clist[i][ii:ii+scs]
                        ifself = 0  # 自己非自己変数
                        if c_scs in hdic.keys(): # 自己なら
                            ifself = 0
                        else:
                            ifself = 1

                        try:
                            f.write("{0}-{1},{2},{3},{4}\n".format(i+1,ii+1,ifself,clist[i][ii],hdic[c_scs]))
                        except KeyError:
                            f.write("{0}-{1},{2},{3},{4}\n".format(i+1,ii+1,ifself,clist[i][ii],0))
                    else:
                        f.write("{0}-{1},{2},{3},{4}\n".format(i+1,ii+1,"-",clist[i][ii],"-"))

write_csv()