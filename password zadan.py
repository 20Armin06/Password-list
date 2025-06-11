import itertools
from itertools import*

def generate_pwd(txt,min,max):
    pwds=[]
    for len in range(min,max+1):
        for p in itertools.product(txt,repeat=len):
            pwds.append(''.join(p))
    return pwds

character=input("جناب هکر لطفا کرکتر های مد نظرتو وارد کن:")
min_len  =int(input("کمترین طول رمز را بگو"))
max_len  =int(input("بیشترین طول رمز را بگو"))
javab    =generate_pwd(character,min_len,max_len)

with open("pwds_list.txt","w")as file:
    for p in javab:
        file.write(p+"\n")
print("لیست رمز ها با موفقیت ساخته شد")