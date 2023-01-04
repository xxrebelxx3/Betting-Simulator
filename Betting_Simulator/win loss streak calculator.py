import random



number_of_bets = 0
result_list = []

while number_of_bets < 20:
    
    result = random.choice([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    number_of_bets += 1
    result_list.append(result)

print(result_list)
print(number_of_bets)

str(result_list).replace(', ', '')

my_str = (result_list)
losing_char = "1"
winning_char = "0"
current_loss_seq = 0
max_loss_seq_len = 0
current_win_seq = 0
max_win_seq_len = 0

for c in my_str:
    if c == losing_char:
        current_loss_seq += 1
        if current_loss_seq > max_loss_seq_len:
            max_loss_seq_len = current_loss_seq
    else:
        current_loss_seq = 1
        losing_char = c

print("max loss streak: = ", max_loss_seq_len)