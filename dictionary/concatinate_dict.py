"""
Write a Python program to concatenate following dictionaries to create a new one.
"""
dic1={1:100, 2:200}
dic2={3:300, 4:400}
dic3={5:500,6:600}

final_dict = {}
# for i in(dic1, dic2, dic3):
#     final_dict.update(i)

#OR----------------
#using list comprehension
[final_dict.update(i) for i in(dic1, dic2, dic3)]
print(final_dict)

