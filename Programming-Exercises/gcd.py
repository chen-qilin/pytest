#coding:utf-8
'''
Created on Spet 11, 2013

@author: 
'''

'''
求正整数x、y的最小公倍数。
举例：
输入：2、3
返回：6
'''

class Demo:

    def gcd(self,x,y):
    #最大公因子
        if x < y:
            x,y = y,x
        while(y!=0):             
            x,y = y,x%y
        return x
    def lcm(self,x,y):
        #最小公倍数
        return x*y/self.gcd(x,y)

if __name__ == '__main__':
    a=Demo()
    print a.gcd(300,35)
    print a.lcm(30,10)
