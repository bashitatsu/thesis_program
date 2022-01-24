import re
import csv
import pickle

def p_load():
    with open("../hdic.pickle","rb") as f:
        hdic = pickle.load(f)


def csv_nonself_count(path,type):
    all_list = []
    nonself_num_list = []
    nonself_place_list = []
    with open(path,"r") as f:
        read = csv.reader(f)
        all_aa = ""
        nonself_num = 0
        nonself_place = []
        for row in read:
            aa_num = row[0].split("-")

            #ここでリセット
            if int(aa_num[-1]) == 1:
                all_list.append(all_aa)
                nonself_num_list.append(nonself_num)
                nonself_place_list.append(nonself_place)

                all_aa = ""
                nonself_num = 0
                nonself_place = []

            all_aa += row[2]
            if row[1].isdecimal() == True:
                if int(row[1]) == 1:
                    nonself_num += 1
                    nonself_place.append(int(aa_num[-1]))

        
        all_list.append(all_aa)
        nonself_num_list.append(nonself_num)
        nonself_place_list.append(nonself_place)

        all_list.pop(0)
        nonself_num_list.pop(0)
        nonself_place_list.pop(0)

        # print(nonself_num_list)
        # print(nonself_place_list)
        print(type,": ",len(nonself_num_list))
    
    
csv_nonself_count("../csv/orf1ab/delta.csv","refseq")
    

            
        
            
