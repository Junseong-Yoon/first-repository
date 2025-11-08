## **Q1. Account 클래스**
은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. 
Account 클래스를 생성한 후 생성자(hint: 매직메서드..!!)를 구현해보세요. 
생성자에서는 예금주와 초기 잔액만 입력 받습니다. 

계좌계설 메서드를 만들고 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성되도록 합니다.
(은행이름: SC은행, 계좌번호: 111-11-111111)

## **Q2. 클래스 변수**
클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.

## **Q3. 클래스 변수 출력**
Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.

## **Q4. 입금 메서드**
Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.

## **Q5. 출금 메서드**
Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.

## **Q6. 정보 출력 메서드**
Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.
(은행이름: SC은행, 예금주: 파이썬, 계좌번호: 111-11-111111, 잔고: 10,000원)
쉼표를 출력하는 값은gpt로 찾아보기

## **Q7. 이자 지급하기**
입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.

## **Q8. 여러 객체 생성**
Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.

## **Q9. 특정 고객의 정보 출력**
객체 순회 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.

## **Q10. 입급과 출금 내역이 기록**

입금과 출금 내역이 기록되도록 코드를 업데이트 하세요.
(입금 내역과 출금 내역을 출력하는 deposit history와 withdrawal history 메서드를 추가하세요.)



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