#Task Sheet 2 - Game Improvements

##Introduction
This series of tasks focuses on improving the game so that it is possible to **persist** data between runs of the program and beginning the process of adding flexibility and customisation to the structure of the game.

##Task 6 - Ace High or Low?
In most card games it is possible to decide whether you want the **ace** to be considered the lowest or highest value in the deck. Currently the program always considers the ace to be low. This needs to be changed to allow the user to make the decision about the ace's value.

It should work as follows:

![The user selects the **options** choice from the main menu][1]

![They are then presented with the options menu][2]

![Having selected an option to modify, the user can then change the default][3]

![The main menu is then redisplayed][4]

###Questions
**Answer** the following questions:

1. Where would be a good place in the program to keep track of whether the ace is high or not? Remember that the aces' value will be set before a game is started and it will not change for the duration of the game.
2. Name the function that will need to be altered so that **`5. Options`** is part of the main menu.
3. Name the function that will need to be modified so that card value comparisons will work correctly now that aces can be either high or low.

###Pseudo-code
You will need four additional functions to make this improvement possible:

- **`DisplayOptions()`** - presents the options menu
- **`GetOptionChoice()`** - gets the options choice from the user
- **`SetOptions(OptionChoice)`** - decides which option is to be modified based on the user's choice
- **`SetAceHighOrLow()`** - asks the user to decide whether the ace should be considered high or low and then sets this value

**Remember** that **validation** should be included where necessary.

1. Write pseudo-code for each of the four functions identified above.

###Program code
Make the following changes to the code in the program:

1. Amend the function you identified in **Question 2** so that **`5. Options`** is part of the main menu.
2. Convert the **pseudo-code** you have written to Python code.
3. Improve the function you identified in **Question 3** so that comparisons work correctly.

###Testing
In the previous section you made significant changes to the program. These changes must be tested to ensure that the program functions correctly. Using the **headings given below** to help you, write a test plan for your changes.

|Test Number|Test Description|Test Data|Type|Expected Result|Actual Result|
|-----------|----------------|---------|----|---------------|-------------|
| | | | | | |

Remember to provide tests for **normal, erroneous and boundary** data.

##Task 7 - Sorting scores (from highest to lowest)
Normally score tables for games are **sorted** - the highest score at the top and the lowest at the bottom. Current the recent scores table in the game is unsorted. 

###Pseudo-code
To sort the score table you will need to create a new function called **`BubbleSortScores(RecentScores)`**.

1. Write the pseudo-code for this function, ensuring that the scores will be displayed from highest to lowest.

###Program code
The **`BubbleSortScores(RecentScores)`** function should be called **before** the score table is displayed on screen. **Implement** the pseudo-code algorithm you have written and then call it in the correct place to sort the scores.

##Task 8 - Saving scores to a text file
Currently recent scores are lost when the program is quit. It would be better if the program saved the most recent scores to a file so that they can be recalled later. This would mean that when you get a score you would have to beat the highest all time score and not just the highest score since the last time the program was run.

![][5]

###Program code
Make the following changes to the program, keeping in mind that you are dealing with **text** files:

1. Amend **`DisplayMenu()`** so that there is an additional option to save the scores.
2. Write a new function called **`SaveScores(RecentScores)`** that will save the scores to a **text file** called **save_scores.txt**.
3. Amend the main program so that `SaveScores(RecentScores)` can be called successfully.

##Task 9 - Loading scores from a text file
Having saved the scores to a file in the last task we need to enable the program to load in these scores **automatically** when the program runs.

###Program code
Make the following changes to the program:

1. Write a new function called **`LoadScores()`** that will read in the scores from the **text file** and reconstructed the RecentScores list of `TRecentScore()` records.
2. Improve the main program so that the RecentScores are loaded from the file but if the file is empty the program will still append the three blank scores that it currently does.

##Task 10a - Missing save file
Having added the code to load the file there is a problem - if this file doesn't exist it will crash the program!

![][6]

###Program code
Make the following changes to the program:

1. Improve the loading of the file so that it can deal with the **exception** of the **save_scores.txt** file being missing.

##Task 10b - More scores
The **constant** **`NO_OF_RECENT_SCORES`** provides the program with the number of scores that should be present in the high score list. Obviously it is possible to change this value between runs of the program.

###Questions
**Answer** the following questions:

1. Explain why changing the constant **`NO_OF_RECENT_SCORES`** could cause a problem if there are already scores stored in the text file **save_scores.txt**.

###Program Code
Make the following changes to the program:

1. Change the constant **`NO_OF_RECENT_SCORES`** so that 10 recent scores can be displayed.
2. Make any necessary improvements to the program so that the issue identified in **Question 1** is resolved.

##Next
The next set of tasks will continue to focus on **ways to improve the game**.


[1]:images/options_menu_select.png
[2]:images/options_menu_view.png
[3]:images/options_ace_select.png
[4]:images/options_return_to_main.png
[5]:images/save_menu_option.png
[6]:images/load_error.png
