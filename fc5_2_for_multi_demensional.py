# 다차원 배열 프린트
persons = [
    ['유니', '분당', '만화'],
    ['클라라', '서울', '만화'],
    ['맥스', '서울', '모델링'],
    ['다니엘림', '서울', '착시현상']
]
print(persons[0][0])
print()

# 다차원 배열 반복문
for person in persons:
    print(person[0] + ',' + person[1] + ',' + person[2])
print()

# 배열에 이름 부여
person = ['유니', '분당', '만화']
name = person[0]
address = person[1]
club = person[2]
print(name, address, club)
print()

# 배열에 이름 한번에 부여
name, address, club = ['유니', '분당', '만화']
print(name, address, club)
print()

# 배열에 부여한 이름으로 반복문 실행
for name, address, club in persons:
    print(name + ',' + address + ',' + club)
