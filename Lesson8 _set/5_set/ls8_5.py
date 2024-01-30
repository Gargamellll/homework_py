#5.You are given three lists, list1, list2, and list3. Your task is to implement a
#programm that takes these lists and prints the following:
# The set of elements that are common to all three lists.
# The set of elements that are present in at least two of the three lists, but not in all
# three.
# The set of elements that are unique to each list (present in only one list):


list_1=['acknowledge']
list_2=['astonishing']
list_3=['amazing']
x=set(list_1)
y=set(list_2)
a=set(list_3)
set_result1=[x & y & a]
set_result2=list(x|y|a)
set_result3=list(x-y-a)
print(set_result1,
set_result2,
set_result3)


# list_1=set('acknowledge')
# list_2=set('astonishing')
# list_3=set('amazing')
# for letter in list_1,list_2,list_3:
# print(list_1 & list_2 & list_3)
# print(list_1 | list_2 - list_3)
# print([list_2-list_3-list_1,list_1-list_3,list_3-list_1-list_2])