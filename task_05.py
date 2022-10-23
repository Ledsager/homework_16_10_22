# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
import re

filename1 = "polinomial2.txt"
filename2 = "polinomial1.txt"

with open(filename1,'r') as file1:
    string1 = file1.readline()
    lst1 = [i for i in re.split('[ ]+', string1)]
    # print(lst1,string1)

with open(filename2) as file2:
    string2 = file2.readline()
    lst2 = [i for i in re.split('[ ]+', string2)]
    # print(lst2,string2)

# lenght_max=max(len(lst1),len(lst2))
# print(lenght_max)
# for i in lst1:
#     temp_lst1=[i for i in i.split('x')]
#     print (temp_lst1)
#     for j in lst2:
#         temp_lst2=[j for j in j.split('x')]
#         print (temp_lst2,',',j)
       
def stepen(lst_temp):
    mas=[]
    c=''
    lst_temp=lst_temp.replace("=0","")
    print(lst_temp)
    for i in range(len(lst_temp)):
        a=int(lst_temp.find('x'))
        mas.append(lst_temp[0:a])
        
        if lst_temp[a+1]=='^':
            j=2
            while(lst_temp[a+j]!='-') or (lst_temp[a+j]!='+'):
                c=c+lst_temp[a+j]
                j+=1
            mas.append(c)


        

        print(a,' ',mas)
    # lst_temp = [i for i in re.split('[=|0]+', lst_temp)]
    return lst_temp
    pass

# print(stepen(string1))
# print(stepen(string2))

# print(lst1,string1)
# print(lst2,string2)
