import math
def adjecency_matrix(matrix):
    multiplyers = []
    leaf_nodes = []
    nodes_visited = {node: 0 for node in range(len(matrix))}
    row_sums = []
    devisor = 0
    results = []

    for index, row in enumerate(matrix):
        row_sums.append(sum(row))
        if not sum(row):
            leaf_nodes.append((f"s{index}", index))
        else:
            if not devisor:
                devisor += sum(row)
            else:
                devisor *= sum(row)
        for index, element in enumerate(row):
            multiplyers.append((element, sum(row)))
           # print(f"index: {index} element: {element} of row: {row}")
            nodes_visited[index] += element
    #print(leaf_nodes)
    print(nodes_visited)
    #print(multiplyers)



    print("the devisor is", devisor)

    for leaf in leaf_nodes:
        results.append(nodes_visited[leaf[1]])

    results.append(devisor-nodes_visited[0])
    #print(results)
    #print(row_sums)
    #print(leaf_nodes)
    #print({index:[] for index,node in enumerate(matrix)})
    adj_list = {index:[] for index,node in enumerate(matrix)}
   # print(adj_list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if matrix[i][j]:
                if i in adj_list:
                    adj_list[i].append((j,matrix[i][j]))
                else:
                    adj_list[i] = [(j,matrix[i][j])]
    print(f"ADJ_LIST {adj_list} yeah")

    visited = set() # Set to keep track of visited nodes of graph.
    traversed_nodes=[]
    def dfs(visited, graph, node, multiplyer=None):  #function for dfs
        if node not in visited:
            print (node, multiplyer)
            traversed_nodes.append(node,multiplyer)
            visited.add(node)
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour[0], neighbour[1])
    #dfs(visited, adj_list, 0)

class Node_:

    def __init__(self, index, numerator=None, denominator = None):
        self.index = index
        self.denominator = denominator
        self.numerator = numerator
        self.prev = None
        if self.numerator and self.denominator:
            self.simplify_fraction()
    def __str__(self):
        return f"Node {self.index}, with the numerator {self.numerator} and the denominator {self.denominator}"

    def simplify_fraction(self):
        largest_devisor = None
        for i in range(self.numerator, 1, -1):
            if not self.numerator % i and not self.denominator % i:
                largest_devisor = i
                break
        if largest_devisor:
            self.numerator //= largest_devisor
            self.denominator //= largest_devisor

#matrix = [[0,1,0,0,0,1],[4,0,0,3,2,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
matrix = [[0,1,0,3,0],[4,0,2,0,0],[0,0,0,0,0],[3,0,0,0,2],[0,0,0,0,0]]
nodes = [Node_(index) for index, row in enumerate(matrix)]
leaf_nodes = []

for index in range(len(matrix)):
    if not sum(matrix[index]):
        leaf_nodes.append(index)
    for index_1 in range(len(matrix[index])):
        print(f"matrix row {matrix[index]}")
        if matrix[index][index_1]:
            print( f"The matrix element is {matrix[index][index_1]}")
            nodes[index_1].prev = nodes[index]
            nodes[index_1].numerator = matrix[index][index_1]
            nodes[index_1].denominator = sum(matrix[index])

for node in nodes:
    print(node)

print("\n\n")
print(nodes[-1])

for index, node in enumerate(nodes):

    if node.prev and node.index and node.prev.index:
        #print(f"the node {node.index} has a numerator of {node.numerator}, and node {node.prev.index} has a numerator of {node.prev.numerator}")
        node.numerator *= node.prev.numerator
        node.denominator *= node.prev.denominator
        #print(node.denominator, node.prev.denominator)
for node in nodes:
    node.simplify_fraction()
    print(node)
    if not node.numerator and not node.denominator:
        leaf_nodes.pop(leaf_nodes.index(node.index))
print(leaf_nodes)
for leaf in leaf_nodes:
    print(nodes[leaf])

numerators = []
denominators = []
def least_comon_denominator(numerators,denominators):
    lcm = 1
    for denominator in denominators:
        lcm = lcm * denominator // math.gcd(lcm, denominator)
    print(lcm)


def simplify_fraction(fraction):
    numerator = fraction[0]
    denominator = fraction[1]
    largest_devisor = None
    for i in range(numerator, 1 , -1):
        if not numerator%i and not denominator%i:
            largest_devisor = i
            break
    if largest_devisor:
        return [numerator//largest_devisor, denominator//largest_devisor]
    #print(f"the largest devisor is {largest_devisor}")
    #print(f"the simplest form of the fraction {numerator}/{denominator} is {numerator//largest_devisor}/{denominator//largest_devisor}")

print(simplify_fraction([30,100]))
#print(f"Have to make this shit stand out bruv, nou doubt {least_comon_denominator([0],[24, 20,25])}")
#adjecency_matrix(matrix)

