import random

player_health = 100
enemy_health = 100
critical_hit = 0
base_dmg = 1
sword = False
tf = [1, 0]
crit_multiplier = [2, 3, 4]

sword = input("An enemy approaches, do you wish to draw your sword or fight with your fists? Type S for sword and F for fist: ") == "S"
if sword == True:
    base_dmg += 5

print("A battle commences!")

while player_health and enemy_health > 0:
    print(random.choice(["You attack", "It's your turn", "You go for the eyes"]))
    critical_hit = random.choice(tf)
    if critical_hit == 1:
        enemy_health -= (base_dmg * random.choice(crit_multiplier))
        if enemy_health < 0:
            enemy_health = 0
        print("You dealt a critical Hit! Enemy health is at", enemy_health)
    else:
        enemy_health -= base_dmg
        if enemy_health < 0:
            enemy_health = 0
        print("You've dealt", str(base_dmg), "damage leaving the enemy with", str(enemy_health), "health")

    if enemy_health > 0:
        print(random.choice(["The enemy attacks", "The attacker bites you", "Here comes the pain!"]))
        critical_hit = random.choice(tf)
        if critical_hit == 1:
            player_health -= (base_dmg * random.choice(crit_multiplier))
            if player_health < 0:
                player_health = 0
            print("You been hit with a critical Hit! Your health is at", player_health)
        else:
            player_health -= base_dmg
            if player_health < 0:
                player_health = 0
            print("The enemy dealt", str(base_dmg), "damage leaving you with", str(player_health), "health")

if player_health <= 0:
    print("You have died.")
if enemy_health <= 0:
    print("You have defeated the enemy!")