#! /usr/bin/python3

# Download the helper library from https://www.twilio.com/docs/python/install
from datetime import datetime
from twilio.rest import Client
import time


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

class Node:
    a = null
    b = null
    c = null
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
    
    print(objnode.text, end="\n")
    
    time.sleep(10)

    a=0
    b=0
    c=0
    messages = client.messages.list(
                                date_sent=datetime.now()-10;
                                limit=30
                            )
    for record in messages:
        if (record.body == '1'):
            a += 1
        elif (record.body == '2'):
            b += 1
        elif (record.body == '3'):
            c += 1

    sum = a+b+c

    print(sum, " people voted.\n");
    print("%0.2f" % (a/sum * 100), "% voted OPTION 1\n")
    print("%0.2f" % (b/sum * 100), "% voted OPTION 1\n")
    print("%0.2f" % (c/sum * 100), "% voted OPTION 1\n")

    if (a>b and a>c):
        return objnode.a
    elif (b>a and b>c):
        return objnode.b
    else:
        return objnode.c

def main():

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


