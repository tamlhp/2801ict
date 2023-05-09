import heapq

class Node:
    def __init__(self, frequency, symbol=None, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(alphabet, frequencies):
    priority_queue = [Node(frequencies[s], s) for s in alphabet]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        a = heapq.heappop(priority_queue)
        b = heapq.heappop(priority_queue)
        c = Node(a.frequency + b.frequency, left=a, right=b)
        heapq.heappush(priority_queue, c)

    return priority_queue[0]

def dfs_traversal(node, codeword, codeword_dict):
    if node.symbol is not None:
        codeword_dict[node.symbol] = codeword
    else:
        dfs_traversal(node.left, codeword + '0', codeword_dict)
        dfs_traversal(node.right, codeword + '1', codeword_dict)

def get_codewords(root_node):
    codeword_dict = {}
    dfs_traversal(root_node, '', codeword_dict)
    return codeword_dict

def huffman_encode(input_string, codewords):
    encoded_string = ''.join([codewords[symbol] for symbol in input_string])
    return encoded_string

def huffman_decode(encoded_string, root_node):
	decoded_string = []
	current_node = root_node

	for bit in encoded_string:
	    if bit == '0':
	        current_node = current_node.left
	    else:
	        current_node = current_node.right

	    if current_node.symbol is not None:
	        decoded_string.append(current_node.symbol)
	        current_node = root_node

	return ''.join(decoded_string)
# Example usage:

alphabet = ['A', 'B', 'C', 'D', 'E']
frequencies = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 12}
input_string = 'ABCDEABCDEABCDEE'

root_node = build_huffman_tree(alphabet, frequencies)
codewords = get_codewords(root_node)
encoded_string = huffman_encode(input_string, codewords)
decoded_string = huffman_decode(encoded_string,root_node)
print("Codewords:", codewords)
print("Encoded string:", encoded_string)
print("Encoded string:", decoded_string)