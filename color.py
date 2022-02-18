class Color:
	BLACK          = '\033[30m'#(文字)黒
	RED            = '\033[31m'#(文字)赤
	GREEN          = '\033[32m'#(文字)緑
	YELLOW         = '\033[33m'#(文字)黄
	BLUE           = '\033[34m'#(文字)青
	MAGENTA        = '\033[35m'#(文字)マゼンタ
	CYAN           = '\033[36m'#(文字)シアン
	WHITE          = '\033[37m'#(文字)白
	COLOR_DEFAULT  = '\033[39m'#文字色をデフォルトに戻す
	BOLD           = '\033[1m'#太字
	UNDERLINE      = '\033[4m'#下線
	INVISIBLE      = '\033[08m'#不可視
	REVERCE        = '\033[07m'#文字色と背景色を反転
	BG_BLACK       = '\033[40m'#(背景)黒
	BG_RED2        = '\033[48;2;255;0;0m'
	BG_RED         = '\033[41m'#(背景)赤
	BG_GREEN       = '\033[42m'#(背景)緑
	BG_GREEN2      = '\033[48;2;51;204;102m'#(背景)緑
	BG_YELLOW      = '\033[43m'#(背景)黄
	BG_YELLOW2     = '\033[48;2;251;224;0m'#(背景)黄
	BG_BLUE        = '\033[44m'#(背景)青
	BG_MAGENTA     = '\033[45m'#(背景)マゼンタ
	BG_CYAN        = '\033[46m'#(背景)シアン
	BG_WHITE       = '\033[47m'#(背景)白
	BG_DEFAULT     = '\033[49m'#背景色をデフォルトに戻す
	RESET          = '\033[0m'#全てリセット

#print(f'{Color.BG_MAGENTA}A{Color.RESET}')
#print(f'黒:{Color.BLACK}●ABC{Color.RESET}')
#print(f'赤:{Color.RED}●ABC{Color.RESET}')
#print(f'緑:{Color.GREEN}●ABC{Color.RESET}')
#print(f'黄:{Color.YELLOW}●ABC{Color.RESET}')
#print(f'青:{Color.BLUE}●ABC{Color.RESET}')
#print(f'マゼンタ:{Color.MAGENTA}●ABC{Color.RESET}')
#print(f'シアン:{Color.CYAN}●ABC{Color.RESET}')
#print(f'白:{Color.WHITE}●ABC{Color.RESET}')
#print(f'下線:{Color.UNDERLINE}●ABC{Color.RESET}')
#print(f'太字:{Color.BOLD}●ABC{Color.RESET}')
#print(f'不可視:{Color.INVISIBLE}●ABC{Color.RESET}')
#print(f'反転:{Color.REVERCE}●ABC{Color.RESET}')
#print(f'背景黒:{Color.BG_BLACK}●ABC{Color.RESET}')
#print(f'背景赤:{Color.BG_RED}●ABC{Color.RESET}')
#print(f'背景緑:{Color.BG_GREEN}●ABC{Color.RESET}')
#print(f'背景黄:{Color.BG_YELLOW}●ABC{Color.RESET}')
#print(f'背景青:{Color.BG_BLUE}●ABC{Color.RESET}')
#print(f'背景マゼンタ:{Color.BG_MAGENTA}●ABC{Color.RESET}')
#print(f'背景シアン:{Color.BG_CYAN}●ABC{Color.RESET}')
#print(f'背景白:{Color.BG_WHITE}●ABC{Color.RESET}')
#文字色と背景色を変える
#print(f'文字赤+背景緑:{Color.RED}{Color.BG_GREEN}●ABC{Color.RESET}')

def makeScsDictFromAminoSeq(scsDict, scsLength, aminoSeq):
    index = 0
    for amino in range(len(aminoSeq) - scsLength + 1):
        if aminoSeq[amino:(amino + scsLength)] not in scsDict: 
            scsDict[aminoSeq[amino:(amino + scsLength)]] = index
            index += 1

# 複数のタンパク質の時
def get_scs_multi(path):
    import csv
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

        return all_list, nonself_num_list, nonself_place_list

