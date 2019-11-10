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
                tree[children[1]] = (Node(split[1], text, children[1], False, children[1:]))

            # Jump Node
            # Format: Op Node Jump
            elif len(split[0]) == 6:
                tree[children[1]] = Node(split[1], text, children[1], True, children[2])

            # End node
            # Format: Op Node None
            else:
                tree[children[1]] = Node(split[1], text, children[1], False)

    return tree
