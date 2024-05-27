# C
## 1.helloword
~~~c
#include <stdio.h>

int main (){
    printf("hello,word");
    return 0;
}

~~~
## 2.占位符
`%d`  期望printf可以输出数字
~~~c
//printf("%d",1)
//or
//printf("1+1=%d",1+1)
#include <stdio.h>
int main(){
    printf("%d",1);
    return 0;
}
~~~
## 3.变量和输入
~~~c
// int 数字变量
//scanf()用户输入

int a = 0
scanf("%d",&a) // 将用户输入的值重新复制给a

~~~