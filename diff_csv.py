compare_1 = []
# 自分
with open("./B_B_Omicron_dd.csv", "r", encoding="utf8", errors='ignore') as f:
    for align in f:
        rp_align = align.replace("\n","")
        sp_1 = rp_align.split(",")
        # print(sp_1[:3])
        compare_1.append(sp_1[:3])

compare_2 = []
# 先輩
with open("./another_omicron.csv", "r", encoding="utf8", errors='ignore') as f:
    for align in f:
        rp_align = align.replace("\n","")
        sp_2 = rp_align.split(",")
        # print(sp_2[:3])
        compare_2.append(sp_2[:3])

compare = []
# for com1 in compare_1:
#     for com2 in compare_2:
#         if com1 == com2:
#             compare.append(com2)

for com2 in compare_2:
    for com1 in compare_1:
        if com1 == com2:
            # print(com1)
            compare.append(com1)

if compare == compare_2:
    print("ok")
else:
    print(len(compare))
    print(len(compare_2))
    print("だめ")

# for i in range(11886,len(compare_2)):
#     if compare[i] != compare_2[i+1]:
#         print(i)
#         print(compare[i])
#         print(compare_2[i+1])
#         break

