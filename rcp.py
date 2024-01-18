import pymysql.cursors
import random

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='0000',
                             db='sakila',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

# Class Part
class player:

    def __init__(self, id, win, lose, draw, gold, plays):
        self.id = id
        self.win = win
        self.lose = lose
        self.draw = draw
        self.gold = gold
        self.plays = plays
    
    def info(self):
        print("--Player Info--\n")
        print("ID: {0}\n\
              Win: {1}\n\
              Lose: {2}\n\
              Draw: {3}\n\
              Gold: {4}\n\
              Plays: {5}\n".format(self.id, self.win, self.lose, self.draw, self.gold, self.plays))

# Function Part (player info)
def inputInfo(Ob, id):
    query = 'SELECT * FROM player_info WHERE id = %s'
    cursor.execute(query, id)
    row = cursor.fetchone()
    if row:
        while row:
            Ob.id = row['id']
            Ob.win = row['win']
            Ob.lose = row['lose']
            Ob.draw = row['draw']
            Ob.gold = row['gold']
            Ob.plays = row['plays']
            row = cursor.fetchone()
    else:
        print("\n해당 아이디가 없습니다\n")

def makeAccount(id):
    query = "INSERT INTO player_info VALUES (%s, %s, %s, %s, %s, %s)"
    zero = 0
    data = (id, zero, zero, zero, zero, zero)
    cursor.execute(query, data)
    print("Account Made Complete\n")

def printInfo():
    cursor.execute("SELECT * FROM `player_info`")
    print("플페이어 정보를 출력합니다\n")
    print("ID\t\t Wins\t Loses\t Draws\t Gold\t Plays")
    print("--------------------------------------------------------")
  
    row = cursor.fetchone()
    while row:
         print("%s\t\t %d\t %d\t %d\t %d\t %d" % (row['id'], row['win'], row['lose'], row['draw'], row['gold'], row['plays']))
         row = cursor.fetchone()

# Function Part (Game)

def get_user_choice():
    user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
    return user_choice.lower()

def get_computer_choice():
    choices = ['가위', '바위', '보']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    global w
    w = 0
    if user_choice == computer_choice:
        w += 3
        return "무승부", 0
    elif (
        (user_choice == '가위' and computer_choice == '보') or
        (user_choice == '바위' and computer_choice == '가위') or
        (user_choice == '보' and computer_choice == '바위')
    ):
        w += 1
        return "당신의 승리", 2
    else:
        w += 2
        return "컴퓨터의 승리", 2

def play_game():
    user_gold = 100
    computer_gold = 100
    rounds = 3

    for _ in range(rounds):
        global w
        print(f"\n현재 골드: 당신({user_gold}원) vs 컴퓨터({computer_gold}원)")

        # 최대 20원까지 걸 수 있도록 제한
        user_bet = min(int(input("얼마를 거시겠습니까? (최대 20원): ")), 20)
        computer_bet = random.randint(1, 20)

        user_gold -= user_bet
        computer_gold -= computer_bet

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\n당신의 선택: {user_choice}")
        print(f"컴퓨터의 선택: {computer_choice}")

        result, multiplier = determine_winner(user_choice, computer_choice)

        print(result)
        # 게임 결과에 따라 골드 조정
        if w == 1:
            user_gold += user_bet * multiplier
        elif w == 2:
            computer_gold += computer_bet * multiplier

        # 한 명이라도 골드가 0이 되면 게임 종료
        if user_gold <= 0 or computer_gold <= 0:

            print("\n최종 결과:")
            print(f"당신의 골드: {user_gold}원")
            print(f"컴퓨터의 골드: {computer_gold}원")

            print("\n게임 종료!")
            break

# Main Part
print("Rock Scissor Paper Game Program\n")
player_1 = player("id", 0, 0, 0, 0, 0)
com_1 = player("com", 0, 0, 0, 0, 0)
a = 0
global w

while True:
    print("\n\n1. New Game\
          2. Load Game\
          3. Print Info\
          4. Exit Game\n")
    choice = int(input("input: "))
    if choice == 1:
        new_id = input("Your New ID: ")
        makeAccount(new_id)
        inputInfo(player_1, new_id)
        a += 1
        #break
    elif choice == 2:
        old_id = input("Your ID: ")
        inputInfo(player_1, old_id)
        a += 1
        break
    elif choice == 3:
        printInfo()
    else:
        break

# Game Part
if a == 1:
    print("\nGame Start\n")
    play_game()
else:
    print("\nShutting Down Program\n")
