import heapq

#define nodes
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, next):
        return self.freq < next.freq


def buildTree(charFreq):


    # Create a minHeap
    nodes = []
    for char, freq in charFreq.items():
        node = Node(char, freq)
        heapq.heappush(nodes, node)

    # build tree by combining nodes untill one remains
    while len(nodes) > 1:
        # remove 2 min values
        node1 = heapq.heappop(nodes)
        node2 = heapq.heappop(nodes)

        # create a new node as their parent with the combined freq
        parent = Node(None, node1.freq + node2.freq)
        parent.left = node1
        parent.right = node2

        # push the parent node back into the minHeap
        heapq.heappush(nodes, parent)

    # return the final value
    return heapq.heappop(nodes)

# encode values based on minheap
def buildCodex(tree):
    codes = {}
    
    def traverse(node, code):
        if node.char:
            codes[node.char] = code
        else:
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

    traverse(tree, "")
    return codes

# run both buildTree & buildCodex and combine final output value
def huffmanDriver(charFreq, text):
    tree = buildTree(charFreq)
    codes = buildCodex(tree)

    output = ""
    for char in text:
        output += codes[char]

    return output




#run the 
text = "KALAMAZOO CS"
charFreq = ({'A': 40, 'C':30, 'K':10, 'L':40, 'M': 20, 'O': 70, 'S': 60, 'Z': 5, ' ': 90})
output = huffmanDriver(charFreq, text)
print("Original text:", text)
print("Encoded text:", output)
