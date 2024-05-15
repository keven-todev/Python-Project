import random

user = input("Hey, what is your name ?")
welcome = print("Hello", user, "good luck !")

word_list = ["python", "java", "ruby", "javascript", "swift"]
random_word = random.choice(word_list)

correct_word = ["_"] * len(random_word)
turns = 12
displayed_parts = []

while turns > 0:
    response = input('Enter a letter: ')

    if response in random_word:
        print('A letter has been found, what is the next one?')
        for i in range(len(random_word)):
            if random_word[i] == response and correct_word[i] == "_":
                correct_word[i] = response
                print(correct_word)
    else:
        print('Sorry, this letter is not in the word.')
        if response not in displayed_parts:
            displayed_parts.append(response)
            turns -= 1
            print("Your remaining number of tries: ", turns)
            if turns == 0:
                print("The hangman is complete, you lost!")
                break

    if "_" not in correct_word:
        print('Congratulations, you won! The correct word was:', random_word)
        break
