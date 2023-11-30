print("Welcome to the word guessing game!")

secret_word = "moroni"
underscores = "_ " * len(secret_word)

count = 1

while underscores != secret_word:
    hint = input(f"Your hint is: {' '.join(underscores)} ")
    guess = input("What is your guess: ")
    if (len)(guess) != (len)(secret_word): 
        print("Invalid guess. Please enter a word of the same length as the secret word.")
        continue
    if guess == secret_word:
        print("Congratulations! You guessed the word correctly!")
        break
    
    correct_guess = False  # Flag to track if the guess is correct
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            count += 1
            underscores = underscores[:2 * i] + secret_word[i] + underscores[2 * i + 1:]
            correct_guess = True
    
    if not correct_guess:
        # Capture the first letter from the incorrect word guess that is in the secret word
        for letter in guess:
            if letter in secret_word:
                index = secret_word.index(letter)
                underscores = underscores[:2 * index] + letter + underscores[2 * index + 1:]
                count += 1
                break
        print(f"The word '{guess}' is not the word.")
        
        
print(f"Congratulations! You guessed the word '{secret_word}' in {count} attempts.")
exit()