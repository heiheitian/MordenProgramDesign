# -*- coding: utf-8 -*-
import socket
import thread
import random
import hashlib
import urllib, urlparse
import time

connLock = 0
def sendMsg(conn, msg):
    while connLock == 1:
        continue
    connLock = 1
    conn.send(msg)
    connLock = 0

class player():
    username = ''
    token = ''
    point = 0
    guess = 0
    conn = None
    timeoutCount = 0
    def __init__(self, username, conn):
        self.username = username
        self.token = hashlib.md5(str(random.randint(1, 2**256))).hexdigest()
        self.point = 0
        self.timeoutCount = 0
        self.conn = conn
    def getToken(self):
        return self.token
    def win(self):
        self.point = self.point + 10
    def lose(self):
        self.point = self.point - 5
    def timeout(self):
        self.point = self.point - 10
        self.timeoutCount = self.timeoutCount + 1
    def submit(self, guess):
        self.guess = guess
    def getGuess(self):
        return self.guess
    def getUsername(self):
        return self.username
    def getPoint(self):
        return self.point
    def newRound(self, timeout, count):
        req = {
               'cmd': 'newround',
               'count': count,
               'timeout': str(timeout),
               'yourpoint': str(self.getPoint())
               }
        sendMsg(conn, urllib.urlencode(req))
        
class game():
    roundTime = 30
    lastWinner = ''
    lastLosers = []
    lastG = 0
    players = []
    waiting = 0
    roundCount = 0
    def __init__(self):
        self.roundTime = 5
    def newRound(self):
        print 'users:'
        for i in self.players:
            print i.getUsername(), i.point
        #compute G
        self.waiting = 0
        i = [i.getGuess() for i in self.players]
        if len(i) != 0:
            self.lastG = sum(i)*0.618/len(i)
        if len(self.players) > 0:
            minabs = abs(self.players[0].getGuess() - self.lastG)
            maxabs = abs(self.players[0].getGuess() - self.lastG)
        #calculate winner point
        for i in self.players[1:]:
            #calculate timeouts
            if i.getGuess == 0:
                i.timeout()
                if i.timeoutCount >= 3:
                    players.remove(i)
                continue
            if abs(i.getGuess() - self.lastG) < minabs:
                self.lastWinner = i.getUsername()
                minabs = abs(i.getGuess() - self.lastG)
            if abs(i.getGuess() - self.lastG) > maxabs:
                maxabs = abs(i.getGuess() - self.lastG)
            i.guess = 0
        #calculate losers
        self.lastLosers = [i.getUsername for i in self.players if abs(i.getGuess() - self.lastG) == maxabs]
        #add or minus points
        self.roundCount = self.roundCount + 1
        for i in self.players:
            if i.getUsername() == self.lastWinner:
                i.win()
            elif i.getUsername() in self.lastLosers:
                i.lose()
            i.newRound(self.roundTime, self.roundCount)
        self.waiting = 1
    def newPlayer(self, username, conn):
        t = player(username, conn)
        self.players.append(t)
        return t

def getPara(d, p):
    if d.has_key(p):
        return d[p][0]
    return None
def dealWithClient(conn, g):
    p = None
    while True:
        buf = conn.recv(1024)
        d = urlparse.parse_qs(buf)
        cmd = getPara(d, 'cmd')
        if (cmd == 'newplayer'):
            username = getPara(d, 'username')
            p = g.newPlayer(username, conn)
            req = {
                   'cmd': 'confirmplayer',
                   'username': username,
                   'token': p.getToken()
                   }
            sendMsg(conn, urllib.urlencode(req))
        elif (cmd == 'submit'):
            point = int(getPara(d, 'point'))
            print 'submit from ',p.getUsername(), 'point=',point
            p.submit(point)
            req = {
                   'cmd': 'confirmsubmit',
                   'point': point
                   }
            sendMsg(conn, urllib.urlencode(req))
        elif (cmd == 'query'):
            yourpoint = str(p.getPoint())
            lastg = str(g.lastG)
            lastwinner = g.lastWinner
            req = {
                   'cmd': 'confirmquery',
                   'yourpoint': yourpoint,
                   'lastg': lastg,
                   'lastwinner': lastwinner
                   }
            sendMsg(conn, urllib.urlencode(req))

def timer(g):
    while True:
        timeout = g.roundTime
        time.sleep(timeout)
        g.newRound()
        
if __name__ == '__main__':
    g = game()
    thread.start_new_thread(timer, (g, ))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 9210))
    sock.listen(5)
    while True:  
        conn,address = sock.accept()
        print 'New client connected.'
        thread.start_new_thread(dealWithClient, (conn, g))