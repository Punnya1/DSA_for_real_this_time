from typing import List

class Solution:
    """
    LeetCode 73 - Set Matrix Zeroes

    Given an m x n integer matrix, if an element is 0, set its entire row
    and column to 0s. The operation must be done in-place.
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Optimal Approach (O(1) Extra Space)

        Strategy:
        - Use the first row and first column as markers.
        - Track separately if the first row or first column originally had a zero.
        """

        m, n = len(matrix), len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if first row contains zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if first column contains zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Update matrix based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero out the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


    # ---------------------------------------------------------------------
    # Below are alternative approaches kept for reference and learning.
    # They are NOT used in production or final submissions.
    # ---------------------------------------------------------------------

    def setZeroes_extra_space(self, matrix: List[List[int]]) -> None:
        """
        Approach 2: Using Extra Space

        - Maintain two arrays to mark rows and columns that contain zero.
        - Simple and readable, but uses extra memory.

        Time Complexity: O(m * n)
        Space Complexity: O(m + n)
        """

        m, n = len(matrix), len(matrix[0])
        row = [0] * m
        col = [0] * n

        # Record rows and columns that need to be zeroed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        # Update matrix
        for i in range(m):
            for j in range(n):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0


    def setZeroes_bruteforce(self, matrix: List[List[int]]) -> None:
        """
        Approach 3: Brute Force with Temporary Marker

        - Replace affected cells with a temporary marker.
        - Convert all markers to zero in a second pass.
        - Not recommended due to poor performance.

        Time Complexity: O(m * n * (m + n))
        Space Complexity: O(1)
        """

        m, n = len(matrix), len(matrix[0])
        MARKER = -99  # Temporary marker (assumes -99 is not in input)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # Mark entire column
                    for r in range(m):
                        if matrix[r][j] != 0:
                            matrix[r][j] = MARKER

                    # Mark entire row
                    for c in range(n):
                        if matrix[i][c] != 0:
                            matrix[i][c] = MARKER

        # Convert all markers to zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == MARKER:
                    matrix[i][j] = 0
