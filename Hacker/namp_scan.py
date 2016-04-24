# !/usr/bin/env python
# coding = utf-8
__author__ = 'Administrator'

import nmap
import optparse


def namp_scan(tgthost, tgtport):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(tgthost, tgthost)
    state = nm_scan[tgthost]['tcp'][int(tgtport)]['state']
    print('[+]' + tgthost + ' tcp/' + tgthost + ' ' + state)


def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgthost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtport', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgthost = options.tgthost
    tgtports = str(options.tgtport).split(',')
    if (tgthost is None) or (tgtports == ['None']):
        print('[-] You must specify a target host and port[s].')
        exit(0)
    namp_scan(tgthost, tgtports)

if __name__ == '__main__':
    main()
