#!/usr/bin/env python
# coding = utf-8
__author__ = 'chen_qilin'

from cgi import FieldStorage
from os import environ
from cStringIO import StringIO
from urllib import quote,unquote
from string import capwords, strip, split, join


class AdvCGI(object):
    header = 'Content-Type: text\html\n'
    url = '/cgi-bin/advcgi.py'

    formhtml = '''
    <HTML>
        <HEAD>
            <TITLE>Friends CGI Demo</TITLE>
        </HEAD>
        <BODY>
            <H2>Advanced CGI Demo Form</H2>
            <FORM METHOD=post ACTION='%s' ENCTYPE='multipart/form-data'>
                <H3>Cookie Setting</H3>
                <L1><CODE><B>CPPuser=%s</B></CODE>
                <H3>Enter cookie value<BR>
                <INPUT NAME=cookie value=%s>(<I>optional</I>)</H3>
                <H3>Enter your name<BR>
                <INPUT NAME=person value=%s>(<I>optional</I>)</H3>
                <H3>What languages can you program in?
                (<I>at least one required</I>)</H3>
                %s
                <H3>Enter file to upload</H3>
                <INPUT TYPE=file NAME=upfile VALUE='%s' SIZE=45>
                <P><INPUT TYPE=submit>
            </FORM>
        </BODY>
    </HTML>'''
    
    langSet = ('Python', 'PERL', 'Java', 'C++', 'PHP', 'C', 'JavaScript')
    langItem = "<INPUT TYPE=checkbox NAME=lang VALUE='%s'%s>%s\n"

    def getCPPCookies(self):
    #read cookies from client
        if environ.has_key('HTTP_COOKIE'):
            for eachCookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
                if len(eachCookie) > 6 and eachCookie[:3] == 'CPP':
                    tag = eachCookie[3:7]
                try:
                    self.cookies[tag] = eval(unquote(eachCookie[8:]))
                except (NameError, SytaxError):
                    self.cookies[tag] = unquote(eachCookie[8:])
        else:
            self.cookies['info'] = self.cookies['user'] = ''

        if self.cookies['info'] != '':
            self.who, langStr, self.fn = split(self.cookies['info', ':'])
            self.langs = split(langStr, ',')
        else:
            self.who = self.fn = ''
            self.langs = ['Python']
