"""
friends = input()
gifts = input()
friends_len = len(friends)
"""

friends = ["muzi", "ryan", "frodo", "neo"]
friends_len = len(friends)
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

friend_matrix = [[0] * friends_len for _ in range(friends_len)]

for i in gifts:
    a, b = i.split()
    a = friends.index(a)
    b = friends.index(b)
    friend_matrix[a][b] += 1

p_mat = [[0] * 3 for _ in range(friends_len)]

for i in friend_matrix:
    print(i)
    for j in range(len(i)):
        p_mat[j][1] += i[j]  # p[][0] = get_count

for i in range(friends_len):
    p_mat[i][0] = sum(friend_matrix[i])  # p[][0] = give_count
    p_mat[i][2] = p_mat[i][0] - p_mat[i][1]


# 비교.
total = [0] * friends_len

for i in range(friends_len):
    for j in range(i + 1, friends_len):

        if friend_matrix[i][j] == friend_matrix[j][i]:  # 주고받은 개수 같으면
            # 선물지수 비교
            if p_mat[i][2] == p_mat[j][2]:  # 선물 지수 같으면
                continue  # 0개.
            elif p_mat[i][2] > p_mat[j][2]:
                total[i] += 1
            else:
                total[j] += 1
        elif friend_matrix[i][j] > friend_matrix[j][i]:
            total[i] += 1
        else:
            total[j] += 1

print(max(total))
