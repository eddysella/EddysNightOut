from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import time
import threading

# twilio phone-numbers:update "+15017122661" --sms-url="http://localhost:5000/sms"
# use code above to reset tunnel
num_reply = dict()

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    resp = MessagingResponse()
    num_reply[request.form['From']] = request.form['Body']
    resp.message("Response Received")
    # print(num_reply)
    return str(resp)


def run_vote(objnode):
    print(objnode.text, end="\n")

    time.sleep(20)

    a, b, c = 0

    for record in num_reply:
        if num_reply[record] == '1':
            a += 1
        elif num_reply[record] == '2':
            b += 1
        elif num_reply[record] == '3':
            c += 1

    num_reply.clear()
    total = a + b + c

    if total == 0:
        print("Nobody voted.\n")
        return objnode
    else:
        print(total, " people voted.\n")
        print("%0.2f" % (a / total * 100), "% voted OPTION 1\n")
        print("%0.2f" % (b / total * 100), "% voted OPTION 2\n")
        print("%0.2f" % (c / total * 100), "% voted OPTION 3\n")

    if a > b and a > c:
        return objnode.a
    elif b > a and b > c:
        return objnode.b
    else:
        return objnode.c


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

        def set_node_a(self, node):
            self.a = node

        def set_node_b(self, node):
            self.b = node

        def set_node_c(self, node):
            self.c = node

    def run(self):
        node = self.Node("I")
        node.set_node_a(self.Node("am"))
        node.a.set_node_a(self.Node("dead"))
        node.a.set_node_b(self.Node("alive"))
        node.a.set_node_c(self.Node("drunk"))

        node.set_node_b(self.Node("have"))
        node.b.set_node_a(self.Node("herpes"))
        node.b.set_node_b(self.Node("nothing"))
        node.b.set_node_c(self.Node("everything"))

        node.set_node_c(self.Node("can"))
        node.c.set_node_a(self.Node("fly"))
        node.c.set_node_a(self.Node("poop"))
        node.c.set_node_a(self.Node("giggle"))

        curr = node

        while curr is not None:
            curr = run_vote(curr)


if __name__ == "__main__":
    g = Game()
    g.start()
    app.run(debug=True)
