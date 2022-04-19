person = {'name': '유니', 'address': '분당', 'club': '만화'}
print(person['name'])

for key in person:
    print(key, person[key])

persons = [
    {'name': '유니', 'address': '분당', 'club': '만화'},
    {'name': '클라라', 'address': '서울', 'club': '만화'},
    {'name': '맥스', 'address': '서울', 'club': '모델링'},
    {'name': '다니엘림', 'address': '서울', 'club': '착시현상'}
]

print('==== persons ====')
for person in persons:
    for key in person:
        print(key, ':', person[key])
    print('-----------------')
