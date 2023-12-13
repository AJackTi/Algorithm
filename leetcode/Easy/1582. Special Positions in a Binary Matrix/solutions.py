def numSpecial(mat: list[list[int]]) -> int:
    ans = 0
    for idx in range(len(mat)):
        for jdx in range(len(mat[idx])):
            if mat[idx][jdx] == 1:
                count = 0
                for i in range(len(mat)):
                    if mat[i][jdx] == 1:
                        count += 1
                if count == 1:
                    count = 0
                    for j in range(len(mat[idx])):
                        if mat[idx][j] == 1:
                            count += 1
                    if count == 1:
                        ans += 1

    return ans