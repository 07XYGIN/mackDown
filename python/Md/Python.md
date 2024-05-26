# python

## 1.Hello,word!
~~~py
print('hello,word')
~~~

## 2.字符串(str)
### 2.1 字符串的大小写
~~~py
#1.首字母大写
name = 'title'.title()
#2. 字符串全部大写
name = 'title'.upper()
#3. 全字母小写
name = 'title'.lower()
~~~
### 2.2 去除空白
~~~python
#1.去除末尾空白
name = 'title'.rstrip()
#2.去除头部空白
name = 'title'.lstrip()
#3.去除所有空白
name = 'title'.strip()
~~~
## 3.制表符

- `\t` 向前缩进
- `\n` 换行
## 4.列表
~~~py
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
~~~
