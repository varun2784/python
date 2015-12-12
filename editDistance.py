def edit_dist(word1, word2, i, j):
    if i == 0 and j == 0:
        return 0
    if i == 0:
        return 1 + edit_dist(word1, word2, i, j-1)
    if j == 0:
        return 1 + edit_dist(word1, word2, i-1, j)

    if word1[i-1] == word2[j-1]:
        return edit_dist(word1, word2, i-1, j-1)
    else:
        x = min(edit_dist(word1, word2, i-1, j),
                edit_dist(word1, word2, i, j-1),
                edit_dist(word1, word2, i-1, j-1))
        return 1 + x

if __name__ == "__main__":
    word1 = "PLASMA"
    word2 = "ALTRUISM"
    print edit_dist(word1, word2, len(word1), len(word2))
