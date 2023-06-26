#https://www.youtube.com/watch?v=EUUlB4Rmhf0

class Node:
    def __init__(self, data,node):
        self.data = data
        self.next = None
        self.name = node

    def __str__(self):
        return f'\nNode Name: {self.name} Data: {self.data} Next: ***{self.next}***'

node1 = Node(5,'node1')
node2 = Node(10,'node2')
node1.next = node2
#print(node2)
print(node1)