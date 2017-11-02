a = [1,4,5,6,78,23,45,67,24,87,67,56,45,33,44,68,69]
print(a)
new_list = [n for n in a if n%2 == 0] 
print(new_list)


b = [3,4,5,6,7,2,6,7,834,67,34,2,4,4,5,6,6,7,2323,545,6,623,656,77,454,34]
new_list1 = []
for i in b:
 if(i%2 == 0 and i not in new_list1):
  new_list1.append(i)

print(new_list1)
