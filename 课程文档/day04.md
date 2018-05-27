## day04

## 回顾

```puthon
1.Number    int  float   abs max  min  pow  round
			import random    import  math
			math.ceil   math.floor  math.modf  math.sqrt
			random.choice  random.random()                 		       random.randint(返回指定区间的随机数int)    		        random.uniform(返回指定区间的随机数float) 
2.String   单行:''  ""  
		   多行: ''''''   """"""
		   字符串的长度: len
		   提取字符串中的某个字符: str1[n]   下标是从0开始
		   转义字符: \     \n  \t \r    r'一堆字符串'
		   字符串的截取: str1[0:4]
		   				str1[:5]
		   				str1[3:]
		   				str[3:-3]
		   				str1[-5:]
		   				str1[:]
		   				str1[::-1]
		   				str1[::-2]
		    *+: 
		    格式化: %s   %d  %f   %c   %o   %x    						str.format(
		    字符串比较大小: 根据ASCII值的大小进行比较
		   
3.路径: 
4.网站协议组成部分:协议://域名:端口/文件路径?键1=值1&键2=值2
5.状态码: 100 发送消息   200 OK   成功   302: 临时重定向  403:  禁止访问    404: 找不到页面   500:服务器内部错误

0-9:  48-57
A-Z:   65-90
a-z:  97-122			
```

## 流程控制

```
顺序结构:
分支结构:
循环结构:
```

### 分支结构

```python
第一种:  if结构
  	格式:  if 表达式:
        		语句块
     执行流程:程序遇到if结构时,判断表达式的真假,如果为真,则执行语句块,否则结束if结构    
     表达式为假的情况: 0 '' None  False []  ()  {}
 第二种: ifelse结构
  	格式: if 表达式:
        	语句块1
          else:
            语句块2
         执行流程:程序执行到if结构,判断表达式的真假,如果为真,则执行语句块1,如果为假,则执行else中的语句块的内容
 第三种: if-elif-else
  	格式: if 表达式1:
        	语句块1
          elif 表达式2:
            语句块2
          elif 表达式3:
            语句块3
           else:
            语句块n
         执行流程:程序执行到if语句,判断表达式1的真假,如果为真,则执行语句1,否则判断表达式2的真假,如果为真,则执行表达式2,一次类推,直到最后一个表达式为假,就执行else里边的语句块n
  第四种: 嵌套
    if  表达式1:
      if 表达式2:
        语句块1
       else:
        语句块2
     else:
      	语句块3
```

### 循环结构

```
必不可少的三个条件:  初始值  循环条件  循环的次数
初始值:
while 表达式:
	循环体
	循环的次数
for in
```

### break和continue

```python
break: 跳过循环剩余部分,到达下一条语句
注意: 一般情况下用在for  while  if  结构里边
表示跳出整个循环结构

continue:跳过循环的剩余部分,开始新一轮循环
```

