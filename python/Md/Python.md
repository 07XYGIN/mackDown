# python

## 1.Hello,word!

```py
print('hello,word')
```

## 2.字符串(str)

### 2.1 字符串的大小写

```py
#1.首字母大写
name = 'title'.title()
#2. 字符串全部大写
name = 'title'.upper()
#3. 全字母小写
name = 'title'.lower()
```

### 2.2 去除空白

```python
#1.去除末尾空白
name = 'title'.rstrip()
#2.去除头部空白
name = 'title'.lstrip()
#3.去除所有空白
name = 'title'.strip()
```

## 3.制表符

-   `\t` 向前缩进
-   `\n` 换行

## 4.列表

```py
list = ['first','second','three']
#在末尾添加
list.append('four')
#在指定地址添加
#<listName>.insert(_index,_object)
list.insert(0,'one')
#在指定地方删除
#del <listName>[_index]
del list[0]
#获取删除的元素
#<listName>.pop(_index)
delData = list.pop(1)
#删除列表内指定值
#<listName>.remove(_value)
list.remove('second')
#查看数组内元素个数
#len(listName)
len(list)
#列表的切片
#<listName>[n?,m?] 可选 n是起点  m是终点 某个值为空时默认从头开始 全部为空时则为整个列表
list[:,5]
```

## 5.元组

元组里面的元素不可修改

```python
lists = (1,2,3)
lists[0] = 4 #error
lists = (4,2,3) #OK
```

## 6.条件判断

```py
# 1.与或非
and == &&
or == ||
! = !
# 2.特定的值未包含再列表
not in
# 3.if-elif-else
if :
    elif:
        else:
```

## 7.字典

```py
#0.
obj = {
    'name':'job',
    'age':10
}
print(obj['age'])
#1. 在字典中添加键值对
obj['set'] = "gril"
#2. 修改键值对
obj['set'] = 'woman'
#3. 删除键值对
del obj['set']
#4. 遍历字典
for key,value in obj.items():
    print(key,value)
#5.遍历字典中所有键
for key in obj.keys():
    print(key)
#5.1 遍历字典中的所有值
for values in obj.values():
    print(values)
#6. 按照某个顺序进行排列   for key in sorted('#顺序')
for key in sorted(obj.keys()):
    print(key)
```

## 8.类

```py
    # 类 一般为一类事物的统称,比如人类,动物 也可以细致划分。如男人,女人,猫,狗等
class People:
    #self 引用实例
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 可以对参数进行默认
        # 并没有在形参中书写isHappy
        self.isHappy = false
    def eat(self):
        return self.name  + '\n'+ 'eat apple'

    # 使用类
    zhangsan = People('zhangsan', 18)
    eat = zhangsan.eat()
```
