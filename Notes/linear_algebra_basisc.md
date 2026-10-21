# Emora — Day 1: Linear Algebra Foundations

## 1. NumPy Arrays

NumPy is a Python library used for numerical computing. It allows us to store numbers in arrays and perform mathematical operations efficiently.

Example:

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

Basic operations:

- `a + b`: adds corresponding elements.
- `a * b`: multiplies corresponding elements.
- `len(a)`: returns the number of elements in a one-dimensional array.
- `a.shape`: returns the dimensions of an array.
- `a.size`: returns the total number of elements in an array.

For example, the shape of a one-dimensional array containing three elements is `(3,)`. The shape of a matrix with two rows and three columns is `(2, 3)`.

## 2. Vectors and Vector Length

A vector is an ordered collection of numbers. In machine learning, vectors can represent numerical features or embeddings of text, images, and other data.

Example:

```python
a = np.array([1, 2, 3])
```

The length of a vector is also called its magnitude or Euclidean norm. To calculate it, square each element, add the squares, and take the square root.

Mathematical formula:

||a|| = sqrt(a1² + a2² + ... + an²)

For the vector a = [1, 2, 3]:

||a|| = sqrt(1² + 2² + 3²)

||a|| = sqrt(1 + 4 + 9)

||a|| = sqrt(14) ≈ 3.742

Python implementation:

```python
import math

numbers = [1, 2, 3]
sum_of_squares = 0

for number in numbers:
    sum_of_squares += number ** 2

length = math.sqrt(sum_of_squares)
print(length)
```

This implementation uses a loop and an accumulator to calculate the sum of the squared elements.

## 3. Dot Product

The dot product takes two vectors of equal length, multiplies their corresponding elements, and adds the products.

Mathematical formula:

a · b = a1*b1 + a2*b2 + ... + an*bn

Example:

a = [1, 2, 3]

b = [2, 3, 4]

Therefore:

a · b = (1*2) + (2*3) + (3*4)

a · b = 2 + 6 + 12 = 20

In NumPy, we can calculate the dot product using:

```python
np.dot(a, b)
```

I also implemented the dot product using a loop. This helped me understand how the calculation works internally.

A dot product requires vectors with the same number of elements. A robust function should reject inputs with different lengths.

## 4. Cosine Similarity

Cosine similarity measures the directional similarity between two nonzero vectors. It is calculated by dividing their dot product by the product of their lengths.

Formula:

cosine_similarity(a, b) = (a · b) / (||a|| * ||b||)

Example 1: Same direction

a = [1, 2]

b = [2, 4]

The second vector is twice the first vector, so both point in the same direction.

Cosine similarity = 1

Example 2: Perpendicular vectors

a = [1, 0]

b = [0, 1]

Their dot product is zero, so their cosine similarity is zero.

Example 3: Opposite directions

a = [1, 0]

b = [-1, 0]

The vectors point in opposite directions, so their cosine similarity is -1.

The usual range of cosine similarity is from -1 to 1:

- 1 means the vectors point in the same direction.
- 0 means the vectors are perpendicular.
- -1 means the vectors point in opposite directions.

Cosine similarity is useful in text retrieval because it can compare embeddings to estimate how similar two pieces of text are. However, a high similarity score does not guarantee that two sentences have the same meaning.

A zero vector has length zero, so cosine similarity is undefined for it. A robust implementation should detect this case before dividing.

## 5. Python Functions and Loops

I practiced writing reusable functions to calculate vector lengths, dot products, and cosine similarity.

Important concepts:

- `def` defines a function.
- A parameter receives an input.
- `return` sends a result back to the caller.
- A `for` loop visits each element in a collection.
- A `while` loop repeats while a condition remains true.
- An accumulator stores a running total.
- `len()` returns the number of elements in a one-dimensional list or array.
- `raise ValueError(...)` reports invalid input.

For example, in a loop that calculates a dot product, an accumulator starts at zero. Each iteration adds one product to the running total.

Good function design includes descriptive variable names, input validation, and handling edge cases.

## 6. Matrices

A matrix is a rectangular arrangement of numbers organized into rows and columns.

Example:

A = [[1, 2, 3],
     [4, 5, 6]]

This matrix has two rows and three columns. Its NumPy shape is `(2, 3)`.

For a two-dimensional NumPy array:

- `A.shape` returns the number of rows and columns.
- `A[0]` selects the first row.
- `A[1, 1]` selects the element in the second row and second column.
- `A[1, 2]` selects the element in the second row and third column.

Python indexing starts at zero. Therefore, the first row has index 0, and the second row has index 1.

## 7. Matrix Operations

Consider these two matrices:

A = [[1, 2],
     [3, 4]]

B = [[10, 20],
     [30, 40]]

### Matrix addition

In NumPy, `A + B` adds corresponding elements.

Result:

[[11, 22],
 [33, 44]]

### Element-wise multiplication

In NumPy, `A * B` multiplies corresponding elements.

Result:

[[10, 40],
 [90, 160]]

This operation is different from matrix multiplication.

### Matrix multiplication

In NumPy, `A @ B` performs matrix multiplication. Each result element is obtained by multiplying a row of the first matrix by a column of the second matrix and adding the products.

Result:

[[70, 100],
 [150, 220]]

For example, the top-left element is:

(1*10) + (2*30) = 70

If matrix A has shape `(m, n)` and matrix B has shape `(n, p)`, their product has shape `(m, p)`. The inner dimensions must match.

## 8. Connection to Emora

These concepts provide part of the mathematical foundation for Emora.

- Vectors can represent text embeddings.
- Dot products are used in neural network calculations and similarity measurements.
- Cosine similarity can help retrieve semantically related information.
- Matrices can represent batches of data, model weights, and intermediate neural network values.
- Matrix multiplication is a fundamental operation in neural networks and transformer models.

Later, I will learn how real embedding models transform text into high-dimensional vectors and how retrieval systems compare those vectors.

## 9. Day 1 Summary

During Day 1, I practiced:

1. Creating NumPy arrays.
2. Understanding vector length and magnitude.
3. Implementing dot products with loops.
4. Implementing cosine similarity using reusable functions.
5. Handling invalid vector lengths and zero vectors.
6. Understanding matrix shapes and indexing.
7. Performing matrix addition, element-wise multiplication, and matrix multiplication.
8. Connecting these mathematical operations to embeddings and neural networks.

The main lesson is that mathematical formulas can be translated into algorithms, implemented in Python, and verified using test cases.

Next topic: Probability and statistics, beginning with mean, median, variance, standard deviation, and basic probability.
