"""Betting simulator.py - Betting Simulator to test wolf.bet strategy"""

import random
import matplotlib.pyplot as plt
from time import perf_counter
"""
0. (optional) header comment
1. imports 
2. constants
3. functions
4. main function

"""
def money_format(self, money: float) -> str:
    return "${:,.2f}".format(money)

def main():        
    
    # Variables
    start_time = perf_counter()
    bankroll = 128_844.50
    starting_bankroll = bankroll
    bankroll_max = bankroll * 2
    bet = 0.00000001
    win_counter = 0
    number_of_bet = 0
    bankroll_result = []
    number_of_bet_result = []
    result_list = []

    while bankroll > 0 and bankroll < bankroll_max and number_of_bet < 10_000_000:

        # numbers = [49 * "0", 51 * "1"]
        result = int(random.choice([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
        guess = 0
        number_of_bet += 1
        number_of_bet_result.append(number_of_bet)
        result_list.append(result)

        if guess == result:
            bankroll += (bet * 1.02)
            # print("congratulations you win, your current bankroll is ", bankroll)
            win_counter += 1
            bankroll_result.append(bankroll)
        else:
            bankroll -= bet
            # print("Sorry you lose, your bankroll is: ", bankroll)
            win_counter = 0
            bankroll_result.append(bankroll)

        if win_counter < 2 and bankroll > bet:
            bet *= 2.2
        if win_counter == 1 and bet > 0.05:
            bet = 0.00000001
        if win_counter < 2 and bankroll <= bet:
            bet = bankroll
            
        if win_counter == 2:
            bet = 0.00000001
            win_counter = 0

    
    # calculating max streak
    str(result_list).replace(', ', '')

    my_str = (result_list)
    losing_char = "1"
    current_loss_seq = 0
    max_loss_seq_len = 0
    
    for c in my_str:
            if c == losing_char:
                current_loss_seq += 1
                if current_loss_seq > max_loss_seq_len:
                    max_loss_seq_len = current_loss_seq
            else:
                current_loss_seq = 1
                losing_char = c


            # Printing to terminal
    if bankroll <= 0:
        print("You are broke!")
    if bankroll >= 1:
        print("You're rich bich, bankroll = $", bankroll)
    print("Number of Bets: = ", number_of_bet)
    print("Time to run: ", int(perf_counter() - start_time), "seconds")
    print("profit: = $", bankroll - starting_bankroll)
    print("max streak: = ", max_loss_seq_len)
    print((money_format(100000)))

# print to txt
    with open("bankroll.txt", 'w') as file:
        prev_elem = 0
        for elem in bankroll_result[-40:]:

            bet_size = abs(elem - prev_elem)
            if elem > prev_elem:
                file.write(f"{str(elem)} win, bet_size: {bet_size}\n")
            elif elem < prev_elem:
                file.write(f"{str(elem)} loss, bet_size: {bet_size}\n")
            prev_elem = elem
   
    # Graph code below:

        plt.plot(number_of_bet_result, bankroll_result)
        plt.xlabel('Number of Bet')
        plt.ylabel('Bankroll')
        plt.title('Betting Stratagy Simulation')
        plt.show()

if __name__ == '__main__':
    main()