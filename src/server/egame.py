import operator

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import time
import threading
import sys
import os

# twilio phone-numbers:update "+441732252343" --sms-url="http://localhost:5000/sms"
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


def run_vote(tree, curr, nodes):
    if tree.get(curr).jump:
        for line in tree.get(curr).text:
            print(line)
        return nodes, tree.get(nodes).next_nodes
    else:
        print(tree.get(curr).label)
        for line in tree.get(curr).text:
            print(line)
        counters = {}
        for node in nodes:
            counters[node] = 0
            print(tree.get(node).label)

    time.sleep(15)

    for record in num_reply:
        for option in nodes:
            if num_reply[record] == option:
                counters[option] += counters[option] + 1

    num_reply.clear()
    total = sum(counters.values())

    if total == 0:
        print("Nobody voted.\n")
        return curr, nodes
    else:
        print(total, " people voted.\n")
        for option in nodes:
            print("%0.2f" % (counters[option] / total * 100), "%% voted OPTION", option, " \n")

    next = max(counters.items(), key=operator.itemgetter(1))[0]

    return next, tree.get(next).next_nodes


def create_tree(filepath):
    tree = {}
    story = []

    class Node:
        node = None
        next_nodes = None
        jump = False
        text = ""
        label = ""

        def __init__(self, label, textField, node, jump, next_nodes=None):
            self.next_nodes = next_nodes
            self.jump = jump
            self.node = node
            self.text = textField
            self.label = label

    def collect_text(file_as_list, index):
        y = index
        collected_lines = []
        while y < len(file_as_list) and not file_as_list[y].startswith('Op'):
            collected_lines.append(file_as_list[y])
            y += 1
        return collected_lines

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath, 'r', encoding="utf8") as fp:
        cnt = 0
        for line in fp:
            story.append(line)
            cnt += 1

    for i, line in enumerate(story):
        if line is None:
            None
        elif line.startswith('Op'):
            # Split into opcode + message
            split = story[i].split(':')
            # Collect text for the node
            text = collect_text(story, i + 1)
            # Collect connected nodes
            children = split[0].split(' ')

            # Display Node
            # Format: Op Node [Children]
            if len(split[0]) > 6:
                tree[children[1]] = (Node(split[1], text, children[1], False, children[2:]))

            # Jump Node
            # Format: Op Node Jump
            elif len(split[0]) == 6:
                tree[children[1]] = Node(split[1], text, children[1], True, children[2])

            # End node
            # Format: Op Node None
            else:
                tree[children[1]] = Node(split[1], text, children[1], False)

    return tree


class Game(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        story_tree = create_tree(sys.argv[1])
        curr = story_tree.get('0').node
        next_node = story_tree.get('0').next_nodes

        while curr is not None:
            curr, next_node = run_vote(story_tree, curr, next_node)


if __name__ == "__main__":
    g = Game()
    g.start()
    app.run(debug=True)
