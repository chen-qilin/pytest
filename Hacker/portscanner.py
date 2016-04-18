# !/usr/bin/env python
# coding = utf-8

import optparse
from socket import *


def conn_scan(tgthost, tgtport):
    try:
        conn_skt = socket(AF_INET, SOCK_STREAM)
        conn_skt.connect((tgthost, tgtport))
        conn_skt.send(b'ViolentPython\r\n')
        results = conn_skt.recv(1024)
        print('[+] %d/tcp open' % tgtport)
        print('[+] ' + str(results))
        conn_skt.close()
    except Exception:
        print('[-] %d/tcp closed' % tgtport)


def port_scan(tgthost, tgtports):
    try:
        tgt_ip = gethostbyname(tgthost)
        print(1)
    except Exception:
        print("[-] Cannot resolve '%s': Unknown host" % tgthost)
        return None
    try:
        tgtname = gethostbyaddr(tgt_ip)
        print(2)
        print('\n[+] Scan Results for: ' + tgtname[0])
    except Exception:
        print(3)
        print('\n[+] Scan Results for:' + tgt_ip)
    setdefaulttimeout(20)
    for tgtport in tgtports:
        print('Scanning port ' + tgtport)
        conn_scan(tgthost, int(tgtport))


def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgthost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtport', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgthost = options.tgthost
    tgtport = str(options.tgtport).split(',')
    if (tgthost is None) | (tgtport == ['None']):
        print('[-] You must specify a target host and port[s].')
        exit(0)
    port_scan(tgthost, tgtport)

if __name__ == '__main__':
    main()
