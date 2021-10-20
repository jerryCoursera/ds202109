#***--- 1.5 ---***
# str_a = "you need python"
# print("original string：%s" % str_a)
# parsed_words = str_a.split(" ")
# print("splited words：%s" % parsed_words)
#
# left_sequence = str_a[::2]
# print("from left to right：%s" % left_sequence )
# right_sequence = str_a[::-2]
# print("from right to left：%s" % right_sequence )
# reverse_sequence = str_a[::-1]
# print("reverse：%s " % reverse_sequence )

#***--- 1.6 ---***
# english_name = "jerry"
# print("my name is: {}, type is: {}, length is: {}".format(english_name, type(english_name), len(english_name)))
#
# age = 18
# print("{}{}".format(english_name,age))
#
# hello = " hello "
# trimed_hello = hello.strip(" ")
# print(trimed_hello)
#
#
# org_string = "you need python"
# replaced_str = org_string.replace(" ", "*")
# print("original string: {}, replace string: {}".format(org_string, replaced_str))
#
# print("{} {} {} {}".format("you", "are", "very", "good"))
#

#***--- 1.7 ---***
# lst = list("python")
# print(lst)
# lst.extend(list("good"))
# print(lst)
# lst.sort()
# print(lst)
# h_index = lst.index("h")
# print("index of 'h': %s" % h_index)
# removed_str = list(set(lst))
# print("remove duplicated: %s" % removed_str)


# #***--- 1.8 ---***
# a = tuple("python")
# b = list(a)[:-1]
# print(" the last letter of string is: %s" % b[-1])

# #***--- 1.9 ---***
# my_dict = {"A": 90, "B": 85, "C": 80, "D":100 , "E":99 }
# while True:
#     q = input("enter name(A or B or C or D or E):")
#     if q in my_dict.keys():
#         print("scord of %s is: %s" % (q, my_dict[q]))
#     else:
#         print("you entered wrong name!")

# print(" the last letter of string is: %s" % b[-1])

# #***--- 1.10 ---***
# a=100
# b=150
# print("a: {}, b: {}".format(a,b))
# print ("a==b: {}".format(a==b))
# print ("a!=b: {}".format(a!=b))
# print ("a<b: {}".format(a<b))
# print ("a<=b: {}".format(a<=b))

# a={1,2,3,4,5,6,7,8}
# b= {2,3,4,6,8,0}
# print(a)
# print(b)
#
# a_and_b = a & b
# print("a interset b: %s" % a_and_b)
#
# a_plus_b = a | b
# print("a union b: %s" % a_plus_b)
#
#
# a_minus_b = a - b
# print("a - b: %s" % a_minus_b)
#
#
# b_minus_a = b - a
# print("b - a: %s" % b_minus_a)



# #***--- 1.11 ---***
# a = "right"
# if str(a).isnumeric():
#     b = float(a)* 10
#     print(b)
# else:
#     b = a + "@python"
#     print(b)
#
# a = "right_"
# if str(a).isnumeric():
#     b = float(a)* 10
#     print(b)
# else:
#     b = a + "@python"
#     print(b)
#
# a = "123"
# if str(a).isnumeric():
#     b = float(a)* 10
#     print(b)
# else:
#     b = a + "@python"
#     print(b)


# #***--- 1.12 ---***
# d={'book': ['python', 'datascience'], 'author': 'laoqi','publisher': 'phei'}
# print(d)
# d_rev = {}
# for k in d.keys():
#     d_rev[d[k]] = k
# print(d_rev)

# a='Life is short You need python'
# a_upper = a.upper().split(" ")
# a_lower = a.lower().split(" ")
# a_size = [len(x) for x in a.split(" ")]
# print(a)
# print(a_upper)
# print(a_lower)
# print(a_size)

# #***--- 1.13 ---***
# result=[]
# for i in range(100,1001):
#     a = i // 100
#     b = (i - 100* a)//10
#     c = i-100* a - 10 * b
#     if a**3 + b**3 + c**3 == i:
#         result.append(i)
# print(result)

# #***--- 1.14 ---***

# names = list('ABCDE')
# english = [90,85,80,100,99]
# math = [70,75,90,98,99]
#
# my_dict = {names[i]: {"english": english[i], "math": math[i]} for i in range(len(names)) }
# print (my_dict)
#
# while True:
#     q = input("enter name(A or B or C or D or E):")
#     if q in my_dict.keys():
#         print("scord of %s is: %s" % (q, my_dict[q]))
#     else:
#         print("you entered wrong name!")

# names = list('ABCDE')
# english = [90,85,80,100,99]
# math = [70,75,90,98,99]
#
# my_dict = {names[i]: {"english": english[i], "math": math[i]} for i in range(len(names)) }
# print (my_dict)
#
# while True:
#     q1 = input("enter name(A or B or C or D or E):")
#     q1 = q1.strip(" ")
#     if q1 in my_dict.keys():
#         target = my_dict[q1]
#         q2 = input("enter subject(math or english):")
#         q2 = q2.strip(" ")
#         if q2 in target.keys():
#             print("{}'s score of {}:{}".format(q1, q2, target[q2]))
#         else:
#             print("sudent {} has no score of subject: {}".format(q1, q1))
#     else:
#         print("you entered wrong name!")


