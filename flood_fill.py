def flood_fill(image, sr, sc, newColor):
    original_color = image[sr][sc]
    if original_color == newColor:
        return image

    def dfs(r, c):
        if (r < 0 or r >= len(image) or 
            c < 0 or c >= len(image[0]) or 
            image[r][c] != original_color):
            return
        image[r][c] = newColor #change color
        #flood fill algo recursion calls itself to adjacent pixels
        dfs(r + 1, c) #down
        dfs(r - 1, c) #up
        dfs(r, c + 1) #right
        dfs(r, c - 1) #left

    dfs(sr, sc)
    return image


print(flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)) # Output: [[2,2,2],[2,2,0],[2,0,1]]
