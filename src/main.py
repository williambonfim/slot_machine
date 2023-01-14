from util import *

def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}')
        answer = input('Press enter to play (q to quit).')
        if answer == 'q':
            break
        balance += spin(balance)
    
    print(f'You left with ${balance}')

main()