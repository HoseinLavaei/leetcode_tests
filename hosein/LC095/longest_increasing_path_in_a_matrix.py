class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows_count = len(matrix)
        columns_count = len(matrix[0])
        longest_path_cache = [[0] * columns_count for _ in range(rows_count)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def depth_first_search(current_row: int, current_col: int) -> int:
            if longest_path_cache[current_row][current_col] != 0:
                return longest_path_cache[current_row][current_col]

            max_path_length = 1
            for row_offset, col_offset in directions:
                neighbor_row = current_row + row_offset
                neighbor_col = current_col + col_offset
                if 0 <= neighbor_row < rows_count and 0 <= neighbor_col < columns_count:
                    if matrix[neighbor_row][neighbor_col] > matrix[current_row][current_col]:
                        path_length = 1 + depth_first_search(neighbor_row, neighbor_col)
                        if path_length > max_path_length:
                            max_path_length = path_length

            longest_path_cache[current_row][current_col] = max_path_length
            return max_path_length

        global_maximum = 0
        for row_index in range(rows_count):
            for col_index in range(columns_count):
                path_length = depth_first_search(row_index, col_index)
                if path_length > global_maximum:
                    global_maximum = path_length

        return global_maximum