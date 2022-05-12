def solution(new_id):
    ban = '~!@#$%^&*()=+[{]}:?,<>/'

    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id2 = ''
    for i in range(len(new_id)):
        if new_id[i] not in ban:
            new_id2 += new_id[i]
    # 3단계
    while '..' in new_id2:
        new_id2 = new_id2.replace('..', '.')

    # 4단계
    new_id2 = new_id2.strip('.')

    # 5단계
    if new_id2 == '':
        new_id2 = 'a'

    # 6단계
    if len(new_id2) > 15:
        new_id2 = new_id2[:15].rstrip('.')

    # 7단계
    while len(new_id2) <= 2:
        new_id2 += new_id2[-1]

    answer = new_id2
    return answer