babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]


def solution(babbling):
    valid_sound = ["ye", "ma", "aya", "woo"]
    count = 0

    for word in babbling:
        for sound in valid_sound:
            if sound in word:
                word = word.replace(sound, " ", 1)
        word = word.replace(" ", "")  # 공백 제거.
        if not word:  # word 가 비어있으면
            count += 1
    return count


print(solution(babbling))
