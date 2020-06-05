lst_num = [1,2,3,4,5,5,6,3,7,8,8]
set_num = set(lst_num)
set_result = set()
for i in set_num:
    if lst_num.count(i) >=2:
        print(i)                         
