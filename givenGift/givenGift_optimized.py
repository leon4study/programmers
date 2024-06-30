friends = ["muzi", "ryan", "frodo", "neo"]
friends_len = len(friends)
gifts = [
    "muzi frodo",
    "muzi frodo",
    "ryan muzi",
    "ryan muzi",
    "ryan muzi",
    "frodo muzi",
    "frodo ryan",
    "neo muzi",
]


def solution(friends, gifts):

    friends_len = len(friends)

    # 친구 이름을 인덱스로 매핑
    friend_index = {name: idx for idx, name in enumerate(friends)}

    # 주고받은 선물 횟수를 기록할 매트릭스 초기화
    friend_matrix = [[0] * friends_len for _ in range(friends_len)]

    # 선물 주고 받기 기록
    for gift in gifts:
        giver, receiver = gift.split()
        giver_index = friends.index(giver)
        receiver_index = friends.index(receiver)
        friend_matrix[giver_index][receiver_index] += 1

    """
    p_mat = [[0] * 3 for _ in range(friends_len)]

    for i in friend_matrix:
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
    """

    # 선물 주고받기 및 지수를 기록할 배열 초기화 > 구지 2차원 배열로 만들필요가 x..
    total = [0] * friends_len
    give_count = [0] * friends_len
    get_count = [0] * friends_len

    # 주고 받은 선물 횟수 계산
    for i in range(friends_len):
        for j in range(friends_len):
            give_count[i] += friend_matrix[i][j]
            get_count[j] += friend_matrix[i][j]

    # 선물 지수 계산 및 비교
    for i in range(friends_len):
        for j in range(i + 1, friends_len):
            if friend_matrix[i][j] == friend_matrix[j][i]:
                if (
                    give_count[i] - get_count[i] > give_count[j] - get_count[j]
                ):  # 추가로 matrix 생성 x.
                    total[i] += 1
                elif (
                    give_count[i] - get_count[i] < give_count[j] - get_count[j]
                ):  # if 조건문에서 continue 가 나오는 코드가 있으면 if 문 자체를 적지 x
                    total[j] += 1
            elif friend_matrix[i][j] > friend_matrix[j][i]:
                total[i] += 1
            else:
                total[j] += 1

    answer = max(total)

    return answer
