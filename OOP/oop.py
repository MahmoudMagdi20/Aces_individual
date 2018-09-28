class Matrix:
    __id = 0

    def __init__(self, *args):
        #Defining an empty list for rows.
        self.matrix_rows = []
        #If no. of elements in args = 0
        #,then add to matrix only one row that has one col with value 0.
        if len(args) == 0:
            self.matrix_rows.append([0])
        #Adding to matrix each row in args.
        for a in args:
            self.matrix_rows.append(a)
        Matrix.__id += 1
        self.__id = Matrix.__id

    def rows(self):
        return len(self.matrix_rows)

    def cols(self):
        return len(self.matrix_rows[0])

    def dimensions(self):
        return str(len(self.matrix_rows)) + 'x' + str(len(self.matrix_rows[0]))

    def get_id(self):
        return self.__id

    def description(self):
        return self.matrix_rows


A = Matrix([1,2,3],[4,5,6],[7,8,9])
B = Matrix([1,2],[3,4])
C = Matrix([1,2],[5,6],[7,9])
D = Matrix()

print(A.get_id())
print(B.get_id())
print(C.get_id())
print(D.get_id())

print()

print(A.rows())
print(A.cols())
print(A.dimensions())
print(A.description())

print()

print(B.rows())
print(B.cols())
print(B.dimensions())
print(B.description())

print()

print(C.rows())
print(C.cols())
print(C.dimensions())
print(C.description())

print()

print(D.rows())
print(D.cols())
print(D.dimensions())
print(D.description())
