class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        self.data = {}
        if matrixFilePath:
            self.load_from_file(matrixFilePath)
        elif numRows is not None and numCols is not None:
            self.numRows = numRows
            self.numCols = numCols
        else:
            raise ValueError("Either matrixFilePath or numRows/numCols must be provided.")

    def load_from_file(self, matrixFilePath):
        with open(matrixFilePath, 'r') as file:
            lines = file.readlines()

        # Parse the matrix dimensions
        if len(lines) < 2:
            raise ValueError("Input file format is incorrect.")

        try:
            self.numRows = int(lines[0].strip().split('=')[1])
            self.numCols = int(lines[1].strip().split('=')[1])
        except (IndexError, ValueError):
            raise ValueError("Input file has wrong format.")

        # Parse the matrix values
        for line in lines[2:]:
            line = line.strip()
            if not line:
                continue  # Ignore empty lines
            if not (line.startswith("(") and line.endswith(")")):
                raise ValueError("Input file has wrong format.")
            try:
                row, col, value = map(int, line[1:-1].split(","))
                self.setElement(row, col, value)
            except ValueError:
                raise ValueError("Input file has wrong format.")

    def getElement(self, currRow, currCol):
        return self.data.get((currRow, currCol), 0)

    def setElement(self, currRow, currCol, value):
        if value != 0:
            self.data[(currRow, currCol)] = value
        elif (currRow, currCol) in self.data:
            del self.data[(currRow, currCol)]

    def add(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for addition.")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for (row, col), value in self.data.items():
            result.setElement(row, col, value + other.getElement(row, col))
        return result

    def subtract(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for subtraction.")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for (row, col), value in self.data.items():
            result.setElement(row, col, value - other.getElement(row, col))
        return result

    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrices dimensions do not match for multiplication.")
        result = SparseMatrix(numRows=self.numRows, numCols=other.numCols)
        for (row_a, col_a), value_a in self.data.items():
            for col_b in range(other.numCols):
                value_b = other.getElement(col_a, col_b)
                if value_b != 0:
                    result.setElement(row_a, col_b, result.getElement(row_a, col_b) + value_a * value_b)
        return result

    def __str__(self):
        result = []
        for (row, col), value in self.data.items():
            result.append(f"({row}, {col}, {value})")
        return "\n".join(result)

def main():
    matrix1_path = input("Enter path for the first matrix: ")
    matrix2_path = input("Enter path for the second matrix: ")
    operation = input("Select operation (add, subtract, multiply): ")

    matrix1 = SparseMatrix(matrix1_path)
    matrix2 = SparseMatrix(matrix2_path)

    if operation == "add":
        result = matrix1.add(matrix2)
    elif operation == "subtract":
        result = matrix1.subtract(matrix2)
    elif operation == "multiply":
        result = matrix1.multiply(matrix2)
    else:
        print("Invalid operation.")
        return

    # Save the result to a file
    output_file_path = input("Enter path for the output result file: ")
    with open(output_file_path, 'w') as output_file:
        output_file.write("Resultant Matrix:\n")
        output_file.write(str(result))

    print(f"Results saved to {output_file_path}")

if __name__ == "__main__":
    main()