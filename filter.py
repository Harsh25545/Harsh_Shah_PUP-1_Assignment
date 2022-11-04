test_list = [1,2,3,-8,9,6,-3,4]
#printing original list
print("The original list is :"+str(test_list))
#Remove nagative element
res=[ele for ele in test_list if ele > 0]
print("List after filtering:"+str(res))
list1=[12,3,45,5,66,90,67,89]
list2=list(filter(lambda x: x % 2==1,list1))
print(list2)
str1="Winter olympic in 2022 will take place in Beijing China"
list=list(filter(lambda x: True if x.lower() in "aeiou"else False,str1))
print(list)