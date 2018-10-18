'''
定义一个学生类
'''
#定义一个空类
class  Student():
    pass

#定义一个对象
mingyue = Student()

# 定义一个听Python的学生
class PythonStudent():
    #用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    #学生的行为
    def doHomework(self):
        print("I'm doing homework!")
        # 推荐在函数末尾使用return语句
        return None

#对象实例化
yueyue = PythonStudent()
yueyue.name = "YUEYUE"
# 注意成员函数的调用没有显示传递参数self
yueyue.doHomework()

print(yueyue.name)
print(yueyue.age)
