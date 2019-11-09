#! /usr/bin/python3

from datetime import datetime
from twilio.rest import Client
import time

import threading

class Game(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Game, self).__init__(*args, **kwargs)

    class Node:
        a = None
        b = None
        c = None
        text = " "

        def __init__(self, text):
            self.text = text

        def setNodeA(self, node):
            self.a = node

        def setNodeB(self, node):
            self.b = node

        def setNodeC(self, node):
            self.c = node

    def runVote(objnode):

        begin_es = datetime.now()

        print(objnode.text, end="\n")

        time.sleep(10)

        a = 0
        b = 0
        c = 0

        for record in num_reply:
            if (num_reply[record] == '1'):
                a += 1
            elif (num_reply[record] == '2'):
                b += 1
            elif (num_reply[record] == '3'):
                c += 1

        sum = a + b + c

        print(sum, " people voted.\n");
        print("%0.2f" % (a / sum * 100), "% voted OPTION 1\n")
        print("%0.2f" % (b / sum * 100), "% voted OPTION 1\n")
        print("%0.2f" % (c / sum * 100), "% voted OPTION 1\n")

        if (a > b and a > c):
            return objnode.a
        elif (b > a and b > c):
            return objnode.b
        else:
            return objnode.c

    def run():

        node = Node("I")
        node.setNodeA(Node("am"))
        node.a.setNodeA(Node("dead"))
        node.a.setNodeB(Node("alive"))
        node.a.setNodeC(Node("drunk"))

        node.setNodeB(Node("have"))
        node.b.setNodeA(Node("herpes"))
        node.b.setNodeB(Node("nothing"))
        node.b.setNodeC(Node("everything"))

        node.setNodeC(Node("can"))
        node.c.setNodeA(Node("fly"))
        node.c.setNodeA(Node("poop"))
        node.c.setNodeA(Node("giggle"))

        curr = node

        while (curr is not None):
            curr = runVote(curr)
