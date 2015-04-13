#!/usr/bin/env python
'''
Created on 2015-4-13

@author: cWX200549
'''
import cgi

reshtml = '''Content-Type: text/html\n
<HTML>
    <HEAD>
        <TITLE>
            Friends CGI Demo(dynamic screen)
        </TITLE>
    </HEAD>
    <BODY>
        <H3>
            Friends list for:<I>%s</I>
        </H3>
        Your name is:<B>%s</B><P>
        you have <B>%s</B> friends.
    </BODY>
</HTML>'''

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print reshtml % (who, who, howmany)
