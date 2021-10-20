#***--- 2.1.1 ---***
#import numpy as np
#
# a = np.array([1,2,3,4,5])
# print(a)

# a='Life is short You need python'
# a_upper = a.upper().split(" ")
# a_lower = a.lower().split(" ")
# a_size = [len(x) for x in a.split(" ")]
# print("{:<12}: {}".format("original", a))
# print("{:<12}: {}".format("upper case", a_upper))
# print("{:<12}: {}".format("lower case", a_lower))
# print("{:<12}: {}".format("word size", a_size))

#***--- 2.1.2 ---***

# a = [180,215,210, 188,176, 209, 200]
#
# mod_result = [x%10 for x in a]
# print("{:<12}{}".format("org values:", a))
# print("{:<12}{}".format("mod values:", mod_result))
#
# import numpy as np
# a = np.array([180,215,210, 188,176, 209, 200])
# mod_result = np.mod(a, 10)
# print("{:<12}{}".format("org values:", a))
# print("{:<12}{}".format("mod values:", mod_result))
#***--- 2.1.3 ---***

# import numpy as np
# height_list = [89, 80, 78]
# np_height = np.array(height_list)
# print("{:<15}: {}".format("height(inch)", np_height))
# np_height_m = np_height * 0.0254
# print("{:<15}: {}".format("height(meter)",np_height_m))
# import numpy as np
# a = np.random.uniform(low = 0.0, high = 1000.0, size = 100)
# avg_a = np.average(a)
# print("average: %s" % avg_a)
#
# sorted_a = np.sort(a)
# median_a = np.median(sorted_a)
# print("median: %s" % median_a)
#
# print(np.linspace(1,16,10))
# print(np.eye(5, k = 1))
#***--- 2.1.4 ---***
# import numpy as np
# a = np.array([[3,6,9],[2,4,8],[1,4,7]])
# print("array is:\n {}".format(a))
# print("shape: {}".format(np.shape(a)))
# print("element in the middle: {}".format(a[1]))
# print("last column: {}".format(a[:,-1])) //print("last column: {}".format(a[:,2]))
# print("top 2 rows: {}".format(a[:2,:]))
# print("elements > 7: {}".format(a[a>7]))

#***--- 2.1.5 ---***

#***--- 2.1.6 ---***
#
# import numpy as np
#
# m1s = np.ones((9,9), dtype=int)
# r9 = np.array([1,2,3,4,5,6,7,8,9])
# result1 = m1s * r9
# #print(result1)
# #print(m1s * r9.reshape((9,1)))
# result2 = result1.T.dot(r9)
# result = result1.T * r9
# print(result)
# #
# c9_d =np.zeros((9,9))
# np.fill_diagonal(c9_d, range(1,10))
# cm_full = np.ones((9,9)).dot(c9_d)
# cm = np.tril(cm_full, k=0)
# result = cm
# m99 = r9.dot(cm)
# print(result)
# print(m99)
#
# s = np.array([1,2,3])
# a = s.reshape((3,1))
# b = s.reshape((1,3))
# print(a)
# print(b)
# print(a+b)
#
# a = np.arange(5)
# b= np.reshape(a,(2,3))
#***--- 2.1.7 ---***
#***--- 2.1.8 ---***
# import numpy as np
# a = np.zeros((2,3))
# b=a.ravel()
# print(a)
#***--- 2.1.9 ---***
# import numpy as np
#
# arrays = [np.random.randn(3, 4) for _ in range(10)]
# print (arrays)
# np.stack(arrays, axis=0).shape
# print (arrays)
#***--- 2.1.11 ---***
import numpy as np
a = np.matrix([[1,2,3],[2,1,1],[3,2,2]])
print("matrix:\n%s"%a)
b = np.linalg.inv(a)
print("inverse:\n%s"%b)
c = np.linalg.det(a)
print("det:\n%s"%c)
d=np.linalg.matrix_power(a,3)
print("matrix power:\n%s"%d)
rhs = np.array([15,20,30])
e = np.linalg.solve(a,rhs)
print("solve equation:\n%s"% e)




