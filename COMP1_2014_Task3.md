#Task Sheet 3 - Further Game Improvements

##Introduction
This series of tasks continues the theme of adding improvements to the game, including saving and restoring a running game and adding the concept of "lives" to the game.

##Task 11 - Guessing the same card
When playing the game if the next card that comes off the deck is equal in value to the current card, the new card is **not higher**. Therefore, if you guessed than the next card was going to be higher you will lose the game. This seems somewhat harsh - it would be better if the game just moved on to the next card but you didn't score a point in this situation.

It should work as follows:

![The user selects the **options** choice from the main menu][1]

![Having selected the **same score** option they can toggle its value][2]

![The main menu is then redisplayed][3]

###Questions
**Answer** the following questions:

1. Where would be a good place in the program to keep track of whether the same card should be considered lower or not? Remember that this value will be set before a game is started and it will not change for the duration of the game.
2. Name the **two functions** that will need to be modified so that card value comparisons will work correctly now that the same card may or may not be considered lower.
3. What additional value will you need to **return** from one of the above functions so that the game knows whether the cards have the same value or not.
4. Describe the alterations you will need to make to **`DisplayOptions()`** and **`GetOptionChoice()`** to allow for the new option.

###Pseudo-code
You will need one additional function to make this improvement possible:

- **`SetSameScore()`** - asks the user to decide whether the next card (if it has the same value) should be considered as having the same or lower value as the current card.

**Remember** that **validation** should be included where necessary.

1. Write pseudo-code for the function identified above.

###Program code
Make the following changes to the code in the program:

1. Amend the functions you identified in **Question 4** so that **you can change** this option from the main menu
2. Convert the **pseudo-code** you have written to Python code.
3. Improve the function you identified in **Question 2** so that comparisons work correctly.
4. Test your changes to ensure that the program works as expected.

##Task 12a - Saving your progress
A common feature of most games is the ability to save your current progress and continue from that point at a later date. We will need to add this functionality to our program.

It should work as follows:

![Instead of choosing yes or no, the user enters s for save][4]

![This saves the game and returns the user to the main menu][5]

Obviously the **current deck** will need to be saved to the text file **deck.txt** but in order to restore the game state we will need to store additional information.

###Questions
**Answer** the following questions:

1. Name and justify the pieces of data that must be stored in order to restore the game state
2. What kind of file would be most appropriate to save this information in? Explain why this is the case.
3. Identify the *two functions* you will need to save the state of the game.

###Pseudo-code
Write pseudo-code for each of the functions you identified in **Question 3**

###Program code
Make the following changes to the code in the program:

1. Convert the pseudo-code you have created into the equivalent Python code.
2. Make the necessary changes to the function **`PlayGame()`** so that the state of the game can be saved.

##Task 12b - Restoring an existing game
Now that the relevant data has been stored successfully into files the game will need to be able to restore this game if we choose to do so.

This should work as follows:

![On starting a new game if an existing game is found the user can choose to continue it or not][6]

![The program loads the existing game and the game then continues from the point it was saved][7]

###Questions
**Answer** the following questions:

1. Describe the changes that will be necessary in **`PlayGame()`** to allow for this new behaviour in the program.

###Program code
Make the following changes to the code in the program:

1. Create a new function called **`LoadGameProgress()`** that will **return** either the game data from the file or **`None`** to represent that nothing was loaded.
2. Make the necessary changes to **`PlayGame()`** to allow the user to choose to continue an existing game. **Ensure** that it is still possible to play a new game as well.

##Task 13 - Lives
Many computer games have the concept of lifes - you get more than a single chance to win the game. Currently our game is over as soon as you make a single mistake. It would be a little gentler if the player could have at least a few lives to play with!

Obviously, if a live is lost the the player's score should **not be increased**.

###Program code
Make the changes necessary to add the concept of lives to the game. **Remember** that your **saving and loading** functions should still work after these modifications.

##Task 14 - Deck creation
One really strange thing about the current program is that the **deck** of cards is always generated from information stored in a file. This makes sense when you have saved the state of an existing game but does not when you are starting a new game.

It would be much simplier to create the deck in Python **without** referring to a text file.

###Program code
Make the following changes to the code in the program:

1. Create a new function called **`CreateNewDeck`** that will construct and **return** an appropraite deck of cards.
2. Call this new function instead of loading the information from a file at the appropriate point in **`PlayGame()`**.

##Task 15 - Higher or lower
Currently the question asked when guessing the next card is a little weird - it would be better if it asked you whether you thought the next card was going to be **higher** or **lower** than the current card.

![][8]

###Program code
Make the necessary changes to the program so that the program works based on the user entering **higher** or **lower** rather than yes or no.

##Next
The next set of tasks will deal with more signifcant, advanced improvements that you could make to the program.





[1]: images/same_card_option.png
[2]: images/same_card_toggle.png
[3]: images/same_card_menu.png
[4]: images/save_game_choice.png
[5]: images/save_game_menu.png
[6]: images/load_game_choice.png
[7]: images/laod_game_continue.png
[8]: images/higher_lower.png