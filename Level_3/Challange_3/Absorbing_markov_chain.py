import fractions

class Inverse_Matrix:

    def __init__(self, matrix):
        self.size = len(matrix)
        self.matrix = self.inverse(matrix)

    def getCofactor(self,A, temp, p, q, n):
        i = 0
        j = 0

        for row in range(n):

            for col in range(n):

                if (row != p and col != q):
                    temp[i][j] = A[row][col]
                    j += 1
                    if (j == n - 1):
                        j = 0
                        i += 1


    def determinant(self, A, n):
        determinant_ = 0
        if (n == 1):
            return A[0][0]

        temp = [[None for _ in range(self.size)] for i in range(self.size)]  # To store cofactors
        sign = 1

        for f in range(n):
            # Getting Cofactor of A[0][f]
            self.getCofactor(A, temp, 0, f, n)
            determinant_ += sign * A[0][f] * self.determinant(temp, n - 1)

            sign *= -1

        return determinant_

    def adjoint(self, A, adj):
        if (self.size == 1):
            adj[0][0] = 1
            return

        sign = 1
        temp = [[None for _ in range(self.size)] for i in range(self.size)]  # To store cofactors


        for i in range(self.size):
            for j in range(self.size):
                self.getCofactor(A, temp, i, j, self.size)
                sign = [1, -1][(i + j) % 2]
                adj[j][i] = (sign) * (self.determinant(temp, self.size - 1))


    def inverse(self, A):
        # Find determinant of A[][]
        inverse = [[None for _ in range(self.size)] for i in range(self.size)]
        determinant_ = self.determinant(A, self.size)
        if (determinant_ == 0):
            #print("Singular matrix, can't find its inverse")
            return False

        adjoint_matrix = [[None for _ in range(self.size)] for i in range(self.size)]

        self.adjoint(A, adjoint_matrix)

        for i in range(self.size):
            for j in range(self.size):
                inverse[i][j] = adjoint_matrix[i][j] / float(determinant_)

        return inverse


def F_times_R(X, Y):
    result = [[0 for i in range(len(Y[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result


def convert_to_transition_matrix(matrix):

    for row_index, row in enumerate(matrix):
        temp_sum = sum(row)
        for element_index, element in enumerate(row):
            if sum(row) > 0:
                matrix[row_index][element_index] /= float(temp_sum)
    return matrix

def get_fundamental_matrix(Q):
    Identity = [[0 if _ != i else 1 for _ in range(len(Q))] for i in range(len(Q))]
    I_minus_Q = [[None for _ in range(len(Q))] for i in range(len(Q))]

    for row in range(len(Q)):
        for element in range(len(Q)):
            I_minus_Q[row][element] = Identity[row][element]-Q[row][element]
    Fundamental = Inverse_Matrix(I_minus_Q).matrix

    return Fundamental


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_fractions(f_times_r):
    fractions_ = [fractions.Fraction(element).limit_denominator() for element in f_times_r[0]]
    lcm = 1
    for denominator in fractions_:
        if denominator.denominator != 1:
            lcm = lcm * denominator.denominator // gcd(lcm, denominator.denominator)
    fractions_ = [(i * lcm).numerator for i in fractions_]
    fractions_.append(lcm)

    return fractions_


def Get_F_and_R(m):
    m = convert_to_transition_matrix(m)
    terminal = []
    terminal_index = []
    transient = []
    transient_index = []

    for index,row in enumerate(m):
        if sum(row) == 0:
            terminal.append(row)
            terminal_index.append(index)
        else:
            transient.append(row)
            transient_index.append(index)
    R = []
    Q = []

    for i in transient_index:
        temp_t = []
        temp_n = []
        for j in terminal_index:
            temp_t.append(m[i][j])
        for j in transient_index:
            temp_n.append(m[i][j])
        R.append(temp_t)
        Q.append(temp_n)
       # print "these are the terminal nodes", terminal
    Fundamental = get_fundamental_matrix(Q)


    return Fundamental, R

def solution(m):
    if sum(m[0])==0:
        return [1,1]
    Fundamental, R = Get_F_and_R(m)
    FR = F_times_R(Fundamental, R)
    result = get_fractions(FR)
    return result
#m = [[0,3,1,0,0,0],[0,0,0,2,0,0],[0,0,0,0,1,0],[0,0,0,2,0,1],[0,0,0,0,0,0],[0,0,0,0,0,0]]
#m = [[0,1,0,0,0,1],[4,0,0,3,2,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
#m = [[0,1,0,3,0],[4,0,2,0,0],[0,0,0,0,0],[3,0,0,0,2],[0,0,0,0,0]]
#m = [[0,2,1,0,0],[0,0,0,3,4],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#m = [[0,3,1,0,0,0],[0,0,2,2,0,0],[0,0,0,2,0,0],[]]
print (solution(m))
