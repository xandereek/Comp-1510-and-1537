user_score = int(input("Enter your score: "))

if user_score >= 0:
    tickets = user_score // 10

    bonus_tickets = 0
    if  100 <= user_score < 500:
        bonus_tickets = 5
    elif user_score >= 500:
        bonus_tickets = 20

    total = tickets + bonus_tickets
    print("Base tickets: ", tickets)
    print("Bonus tickets: ", bonus_tickets)
    print("Total tickets: ", total)
else:
    print("Score must be zero or greater")