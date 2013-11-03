# -*- coding: utf-8 -*-

'''
Created on 2013/10/28

@author: Yi
'''
import urllib, urlparse
import thread
import socket
import time

class player:
    username = ''
    token = ''
    point = 0
    guess = 0
    conn = None
    timeout = 0
    roundCount = 0
    def __init__(self, conn):
        self.username = ''
        self.token = ''
        self.point = 0
        self.guess = 0
        self.conn = conn
    def submit(self, guess):
        req = {
               'cmd': 'submit',
               'point': str(guess)
               }
        self.conn.send(urllib.urlencode(req))
    def query(self):
        req = {
               'cmd': 'query'
               }
        self.conn.send(urllib.urlencode(req))
    def newPlayer(self, username):
        req = {
               'cmd': 'newplayer',
               'username': username
               }
        self.conn.send(urllib.urlencode(req))
        
    
def getPara(d, p):
    if d.has_key(p):
        return d[p][0]
    return None

def dealWithServer(conn, p):
    while True:
        buf = conn.recv(1024)
        d = urlparse.parse_qs(buf)
        cmd = getPara(d, 'cmd')
        if cmd == 'newround':
            timeout = getPara(d, 'timeout')
            count = getPara(d, 'count')
            yourpoint = getPara(d, 'yourpoint')
            p.timeout = int(timeout)
            p.roundCount  = int(count)
            p.point = int(yourpoint)
            print 'newround, timeout:',timeout
        elif cmd == 'confirmplayer':
            username = getPara(d, 'username')
            token = getPara(d, 'token')
            p.username = username
            p.token = token
            print 'confirmplayer'
        elif cmd == 'confirmsubmit':
            point = getPara(d, 'point')
            p.guess = point
            print 'confirm submit'
        elif cmd == 'confirmquery':
            yourpoint = int(getPara(d, 'yourpoint'))
            lastg = getPara(d, 'lastg')
            lastwinner = getPara(d, 'lastwinner')
            p.point = yourpoint
            print 'Query result:\nyourpoint:', yourpoint, '\nlastG:', lastg, '\nlastWinner:', lastwinner, '\n'
            
if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9210))
    p = player(sock)
    thread.start_new_thread(dealWithServer, (sock, p))
    while True:
        time.sleep(1)
        print '1. newplayer\n2.submit\n3.query'
        cmd = raw_input('choice:')
        if cmd == '1':
            username = raw_input('username:')
            p.newPlayer(username)
        if cmd == '2':
            point = raw_input('point:')
            p.submit(int(point))
        if cmd == '3':
            p.query()
    