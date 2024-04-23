# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. 
# You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
# Replace the color of all of the aforementioned pixels with color.
# Return the modified image after performing the flood fill.

def flood_fill(image, sr, sc, newColor):
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    originalColor = image[sr][sc]
    
    if originalColor == newColor:
        return image
    
    def dfs(r, c):
        if (0 <= r < len(image)) and (0 <= c < len(image[0])) and (image[r][c] == originalColor):
            image[r][c] = newColor
            for dr, dc in directions:
                dfs(r + dr, c + dc)
    
    dfs(sr, sc)
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc, newColor = 1, 1, 2
result = flood_fill(image, sr, sc, newColor)
print(result)