import random


class Account :

  count = 0

  def __init__ (self, customer, money):
    self.customer = customer
    self.money = money

    self.deposit_count = 0

    self.A=random.randint(100,1000)        #100~999 사이 정수
    self.B=random.randint(10, 100)         #10~99 사이 정수
    self.C=random.randint(100000, 1000000) #100000~999999 사이 정수

    #초기화되는 생성자.
    self.account_number = self.A, '-', self.B, '-', self.C

    Account.count += 1

    self.deposit_history=[]
    self.withdrawal_history=[]

  def get_account_num():
    print(count)

  def info(self):
    print('예금주 :',self.customer, '잔액 :',self.money,'SC은행', self.account_number)




  #입금메서드
  def deposit(self, money):   #money에 받은 값을 self.money에 더해야하고 최소 1원 이상이여야함.

    money = int(money)
    if money > 0 :
      self.money = int(self.money) + money
      print(f"{money}원 입금 //{self.customer} 잔액 : {self.money}원")
      self.deposit_count += 1

      self.deposit_history.append(money)

      if self.deposit_count % 5 == 0 :
        rate = self.money * 0.01
        self.money = self.money + rate
        print(f"입금 5회 이상되어 1% 이자지급{rate} 총 잔액{self.money}")

    else:
      print("0원 이상을 기입하세요")



  #출금메서드
  def withdraw(self, money):
    money = int(money)
    if self.money >= money:
      self.money = int(self.money) - money
      print(f"{money}원 출금 //{self.customer} 잔액 : {self.money}원")

      self.withdrawal_history.append(money)

    else:
      print("잔액보다 큰 값을 입력할 수 없습니다.")


  #잔액을 보여주는 메서드
  def display_info(self):
    print(f"은행이름: SC은행, 예금주:{self.customer}, 계좌번호:{self.account_number}, 잔고: {int(self.money):,}원")

  #history를 출력하는 함수
  def result(self):
    print(f"{self.customer} 입출금내역")
    print("입금내역:",self.deposit_history[0:])
    print("출금내역:",self.withdrawal_history[0:])


#self를 받아서인자를 받을때 다 초기화

first = Account('윤준성', '10000000')
sceond = Account('김희철', '50000')
third = Account('박명수', '70000')

accounts=[first, sceond, third]

first.info()
sceond.info()

first.deposit('7000')
sceond.deposit('10000')

first.withdraw('1000')
sceond.withdraw('30000')

first.display_info()
sceond.display_info()

first.deposit('3000')
first.deposit('3000')
first.deposit('3000')
first.deposit('3000')


for account in accounts:
    if int(account.money) >= 1000000:
        account.display_info()


for account in accounts:
  account.result()