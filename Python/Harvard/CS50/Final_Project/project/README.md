# CS50 Wordle
#### Video Demo:  https://www.youtube.com/watch?v=oYuMOEH51Nw
#### Description:

##### ABOUT THE DATABASE
In the SQLite database that i created, there are three tables: users, user_info and words.
The table users stores the username and the encrypted password of the user that will be provided on the register page.
The table user_info stores the user points, so i can see if the users of CS50 Wordle are playing the game a lot, it also stores the current number of letters that will be provided on the index page, it also stores the current level that will be provided on the levels page and the current row that will be provided on the level page.
The table words stores 4000 words, 1000 five letter words, 1000 six letter words, 1000 seven letter words and 1000 eight letter words.

##### ABOUT THE REGISTER PAGE
In the register page, there are three input fields: username, password and confirmation.
If the user doesn't write anything on the username field, a message will tell them that they need to input their username.
If the user doesn't write anything on the password field, a message will tell them that they need to input their password.
If the user doesn't write anything on the confirmation field, a message will tell them that they need to input their confirmation.
If the password and the confirmation doesn't match, a message will tell them that the password and the confirmation doesn't match.
If the user writes their username and password correctly, both will be sent to the database.

##### ABOUT THE LOGIN PAGE
In the register page, there are two input fields: username and password.
If the user doesn't write anything on the username field, a message will tell them that they need to input their username.
If the user doesn't write anything on the password field, a message will tell them that they need to input their password.
If the user writes their username and password, both will be compared to the ones in the database, if either the username or the password doesn't match, a message will tell them that or the username or the password are invalid.

##### ABOUT THE NAVIGATION BAR
If the user isn't logged in, the navigation bar will only show the login and register options.
If the user is logged in, the navigation bar will show the menu and logout options.

##### ABOUT THE INDEX PAGE
This page requires the user to be logged in.
In the index page, there's one formulary in which the user needs to select an option, the options represents the size of the word that they will play with.
The options are: 5, 6, 7 and 8.
If the user doesn't select any option, a message will tell them that they need to select an option.

##### ABOUT THE LEVELS PAGE
This page requires the user to be logged in.
In the levels page, there's one formulary in which the user needs to select an option, the options represents the level that they will play with.
The options go from 1 to 1000, because there are 1000 words for each number of letters.
If the user doesn't select any option, a message will tell them that they need to select an option.
Every new user starts at level 1, so if the user selects an option that represents a level that is higher than their level, a message will tell them that they haven't unlocked that level yet.

##### ABOUT THE LEVEL PAGE
This page requires the user to be logged in.
In the level page, there are {number of letters that the user selected} inputs.
If the user misses an option, a message will tell them that they must fill in all the fields.
A random {number of letters that the user selected} letter word is selected from the database and the user needs to discover what word it is.
The user will input {number of letters that the user selected} letters.
If the letter that the user inputed is in the generated word and it is in the right spot, the input background color will become green.
If the letter that the user inputed is in the generated word but it isn't in the right spot, the input background color will become yellow.
If the letter that the user inputed isn't in the generated word, the input background color will become gray.
The user has 4 attempts to discover the word, if the user doesn't discover it, a message will tell them that they lost, but if the user discorvers it, a message will them that they won, and their level will be updated to the next level.
