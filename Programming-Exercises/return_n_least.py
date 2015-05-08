#coding:utf-8
'''
输入一个数字列表，返回该列表最小的n项（n >= 1），并且返回列表中的数字从小到大排序
异常返回-1，当n>len(in_list)时，也视为异常
#输入：in_list(数字列表)，n(n项)
#输出：result(数字列表,从小到大排序)
def get_min_nums(in_list,n)
 #do something
 return result
'''
def get_min_nums(in_list,n):   
    result=-1 if len(in_list)<n or n<1 else [i for i in sorted(in_list)[:n]]
    return result

if __name__=='__main__':
    print get_min_nums([1,4,3,2],2)
