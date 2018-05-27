# day08

## 回顾

```shell
1.函数: 
2.调用函数: 函数名()
3.参数: 形式参数  实际参数
4.返回值: return
5.默认参数: 在定义函数时,尽量将默认参数放到最后边
6.不定长参数: *args  
7.关键字参数: **kw    实际调用  函数名('name' = '小明', 'age' = 23)
8.匿名函数: 变量名 = lambda 形式参数1,形式参数2:表达式
		调用:  变量名()
		
9.偏函数: import functools    
		functools.partical
作用:  将一些默认参数给固定住
10.回调函数: 在函数定义时, 形式参数一般传递的是函数名.
```

## 文件的操作

```python
重点
ft.open()
ft.read()
ft.write()
ft.readline()
ft.readlines()
ft.close()

作业:1.整理文件操作中open函数里边第二个参数.   表
	2.将上边每个函数的用法自己写例子整理并理解
```

## 作用域

```python
作用域:针对于变量 在函数中的使用情况
局部作用域:
函数作用域:(闭包以外的函数)
全局作用:(定义到整个文档中)
内建作用域:
  
# 要体现作用域
# 总结:在函数内部定义的变量无法在函数外部使用
# def func():
#     b = 20
#     print(b)
# func()
# print(b)

# 总结:在函数外部定义的变量可以在函数内部使用
# num1 = 30
# def func():
#     print('函数内部输出%d' % num1)
#     print(id(num1))
#
# func()
# print('函数外部输出%d' % num1)
# print(id(num1))


# 总结:这里并没有体现作用域,只是分别在函数外部和函数内容定义了相同名字的变量名而已
# num1 = 50
# def func():
#     num1 = 666
#     print('函数内部的值是%d' % num1)
#     print(id(num1))
#
# func()
# print('函数外部的值是%d' % num1)
# print(id(num1))


# 总结: 一旦在函数内部设置为global,则该变量全局有效
num1 = 100
def func():
    # 将num1变量声明为global,目的是为了方便在内部修改的变量同时可以作用于外部的变量
    global num1
    num1 = 888
    print('内部函数%d' % num1)9
    print(id(num1))

func()
print('外部函数%d' % num1)
print(id(num1))
```

