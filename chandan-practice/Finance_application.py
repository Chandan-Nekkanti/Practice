from pathlib import Path
def dict_conv(x):
    diction = {}
    with open(fname, 'r') as file:
       
        for i in file:
            lst = i.split(',')
            ct = lst[1]
            z = ct[1:-1]
            diction.update({lst[0]:z})   
    print(diction)
    val = 0
    for x,y in diction.items():
        val += float(y)
    print("%.2f" % val)




fname = Path("/home/chandan-nekkanti/Practice/chandan-practice/Stock_data_smple - Sheet1.csv")
dict_conv(fname) 
