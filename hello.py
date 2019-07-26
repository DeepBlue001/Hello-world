# # '''a = 3
# # b = 9.0
# # c = "lizhenhua"
# # print(a+b)
# # print(c)
# # print(c[1])
# # print(c[1:6:2])
# # list = ['runoob',786,2.23,'join',70.2]
# # print(list)
# # print(list[0])
# # print(list[1:3])
# # print(list[2:])
# # tinylist = [123,"john"]
# # print(tinylist*2)
# # print(list+tinylist)
# # list[2]='lizhenhua'
# # print(list)
# # tuple=('runoob',786,2.23,'join',70.2)
# # print(tuple)
# # dict ={}
# # dict['one']='this is one'
# # dict[2]='this is two'
# # print(dict)
# # tinydict={"name":"join",'code':6734,"dept":'sales'}
# # print(tinydict)
# # print(dict['one'])
# # print(tinydict.keys())
# # print(tinydict.values())
# # print(tinydict)
# # print(tinydict)
# # a=21
# # b=10
# # c=0
# # c=a+b
# # print('c的值为',c)
# # a=10
# # b=20
# # list1=[1,2,3,4]
# # if(a in list1):
# #     print("a在list1中")
# # else:
# #     print('a不在list1中')
# # if(b not in list1):
# #     print("b不在list1中")
# # else:
# #     print("b在list1中")
# # '''
# # a=1
# # while(a<10):
# #     print(a)
# #     a+=2
# # numbers=[12,27,5,42,8,3]
# # '''number=numbers[1]
# # print("number",number)
# # print(numbers)'''
# # even=[]
# # odd=[]
# # while len(numbers)>0:
# #     number=numbers.pop()
# #     if(number%2==0):
# #         even.append(number)
# #     else:
# #         odd.append(number)
# # print(numbers)
# # print(odd)
# # print(even)
# # # num=input("enter one number")
# # # print('num',num)
# # for letter in 'python':
# #     print('当前字母：',letter)
# # fruits=['banana','apple','mango']
# # for index in range(len(fruits)):
# #     print("当前水果",fruits[index])
# # print(range(len(fruits)))
# # print("asad%d,%sdaafds"%(21,'sad'))
# # list1=['phy','che',1997,2000]
# # print(list1)
# # del list1[2]
# # print('after')
# # print(list1)
# # dict1={"name":'zara','age':7,'class':"first"}
# # print(dict1)
# # print('after')
# # dict1['age']=8
# # dict1['school']='ustc'
# # print(dict1)
# # del dict1['name']
# # print(dict1)
# # dict1.clear()
# # print(dict1)
# # del dict1
# import time
#
# ticks = time.time()
# print("当前时间戳为：", ticks)
# localtime = time.localtime(time.time())
# print("本地时间为：", localtime)
# localtime1 = time.asctime(localtime)
# print("本地时间为:", localtime1)
# print(time.strftime("%Y=%m=%d %H-%M-%S", localtime))
# print(time.strftime("%a %b %d %H:%M:%S %Y", localtime))
# a="Sat Mar 28 22:24:24 2016"
# print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
# import calendar
# cal=calendar.month(2019,7)
# print("下面输出2019年7月的日历")
# print(cal)
def fun(str):
    print(str)
    return 12
print(fun(123))
print(fun("afdaf"))
print(123)
def prints(arg1,*var):
    print("输出")
    print(arg1)
    for i in var:
        print(i)
    return
print(111,"aaa","bbb","ccc","ddd")
sum=lambda arg1,arg2:arg1+arg2
print("相加后的值为：",sum(10,20))
