questions_dict = {
    "Q1": {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    "Q2": {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    "Q3": {"question": "What is the currency of Japan?", "options": ["Yuan", "Won", "Yen", "Ringgit"], "answer": "Yen"},
    "Q4": {"question": "Which is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": "Pacific Ocean"},
    "Q5": {"question": "Who wrote 'Harry Potter' series?", "options": ["J.R.R. Tolkien", "J.K. Rowling", "George Orwell", "Agatha Christie"], "answer": "J.K. Rowling"},
    "Q6": {"question": "Which animal is known as the King of the Jungle?", "options": ["Tiger", "Lion", "Elephant", "Cheetah"], "answer": "Lion"},
    "Q7": {"question": "How many continents are there on Earth?", "options": ["5", "6", "7", "8"], "answer": "7"},
    "Q8": {"question": "Which gas do plants absorb from the air?", "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], "answer": "Carbon dioxide"},
    "Q9": {"question": "What is the national sport of Canada?", "options": ["Cricket", "Ice Hockey", "Rugby", "Basketball"], "answer": "Ice Hockey"},
    "Q10": {"question": "How many legs does a spider have?", "options": ["6", "8", "10", "12"], "answer": "8"}
}
# print(questions_dict["Q1"]["question"])

price_money=0
for i in range(1,10):
    print(questions_dict[f"Q{i}"]["question"])
    print(questions_dict[f"Q{i}"]["options"])
    users_answer=input("choose any of the answer : ")
    if(users_answer.upper()==questions_dict[f"Q{i}"]["answer"].upper()):
        price_money=price_money+10000
        print(f"Correct!! You won {price_money}rs next question below")
    elif(users_answer.upper()==questions_dict[f"Q{i}"]["answer"].upper() and i==10):
        print("You won the game")
    else:
        print("oppss!! the given answer is incorrect you are out of the game")
        break        