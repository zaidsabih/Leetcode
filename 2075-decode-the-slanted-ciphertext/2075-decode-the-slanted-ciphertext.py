class Solution:
    def decodeCiphertext(self, encodedText, rows):
        if rows == 1:
            return encodedText

        n = len(encodedText)
        cols = n // rows

        matrix = [list(encodedText[i*cols:(i+1)*cols]) for i in range(rows)]

        res = []

        for start_col in range(cols):
            r, c = 0, start_col
            while r < rows and c < cols:
                res.append(matrix[r][c])
                r += 1
                c += 1

        return "".join(res).rstrip()