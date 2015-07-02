#!/usr/bin/env python
# coding= utf-8
'''
Created on 
@author: chen-qilin
用途：将RF生成的自动化结果reporter.html文件中失败的用例，显示在新的文件中。
'''
import time

def show_fail_test():
    '''
          读取reporter.html的每一行，存入templist里用于分段过滤，
          当检测到</tr>并且不是pass的用例时，写入新的newf文件里。
    '''
    templist = []
    
    try:
        f = open('report.html', 'r')
    except IOError:
        print "打开文件失败，请将test.py和reporter.html放入同一目录下。"
        return None
    
    newf = open('failedreport.html', 'w')
    
    for eachline in f:
        if '<h2>Test Details by Tag</h2>' in eachline:
            break
        else:
            if '</tr>' in eachline :
                if '<td class="col_status pass">PASS</td>\n' in templist:
                    templist =[]
                    continue
                else:
                    newf.write(''.join(templist))
                    newf.write(eachline)
                    templist =[]
            else:
                templist.append(eachline)
    newf.write('</body>\n</html>')
    f.close()
    newf.close()
    
if __name__ == '__main__':
    print time.clock()
    show_fail_test()
    print time.clock()
    print 'done'