# タンパク質が1つの時
def get_seq(read):
    all_aa = ""
    # nonself_num = 0
    # nonself_place = []
    for row in read:
        aa_num = row[0].split("-")
        all_aa += row[2]
        # if row[1].isdecimal() == True:
        #     if int(row[1]) == 1:
        #         nonself_num += 1
        #         nonself_place.append(int(aa_num[-1]))
    
    return all_aa

import csv
# from email import header
target_path = "../csv/omicron/sequence-5.csv" # 変異株のcsvのパス
refseq_path = "../csv/refseq/sequences.csv" # refseqのパス

csv_file = open(target_path, "r", encoding="utf_8", errors="", newline="" )
csv_file_refSeq = open(refseq_path, "r", errors="", newline="", encoding='utf-8-sig')


f = list(csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True))
f_ref = list(csv.reader(csv_file_refSeq, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True))

scsDictRefSeq = {}
scsDictTargetSeq = {}

targetSeq = get_seq(f)
refSeq = get_seq(f_ref)

makeScsDictFromAminoSeq(scsDictTargetSeq, 5, targetSeq)           
makeScsDictFromAminoSeq(scsDictRefSeq, 5, refSeq)

nonself=0
# refseq
for row in f_ref:
    ID = row[0].split('-')
    if int(ID[0]) == 1:
        if (int(ID[1]) - 1) % 60 == 0: # 前のアミノ酸が60の倍数個なら
            print(F"\n{Color.RESET}{ID[1].rjust(4)}  ", end = "")
        if row[1] == '1': # nonselfなら
            nonself+=1
            if refSeq[int(ID[1]) - 1:int(ID[1]) + 4] not in scsDictTargetSeq: # targetのscs辞書にないなら
                print(F"{Color.BG_YELLOW2}{Color.BLACK}{row[2]}{Color.RESET}", end="")
            else: # targetのscs辞書にあるなら
                print(F"{Color.BG_GREEN2}{Color.BLACK}{row[2]}{Color.RESET}", end="")
        else: # selfなら
            if refSeq[int(ID[1]) - 1:int(ID[1]) + 4] not in scsDictTargetSeq: # targetのscs辞書にないなら
                print(F"{Color.BG_MAGENTA}{Color.BLACK}{row[2]}{Color.RESET}", end="")
            #if targetSeq[int(ID[1]) - 1:int(ID[1]) + 4] not in scsDictRefSeq:
            else:
                print(F"{Color.BLACK}{row[2]}", end='')
        if int(ID[1]) % 60 == 0: # このアミノ酸が60の倍数個なら
            print(F"  {Color.RESET}{ID[1].rjust(4)}", end="")
print("\n")
# print("\n",nonself)
nonself=0
# target
for row in f:
    ID = row[0].split('-')
    if int(ID[0]) == 1:
        if (int(ID[1]) - 1) % 60 == 0:
            print(F"\n{Color.RESET}{ID[1].rjust(4)}  ", end = "")
        if row[1] == '1':
            nonself+=1
            if targetSeq[int(ID[1]) - 1:int(ID[1]) + 4] not in scsDictRefSeq:
                print(F"{Color.BG_RED2}{Color.BLACK}{row[2]}{Color.RESET}", end="")
            else:
                print(F"{Color.BG_GREEN2}{Color.BLACK}{row[2]}{Color.RESET}", end="")
        else:
            ### 追加してみた
            if targetSeq[int(ID[1]) - 1:int(ID[1]) + 4] not in scsDictRefSeq: # refseqのscs辞書にないなら
                if len(f) - int(ID[1]) > 3: # とりあえず入れてみた
                    print(F"{Color.BG_CYAN}{Color.BLACK}{row[2]}{Color.RESET}", end="")
            #if targetSeq[int(ID[1]) - 1:int(ID[1]) + 4] not in scsDictRefSeq:
            else:
                print(F"{Color.BLACK}{row[2]}", end='')
        if int(ID[1]) % 60 == 0:
            print(F"  {Color.RESET}{ID[1].rjust(4)}", end="")

print("\n")
# print("\n",nonself)
csv_file.close()
csv_file_refSeq.close()