# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
import re

filename1 = "polinom.txt"
filename2 = "polinomial.txt"

with open(filename1,'r') as file1:
    string1 = file1.readline()
    lst1 = [i for i in re.split('[x]+', string1)]
    print(lst1,string1)

with open(filename2) as file2:
    string2 = file2.readline()
    lst2 = [i for i in re.split('[x]+', string2)]
    print(lst2,string2)

lenght_max=max(len(lst1),len(lst2))
print(lenght_max)
for i in lst1:
    temp_lst1=[i for i in i.split('x')]
    print (temp_lst1)
    for j in lst2:
        temp_lst2=[j for j in j.split('x')]
        print (temp_lst2,',',j)
       

        