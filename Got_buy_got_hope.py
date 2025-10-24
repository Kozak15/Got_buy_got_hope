
import random
class Gamble():
    def __init__(self,money):
        self.money = money
    def set_money(self,money):
        self.money = money
    def get_money(self):
        return self.money
        
    def russian_roulette(self, n):#Anything above 5 means you will die most of the time
        loaded = random.randint(1,6)
        chamber = 1
        turns = 0
        Flag = False
        while True:
            print('Options:Quit,Spin,Shoot')
            option = input().lower()
            if option == 'quit':
                return('Coward')
            elif option == 'spin':
                Flag = True
                loaded = random.randint(1,6)
                chamber = 1
            elif option == 'shoot':
                #print("You pull the trigger, praying to whatever god is out there it's empty")
                if chamber == loaded:
                    print('BANG!')
                    if turns == 1:
                        print('You survived 1 round')
                    else:
                        print(f'You survived {turns} rounds')
                    self.money -= 10000*n
                    return 'You are dead'
                else:
                    turns += 1
                    chamber += 1
                    if chamber > 6:
                        chamber %= 6
                    #print('Click.')
                    print('You survived')          
                    if turns == n:
                        if Flag:
                            print('You spun though, so a half victory')
                        self.money += 10000 * n
                        return 'Congratulations, you survived!'
                
            else:
                print('Unknown input')
                continue
        #def blackjack(self,n):
        #    Flag = True
        #    hand = []
        #    card = ['A', '2', '3', '4', '5', '6', 
        #            '7', '8', '9', '10', 'J', 'Q', 
        #            'K']
        #    for _ in range(2):
        #        hand.append(random.randint(1,13))
        #    print(hand)
        #    while Flag:
        #        print('Hit or stand?')
        #    option = input().lower
        #    if option == 'hit':
        #        hand.append(random.randint(1,13))
        #        print(hand)


    def roulette(self,bet):#Only outside bets for now
        mon = self.money
        lst = ['High','Low','Number','Red','Black','Dozen','Column']
        print(lst)
        choice = input('What would you like to bet? ')
        if choice not in lst:
            return('Unknown input')
        else:
            n = random.randint(0,36)
            if n == 0:
                return('You lose')
                self.money -= bet
            if choice not in lst:
                return('Unknown input')
            elif choice == 'High' or choice == 'Low':
                if choice == 'High':
                    self.money += bet if (n > 18) else - bet
                if choice == 'Low':
                    self.money += bet if n < 19 else - bet
            elif choice == 'Number':
                num = int(input('Enter your number: '))
                if num not in range(0,36):
                    return('Unknown input')
                else:
                    self.money += 35*bet if num == n else - bet
            elif choice == 'Red' or choice == 'Black':
                lis = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
                if choice == 'Red':
                    self.money += bet if (n in lis) else - bet
                if choice == 'Black':
                    self.money += bet if (n not in lis) else - bet
            elif choice == 'Odd' or choice == 'Even':
                if choice == 'Odd':
                    self.money += bet if (n%2 == 1) else - bet
                if choice == 'Even':
                    self.money += bet if (n%2 == 0) else - bet
            else:
                c = int(input('1,2, or 3: '))
                if c not in [1,2,3]:
                    return('Unknown input')
                if choice == 'Dozen':
                    if c == 1:
                        self.money += 2*bet if n in range(1,13) else - bet
                    elif c == 2:
                        self.money += 2*bet if n in range(13,25) else - bet
                    else:
                        self.money += 2*bet if n in range(25,37) else - bet
                elif choice == 'Column':
                        self.money += 2*bet if n%3 == c else -bet
        if mon > self.money:
            print(f'You lost, {n} came up')
        else:
            print(f'You won!, {n} came up')
        print(f'You now have {self.money} dollars')
    #WIP
    #Got buy got hope, no buy no hope
    def four_d(self,bet):
        nums = [random.randint(0,9999) for _ in range(23)]
        lst = ['Big','Small']
        lst_1 = ['Ordinary','Roll','System Entry','iBet','Quickpick']
        choice = input()
        if choice not in lst:
            return 'Unknown input'
        else:
def chinese_blackjack(n):
    nums = ['Ace', '2', '3', '4', '5', 
            '6', '7', '8', '9', '10', 
            'Jack', 'Queen', 'King']
    suit = ['Diamonds', 'Clubs' ,'Hearts', 'Spades']
    hand = []
    for _ in range(13):
        hand.append((f'{nums[random.randint(0,12)]} of {suit[random.randint(0,3)]}'))
    while len(set(hand))<13:
        for _ in range(13 - len(set(hand))):
            hand.append((f'{nums[random.randint(0,12)]} of {suit[random.randint(0,3)]}'))
        hand = list(set(hand))
    hand.sort()
    print(hand)
    print('Enter the hand in a list format')
#WIP
def buckshot_roulette():#Russian roulette but with a shotgun
    Alive = True
    Lives = int(input())
    Dealer_Turn = False
    Player_Turn = True
    while Alive: 
        print(f'Dealer:{Lives} , Player:{lives}')
        Shells,Live,Dummy =  random.randint(1,12),random.randint(1,Shells),Shells-Live
        Dummy = max(Dummy,1)
        lst = ['Live']*Live + ['Dummy']*Dummy
        random.shuffle(lst)
        print(f'{Live} live shells, {Dummy} dummy shells')

    #Testing
    Dummy = max(Dummy,1)
    lst = ['Live']*Live + ['Dummy']*Dummy
    random.shuffle(lst)
    print(Shells,Live,Dummy)
    print(lst)
    print(lst[:-1])