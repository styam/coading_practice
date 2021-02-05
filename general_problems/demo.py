class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

node1 = linkedListNode("2")
node2 = linkedListNode("5")
node3 = linkedListNode("8")

node1.nextNode = node2
node2.nextNode = node3

currentNode = node1
while True:
    print(currentNode.value, "-->")
    if currentNode.nextNode is None:
        break
    currentNode = currentNode.nextNode
