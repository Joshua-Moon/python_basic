# 함수 없음
price = 10000
vat_rate = 0.1
print(price * vat_rate)

# 함수 생성
def get_vat():
  price = 10000
  vat_rate = 0.1
  print(price * vat_rate)
get_vat()

# 함수에 파라미터 1개
def get_vat(price):
  vat_rate = 0.1
  print(price * vat_rate)
get_vat(10000)
get_vat(20000)

# 함수에 파라미터 2개
def get_vat(price, vat_rate):
  print(price * vat_rate)
get_vat(10000, 0.1)
get_vat(20000, 0.3)

# 함수에 파라미터 없을 땐 기본 값
def get_vat(price, vat_rate = 0.1):
  print(price * vat_rate)
get_vat(10000)
get_vat(20000, 0.3)

# 함수는 한가지 역할만 하는 부품으로 만드는게 베스트
def get_vat(price, vat_rate = 0.1):
  return price * vat_rate
print(get_vat(10000))
print(get_vat(20000, 0.3))