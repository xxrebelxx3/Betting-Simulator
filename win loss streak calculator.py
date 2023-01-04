import random



number_of_bets = 0
result_list = []

while number_of_bets < 1_000_000_000:
    
    result = random.choice([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    number_of_bets += 1
    result_list.append(result)

#print(result_list)
print("Number of bets:", number_of_bets)

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

print("Max Streak: =", max_loss_seq_len)