# names = list('ABCDE')
# english = [90,85,80,100,99]
# math = [70,75,90,98,99]
#
# my_dict = {names[i]: {"english": english[i], "math": math[i]} for i in range(len(names)) }
# good_students = []
# good_score = 85
# for my_item in my_dict.items():
#     if my_item[1]["english"] > good_score and my_item[1]["math"]> good_score:
#         print(my_item)
#         good_students.append(my_item[0])
# print("students with scores above 85: %s" % good_students)

# #***--- 1.15 ---***

# odd_list = [ i for i in range(100) if i % 2 == 1]
# assert not 13 in odd_list

# # #***--- 1.16 ---***
# def case_switch(word, case):
#     if case in list("Uu"):
#         return word.upper()
#     elif case in list ("Ll"):
#         return word.lower()
#     else:
#         raise Exception("parameter must be 1 of the 4 letters: U,u,L,l")
#
# my_word = "AbcdEfg"
# print("original word: %s" %my_word)
# print("upper case: %s" % case_switch(my_word, "u"))
# print("lower case: %s" % case_switch(my_word, "l"))
#
#
#
#
# def math_func(num_list, sign):
#     count = len(num_list)
#     if count == 0:
#         return None
#     if sign.lower() == "average":
#         return  sum(num_list) / count
#     if sign.lower() == "median":
#         sorted_nums = sorted(num_list)
#         if count % 2 == 1:
#             return sorted_nums[(count+1)/2]
#         else:
#             i = count // 2
#             result = (sorted_nums[i] + sorted_nums[i-1])/2
#             return result
#     raise Exception("wrong parameters!")
#
# my_list = [5,10,220, 300,500,323]
# print("numbers: %s" % my_list)
# result = math_func(my_list, "average")
# print("average: %s" %result)
# result = math_func(my_list, "median")
# print("median: %s" % result)


# #***--- 1.17 ---***
# import random
# nums = []
# for i in range(10000):
#     nums.append(random.random() * 10000)
# avg_val = sum(nums)/10000
# print(avg_val)
# std_val = (sum([(x -avg_val)**2 for x in nums])/10000) **0.5
# print(std_val)
#
#
# def distance(pt1,pt2):
#     result = ( (pt1["x"]-pt2["x"])**2 + (pt1["y"]-pt2["y"])**2)**0.5
#     return result
# pt1 = {"x":0,"y":0}
# pt2 = {"x": 3, "y":4}
# dis = distance(pt1,pt2)
# print(dis)
#
# def findMatchingLetter(str, source):
#     str_list = list(str.upper())
#     str_found = []
#     for i in str_list:
#         if i in source:
#             str_found.append(i)
#     return str_found
#
# source = set("ACEGIKMOQSUWY")
# str = "apple"
# result = findMatchingLetter(str, source)
# print("string: '{}' has the following letters {} in letter set: {}".format(str,result,source))
# #***--- 1.18 ---***

# def changeName_a():
#     name = 'a'
#     def changeName2():
#         name = 'b'
#     return name
#
# print(changeName_a())

# def changeName_b():
#     name = 'a'
#     def changeName2():
#         nonlocal name
#         name = 'b'
#     changeName2()
#     return name
#
# print(changeName_b())

# #***--- 1.19 ---***
#
# x=lambda *vals: max(vals)
# print(x(1,2,3,4,5))
#
# nums = list(range(2,101))
# def check_prime(v):
#     if v == 2: return v
#     for i in range(2,v-1):
#         if v % i == 0:
#             return None
#     return v
#
# map_result = map(lambda x: check_prime(x), nums)
# result = list(set(map_result))
# if None in result: result.remove(None)
# print(result)
# print(len(result))
#
# from functools import reduce
# nums = [0] + list(range(2,100))
# result = reduce(lambda x,y: x + 1 if check_prime(y) is not None else x, nums)
# print("prime numbers total between [2,100]: %s" % result)
#

import re

def valid_pwd(pwd):
    result = True
    if pwd.startswith(" "):
        result = False
        print("invalid password! can not start with blank space!")
    if len(pwd) < 8:
        result = False
        print("invalid password! must >= 8 letters and numbers!")

    r = re.search('[A-Z]', pwd)
    if r is None:
        result = False
        print("invalid password! must include Upper case letter!")
    r = re.search('[a-z]', pwd)
    if r is None:
        result = False
        print("invalid password! must include lower case letter!")
    r = re.search('\d', pwd)
    if r is None:
        result = False
        print("invalid password! must include number!")

    return result

while True:
        my_pwd = input("please enter a password to check:")
        result = valid_pwd(my_pwd)
        print("{} password!".format("valid" if result else "invalid"))
