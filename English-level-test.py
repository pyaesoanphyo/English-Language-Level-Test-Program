import random

# Define the questions, choices, and answers
questions = [
    "What is the correct form of the verb in the following sentence?\nShe ___________ to the store yesterday.",
    "Choose the correct preposition to complete the sentence:\nHe is afraid __________ spiders.",
    "Which of the following is the synonym of 'happy'?",
    "What is the opposite of the word 'big'?",
    "Identify the subject in the following sentence:\nThe cat chased the mouse.",
    "Which of the following sentences is correct?",
    "Choose the correct form of the verb to complete the sentence:\nThey _______ to the beach every summer.",
    "What is the plural form of 'child'?",
    "Which of the following words is a conjunction?",
    "Choose the correct article to complete the sentence:\n____ apple a day keeps the doctor away.",
    "Which of the following sentences uses the correct possessive form?",
    "What is the correct comparative form of the word 'good'?",
    "What is the correct past participle of the verb 'eat'?",
    "Choose the correct form of the verb to complete the sentence:\nShe _________ for the exam all night.",
    "Which of the following is a synonym for 'beautiful'?",
    "What is the opposite of the word 'hot'?",
    "Identify the adverb in the following sentence:\nShe speaks softly.",
    "Choose the correct form of the verb to complete the sentence:\nThey ________ basketball every Saturday.",
    "What is the plural form of 'goose'?",
    "Which of the following is a preposition?",
    "Choose the correct article to complete the sentence:\nI saw ____ movie last night.",
    "What is the comparative form of 'tall'?",
    "Which of the following sentences is correct?",
    "What is the plural form of 'man'?",
    "Which of the following is a conjunction?",
    "Choose the correct form of the verb to complete the sentence:\nShe _______ to the party last night.",
    "What is the superlative form of 'good'?",
    "Which of the following is a preposition?",
    "Choose the correct article to complete the sentence:\nHe bought ____ new car."
]

choices = [
    ["goes", "went", "going", "go"],
    ["of", "with", "in", "by"],
    ["sad", "cheerful", "angry", "worried"],
    ["large", "huge", "small", "gigantic"],
    ["The cat", "Chased", "The mouse", "The"],
    ["She don't like ice cream.", "She doesn't like ice cream.", "She isn't like ice cream.", "She not like ice cream."],
    ["go", "goes", "went", "gone"],
    ["childs", "childes", "child", "children"],
    ["happy", "and", "run", "quickly"],
    ["A", "An", "The", "None needed"],
    ["The cats collar was blue.", "The cats' collar was blue.", "The cat's collar was blue.", "The cats's collar was blue."],
    ["gooder", "more good", "better", "goodest"],
    ["ate", "ateen", "eat", "eating"],
    ["studied", "study", "studies", "studying"],
    ["ugly", "pretty", "handsome", "plain"],
    ["cold", "warm", "cool", "freezing"],
    ["softly", "speaks", "She", "the"],
    ["play", "plays", "played", "playing"],
    ["geeses", "geese", "gooses", "goose"],
    ["with", "happy", "run", "quickly"],
    ["a", "an", "the", "none"],
    ["taller", "more tall", "tall", "tallest"],
    ["He isn't like pizza.", "He does not like pizza.", "He not like pizza.", "He do not like pizza."],
    ["mens", "man", "men", "manes"],
    ["or", "and", "but", "to"],
    ["went", "go", "goes", "gone"],
    ["better", "goodest", "more good", "best"],
    ["on", "from", "for", "to"],
    ["a", "an", "the", "none"]
]

answers = [
    "went", "of", "cheerful", "small", "The cat",
    "She doesn't like ice cream.", "go", "children", "and", "A",
    "The cat's collar was blue.", "better", "eaten", "studied", "pretty",
    "cold", "softly", "play", "geese", "with",
    "a", "taller", "He does not like pizza.", "men", "and",
    "went", "better", "to", "a"
]

# Function to administer the test
def administer_test():
    score = 0
    total_questions = len(questions)

    # Shuffle questions
    combined = list(zip(questions, choices, answers))
    random.shuffle(combined)
    questions_shuffled, choices_shuffled, answers_shuffled = zip(*combined)

    # Ask questions
    for i in range(total_questions):
        print(f"\nQuestion {i+1}:")
        print(questions_shuffled[i])
        choices_list = choices_shuffled[i]
        for j in range(len(choices_list)):
            print(f"{chr(97+j)}) {choices_list[j]}")
        user_answer = input("Your answer (a, b, c, d): ").lower()
        if user_answer == 'a':
            user_answer = choices_list[0]
        elif user_answer == 'b':
            user_answer = choices_list[1]
        elif user_answer == 'c':
            user_answer = choices_list[2]
        elif user_answer == 'd':
            user_answer = choices_list[3]

        if user_answer == answers_shuffled[i]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {answers_shuffled[i]}")

    # Display results
    print("\nTest completed!")
    print(f"You got {score} out of {total_questions} questions correct.")

    # Determine English level
    if score >= 26:
        print("Congratulations! You are at an Advanced level.")
    elif 16 <= score <= 25:
        print("You are at an Intermediate level.")
    else:
        print("You are at a Beginner level.")

# Run the test
administer_test()
