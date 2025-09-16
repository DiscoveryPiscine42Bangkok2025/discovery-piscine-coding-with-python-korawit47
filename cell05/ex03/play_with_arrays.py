ori_a = [2,8,9,48,8,22,-12,2]
ori_n = []
for i in ori_a:
    if i > 5:
        ori_n.append(i + 2)
    else:
        pass
arrynew = set(ori_n)
print(ori_a)
print(arrynew)