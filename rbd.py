import re
import csv
import pickle



# とりあえず1つずつ
def def_rbd(type):
    if type == "refseq" or type == "gamma": # and gamma
        start = 330
        end = 521
    elif type == "omicron" or type == "alpha" or type == "beta": # and alpha, beta
        start = 327
        end = 518
    elif type == "delta":
        start = 328
        end = 519
    
    else:
        return print("typeはrefseq,omicronまたはdeltaです")


    return start, end


def p_load():
    with open("hdic.pickle","rb") as f:
        hdic = pickle.load(f)


def csv_nonself_count(path,type):
    start,end = def_rbd(type)
    rbd_length = end - start + 1 # 今後使うかも

    all_list = []
    all_rbd_list = []
    nonself_num_list = []
    rbd_nonself_list = []
    nonself_place_list = []
    rbd_nonself_place_list = []
    with open(path,"r") as f:
        read = csv.reader(f)
        all_aa = ""
        rbd_aa = ""
        nonself_num = 0
        rbd_nonself_num = 0
        nonself_place = []
        rbd_nonself_place = []
        for row in read:
            aa_num = row[0].split("-")

            #ここでリセット
            if int(aa_num[-1]) == 1:
                all_list.append(all_aa)
                all_rbd_list.append(rbd_aa)
                nonself_num_list.append(nonself_num)
                rbd_nonself_list.append(rbd_nonself_num)
                nonself_place_list.append(nonself_place)
                rbd_nonself_place_list.append(rbd_nonself_place)

                all_aa = ""
                rbd_aa = ""
                nonself_num = 0
                rbd_nonself_num = 0
                nonself_place = []
                rbd_nonself_place = []

            all_aa += row[2]
            

            if start <= int(aa_num[-1]) < end:
                if int(row[1]) == 1:
                    rbd_nonself_num += 1
                    rbd_nonself_place.append(int(aa_num[-1]))

                rbd_aa += row[2]
            else:
                if row[1].isdecimal() == True:
                    if int(row[1]) == 1:
                        nonself_num += 1
                        nonself_place.append(int(aa_num[-1]))

        
        all_list.append(all_aa)
        all_rbd_list.append(rbd_aa)
        nonself_num_list.append(nonself_num)
        rbd_nonself_list.append(rbd_nonself_num)
        nonself_place_list.append(nonself_place)
        rbd_nonself_place_list.append(rbd_nonself_place)

        all_list.pop(0)
        all_rbd_list.pop(0)
        nonself_num_list.pop(0)
        rbd_nonself_list.pop(0)
        nonself_place_list.pop(0)
        rbd_nonself_place_list.pop(0)

        # print(nonself_num_list)
        # print(rbd_nonself_list)
        # print(nonself_place_list)
        print(rbd_nonself_place_list[0])
    
    
csv_nonself_count("./csv/refseq.csv","refseq")
    

            
        
            
