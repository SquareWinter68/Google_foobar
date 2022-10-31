def solution(m):

    class Node_:

        def __init__(self, index, numerator=None, denominator = None):
            self.index = index
            self.denominator = denominator
            self.numerator = numerator
            self.prev = None
            if self.numerator and self.denominator:
                self.simplify_fraction()
        def __str__(self):
            return "Node {0}, with the numerator {1} and the denominator {2}".format(self.index, self.numerator, self.denominator)


        def simplify_fraction(self):
            largest_devisor = None
            #print self.numerator
            if isinstance(self.numerator, int):
                for i in range(self.numerator, 1, -1):
                    if not self.numerator % i and not self.denominator % i:
                        largest_devisor = i
                        break
            if largest_devisor:
                self.numerator //= largest_devisor
                self.denominator //= largest_devisor


    class solution:
        def __init__(self, matrix):
            self.matrix = matrix
            self.clean_matrix()
            self.build_nodes(matrix)
            self.fractions()

        def clean_matrix(self):

            for i in range(len(self.matrix)):
                if self.matrix[i][i]:
                    self.matrix[i][i] = 0

        def build_nodes(self, matrix):
            self.nodes = [Node_(index) for index, row in enumerate(matrix)]
            self.leaf_nodes = []
            for index in range(len(matrix)):
                if not sum(matrix[index]):
                    self.leaf_nodes.append(index)
                for index_1 in range(len(matrix[index])):
                    if matrix[index][index_1]:
                        self.nodes[index_1].prev = self.nodes[index]
                        self.nodes[index_1].numerator = matrix[index][index_1]
                        self.nodes[index_1].denominator = sum(matrix[index])
                       # print index,index_1, matrix[index][index_1]
                       # print self.nodes[index_1]
            self.update_nodes(self.nodes)

        def update_nodes(self, nodes):
            for index, node in enumerate(nodes):

                if node.prev and node.index and node.prev.index:
                    node.numerator *= node.prev.numerator
                    node.denominator *= node.prev.denominator

            for node in nodes:
                if node.numerator and node.denominator:
                    node.simplify_fraction()


        def fractions(self):
            denominators = []
            fractions = []
            for leaf in self.leaf_nodes:
                #print(f"the leaf {self.nodes[leaf]}")
                if self.nodes[leaf].numerator and self.nodes[leaf].denominator:
                    denominators.append(self.nodes[leaf].denominator)
                    fractions.append((self.nodes[leaf].index, self.nodes[leaf].denominator, self.nodes[leaf].numerator))
            self.least_comon_denominator(fractions, denominators)

        def gcd(self, a, b):
            while b:
                a, b = b, a % b
            return a

        def least_comon_denominator(self, fractions, denominators):
            lcm = 1
            results = {}
            for denominator in denominators:
                lcm = lcm * denominator // self.gcd(lcm, denominator)
            for fraction in fractions:
                multipliyer = lcm//fraction[1]
                results[fraction[0]] = (fraction[2]*multipliyer,lcm)
                #results.append((fraction[2]*multipliyer,lcm))
            results["common denominator"] = lcm

            self.build_results(results)



        def build_results(self, x):
            numerator_sum = []
            self.result = []
            for leaf in self.leaf_nodes:
                if not leaf in x:
                    self.result.append(0)
                else:
                    self.result.append(x[leaf][0])
                    numerator_sum.append(x[leaf][0])
            self.result.append(x["common denominator"]-(x["common denominator"] - sum(numerator_sum)))

    s1 = solution(m)
    return s1.result


#print solution([[0,1,0,3,0],[4,0,2,0,0],[0,0,0,0,0],[3,0,0,0,2],[0,0,0,0,0]])
#print solution_([[0,1,0,3,0],[4,0,2,0,0],[0,0,0,0,0],[3,0,0,0,2],[0,0,0,0,0]])

#m = [[0,3,1,0,0,0],[0,0,0,2,0,0],[0,0,0,0,1,0],[0,0,0,2,0,1],[0,0,0,0,0,0],[0,0,0,0,0,0]]
#m = [[0,1,0,0,0,1],[4,0,0,3,2,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
#m = [[0,1,0,3,0],[4,0,2,0,0],[0,0,0,0,0],[3,0,0,0,2],[0,0,0,0,0]]
m = [[0,2,1,0,0],[0,0,0,3,4],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#print solution_(m)
print solution(m)


