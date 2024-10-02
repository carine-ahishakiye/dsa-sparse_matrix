# Programming Assignment 2: Sparse Matrix

## Task Description

This project involves working with **sparse matrices** and performing operations like **addition**, **subtraction**, and **multiplication**. You are required to implement a data structure that optimizes both memory and runtime for storing large sparse matrices.

The project is structured to load two sparse matrices from input files, perform mathematical operations on them, and output the results.

   - **Data Structure Requirements:**
     - Implement a data structure that optimizes memory usage and runtime performance.
     - Functions to implement:
       - `SparseMatrix(char* matrixFilePath)`: Load a sparse matrix from the provided file.
       - `SparseMatrix(int numRows, int numCols)`: Initialize a sparse matrix with specified dimensions.
       - `getElement(int currRow, int currCol)`: Retrieve the value at the specified position in the matrix.
       - `setElement(int currRow, int currCol, int value)`: Set the value at the specified position in the matrix.

   - **Mathematical Operations:**
     - Implement the following operations:
       - **Addition**
       - **Subtraction**
       - **Multiplication**

3. **Variations in Input Files:**
   - Handle various variations in the input file, such as:
     - Ignoring any whitespace on lines.
     - Throwing an error for incorrect formats (e.g., wrong types of parentheses or floating-point values) using the following error message:  
       `std::invalid_argument("Input file has wrong format")`.

## Key Functionalities

- **Memory-Efficient Storage**: The data structure should efficiently store large matrices where most values are zeros.
- **Custom Functions**: Implement all functions without using standard template libraries or built-in packages for sparse matrices. All helper functions and classes must be custom-made.
- **Mathematical Operations**: Ensure that the matrix addition, subtraction, and multiplication are correctly implemented and follow mathematical rules (e.g., matrix dimensions must match for multiplication).

## Error Handling

- Ensure that your code handles invalid input formats, whitespace, and matrix dimension mismatches appropriately.
- Use exception handling to provide meaningful error messages when input files are incorrectly formatted or operations cannot be performed.


### Sample Operations:

- Matrix Addition
- Matrix Subtraction
- Matrix Multiplication





