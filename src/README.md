This is a project completed for the University Of Sussex hackathon: HackSussex 2019.
The game is a story based text game. 
The audience must vote for the decisions the story will follow by texting a phone number.
The twilio API was used for the texting functionality.
Any story can be created by replacing the text file Storyline.
The story will be parsed into a graph which is then traversed to create the game.

Storyline editing:

Op 0 creates a node with index 0.
Op 1 creates a node with index 1.

Op 0 1 creates a jump node which when accessed jumps directly from node 0 to node 1.
Op 1 2 creates a jump node which when accessed jumps directly from node 1 to node 2.

Op 0 1 2 creates a parent node with index 0 who has two children, nodes 1 and 2.
Op 0 3 4 creates a parent node with index 0 who has two children, nodes 3 and 4.

Op 0: Label /n Text

  - Label is the title of the node
  - Text is the story/context that should accompany the node
