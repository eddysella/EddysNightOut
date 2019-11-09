from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import time
import threading

num_reply = dict()

app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])

def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    num_reply[request.form['From']] = request.form['Body']
    # print(num_reply)
    # Add a message
    resp.message("Response Received")

    return str(resp)


class Game(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

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

    def runVote(self, objnode):

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
        num_reply.clear()
        summ = a + b + c

        if summ == 0:
            print("Nobody voted.\n")
            return objnode
        else:
            print(summ, " people voted.\n");
            print("%0.2f" % (a / summ * 100), "% voted OPTION 1\n")
            print("%0.2f" % (b / summ * 100), "% voted OPTION 1\n")
            print("%0.2f" % (c / summ * 100), "% voted OPTION 1\n")

        if a > b and a > c:
            return objnode.a
        elif b > a and b > c:
            return objnode.b
        else:
            return objnode.c

    def run(self):

        node = self.Node("I")
        node.setNodeA(self.Node("am"))
        node.a.setNodeA(self.Node("dead"))
        node.a.setNodeB(self.Node("alive"))
        node.a.setNodeC(self.Node("drunk"))

        node.setNodeB(self.Node("have"))
        node.b.setNodeA(self.Node("herpes"))
        node.b.setNodeB(self.Node("nothing"))
        node.b.setNodeC(self.Node("everything"))

        node.setNodeC(self.Node("can"))
        node.c.setNodeA(self.Node("fly"))
        node.c.setNodeA(self.Node("poop"))
        node.c.setNodeA(self.Node("giggle"))

        curr = node

        while curr is not None:
            curr = self.runVote(curr)


if __name__ == "__main__":
    g = Game()
    g.start()
    app.run(debug=True)