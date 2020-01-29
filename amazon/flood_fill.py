from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
    if image[sr][sc] == new_color:
        return image
    dfs(image, image[sr][sc], new_color, sr, sc)
    return image


def dfs(image: List[List[int]], color: int, new_color: int, i: int, j: int) -> None:
    if i < 0 or i >= len(image) or j < 0 or j >= len(image[i]) or image[i][j] != color:
        return
    image[i][j] = new_color
    dfs(image, color, new_color, i - 1, j)
    dfs(image, color, new_color, i + 1, j)
    dfs(image, color, new_color, i, j - 1)
    dfs(image, color, new_color, i, j + 1)


if __name__ == '__main__':
    print(flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))