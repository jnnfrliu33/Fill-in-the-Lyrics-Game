ARTIST_LIST = ["adele", "charlie puth", "kelly clarkson"]
LEVEL_LIST = ["easy", "medium", "hard"]
NO_OF_BLANKS = {"easy": 4, "medium": 6, "hard": 10}

SONGS_DICT = {
    # Contains the song titles corresponding to
    # the artist and the difficulty level
    "adele":
        {"easy": "Hello",
         "medium": "Rolling in the Deep",
         "hard": "Someone Like You"},
    "charlie puth":
        {"easy": "Attention",
         "medium": "We Don't Talk Anymore",
         "hard": "See You Again"},
    "kelly clarkson":
        {"easy": "Because of You",
         "medium": "Breakaway",
         "hard": "Beautiful Disaster"}
    }

LYRICS_DICT = {
    # Contains the lyrics corresponding to the song title
    "Hello":
        "Hello from the __1__ side \n"
        "I must have called a __2__ times \n"
        "To tell you I'm __3__ for everything that I've done \n"
        "But when I call you never seem to be __4__ \n",

    "Rolling in the Deep":
        "There's a __1__ starting in my heart \n"
        "Reaching a __2__ pitch, it's bringing me out the dark \n"
        "Finally I can see you __3__ clear \n"
        "Go ahead and sell me out and I'll lay your __4__ bare \n"
        "See how I leave with every __5__ of you \n"
        "Don't __6__ the things that I will do \n",

    "Someone Like You":
        "I heard that you're settled down \n"
        "That you found a __1__ and you're __2__ now. \n"
        "I heard that your __3__ came true. \n"
        "Guess she gave you __4__ I didn't give to you. \n"
        "Old friend, why are you so __5__? \n"
        "Ain't like you to hold back or hide from the __6__.\n\n"
        "I hate to turn up out of the blue __7__ \n"
        "But I couldn't stay away, I couldn't __8__ it. \n"
        "I had hoped you'd see my __9__ and that you'd be reminded \n"
        "That for me it isn't __10__. \n",

    "Attention":
        "You just want __1__ \n"
        "You don't want my __2__ \n"
        "Maybe you just hate the __3__ of me with someone new \n"
        "Yeah, you just want __1__ \n"
        "I knew from the __4__ \n"
        "You're just making sure I'm never gettin' over you, oh \n",

    "We Don't Talk Anymore":
        "Don't wanna know \n"
        "Kind of __1__ you're wearing tonight \n"
        "If he's holdin' onto you so __2__ \n"
        "The way I did before \n"
        "I __3__ \n"
        "Should've known your __4__ was a __5__ \n"
        "Now I can't get you out of my brain \n"
        "Oh, it's such a __6__ \n",

    "See You Again":
        "It's been a long __1__ without you, my __2__ \n"
        "And I'll tell you all about it when I see you again \n"
        "We've come a long __3__ from where we __4__ \n"
        "Oh, I'll tell you all about it when I see you again \n"
        "When I see you again \n\n"
        "Why'd you have to __5__ so soon? \n"
        "Why'd you have to __6__? \n"
        "Why'd you have to __5__ me when I needed you the most? \n"
        "'Cause I don't really know how to tell ya \n"
        "Without feeling much __7__ \n"
        "I know you're in a __8__ place \n"
        "But it's always gonna __9__ \n\n"
        "Carry on \n"
        "Give me all the __10__ I need to carry on \n",

    "Because of You":
        "Because of you \n"
        "I never stray too far from the __1__ \n"
        "Because of you \n"
        "I learned to play on the __2__ side so I don't get hurt \n"
        "Because of you \n"
        "I find it hard to __3__ not only me, but everyone around me \n"
        "Because of you \n"
        "I am __4__ \n",

    "Breakaway":
        "I'll spread my __1__ and I'll learn how to __2__ \n"
        "I'll do what it takes 'til I touch the __3__ \n"
        "And I'll make a wish, take a chance, make a change \n"
        "And breakaway \n"
        "Out of the __4__ and into the __5__ \n"
        "But I won't forget all the ones that I __6__ \n"
        "I'll take a risk, take a chance, make a change \n"
        "And breakaway \n",

    "Beautiful Disaster":
        "He drowns in his __1__ \n"
        "An __2__ __3__ I know \n"
        "He's as damned as he seems \n"
        "And more __4__ than a __5__ could hold \n"
        "And if I try to __6__ him \n"
        "My whole world could __7__ in \n"
        "It just ain't __8__ \n"
        "It just ain't __8__ \n\n"
        "Oh and I don't know \n"
        "I don't know what he's after \n"
        "But he's so beautiful \n"
        "Such a beautiful disaster \n"
        "And if I could hold on \n"
        "Through the __9__ and the __10__ \n"
        "Would it be beautiful? \n"
        "Or just a beautiful disaster? \n"
    }

ANSWERS_LIST = [
    # Contains the answers to all the songs, with the index of the items
    # corresponding to the blank number in the song
    ["Hello", "other", "thousand", "sorry", "home"],
    ["Rolling in the Deep", "fire", "fever", "crystal", "ship",
     "piece", "underestimate"],
    ["Someone Like You", "girl", "married", "dreams", "things",
     "shy", "light", "uninvited", "fight", "face", "over"],
    ["Attention", "attention", "heart", "thought", "start"],
    ["We Don't Talk Anymore", "dress", "tight", "overdosed", "love",
     "game", "shame"],
    ["See You Again", "day", "friend", "way", "began",
     "leave", "go", "worse", "better", "hurt", "strength"],
    ["Because of You", "sidewalk", "safe", "trust", "afraid"],
    ["Breakaway", "wings", "fly", "sky", "darkness",
     "sun", "love"],
    ["Beautiful Disaster", "dreams", "exquisite", "extreme", "heaven",
     "heart", "save", "cave", "right", "tears", "laughter"]
    ]


# Beginning the game:
def welcome():
    """
    Welcome message to the player
    """
    print "\nHi there! Welcome to 'Fill in the Lyrics Game'."
    name = raw_input("Before we begin, please enter your name. ")
    print ""
    print "Alright " + name + ", are you ready?\n"


def select_artist(ARTIST_LIST):
    """
    Prompts the player to select an artist from the artist list
    Input: list of artists
    Output: the artist selected by the player
    """
    artist = raw_input("Select an artist you'd like to play by typing in his/her FULL name!\n"
                       "Possible choices include Adele, Charlie Puth, and Kelly Clarkson. ")
    artist = artist.lower()  # Makes sure user input is case-insensitive
    print ""
    while artist not in ARTIST_LIST:  # Checks if user input is valid
        print "Oops, that's not an option!"
        artist = raw_input("Select an artist you'd like to play by typing in his/her FULL name!\n"
                           "Possible choices include Adele, Charlie Puth, and Kelly Clarkson. ")
        artist = artist.lower()
        print ""
    return artist


def select_level(LEVEL_LIST):
    """
    Prompts the player to select a difficulty level
    Input: list of difficulty level - easy, medium and hard
    Output: the difficulty level selected by the player
    """
    level = raw_input("Now pick the difficulty level by entering easy, medium or hard. ")
    level = level.lower()
    print ""
    while level not in LEVEL_LIST:  # Checks if user input is valid
        print "Oops, that's not an option!"
        level = raw_input("Now pick the difficulty level by entering easy, medium or hard. ")
        level = level.lower()
        print ""
    return level


def select_no_of_tries(min_guesses, max_guesses):
    """
    Prompts the player to decide how many wrong guesses one can make before one loses
    within the parameters of the min and max number of guesses defined
    Inputs: minimum and maximum number of guesses
    Output: the number of guesses the player chose
    """
    no_of_tries_selected = int(raw_input("How many try/tries would you like to give yourself before you lose?\n"
                                         "You may select up to " + str(max_guesses) + " tries. "))
    print ""
    while no_of_tries_selected < min_guesses or no_of_tries_selected > max_guesses:
        # Checks if user input is valid
        print "Please enter a number from " + str(min_guesses) + " to " + str(max_guesses) + "."
        no_of_tries_selected = int(raw_input("How many try/tries would you like to give yourself before you lose?\n"
                                             "You may select up to " + str(max_guesses) + " tries. "))
        print ""
    return no_of_tries_selected


# Actual game play:
def start_of_game(artist, level, no_of_tries_selected, SONGS_DICT, LYRICS_DICT):
    """
    Prints the song selected and the lyrics to the song
    Inputs: the artist, difficulty level, no. of guesses selected by the player,
            as well as the songs and lyrics dictionaries
    Output: prints the no. of tries the player entered, the song selected,
            and the lyrics to the song
    """
    song = SONGS_DICT[artist][level]
    print "Here we go! You have " + str(no_of_tries_selected) + " try/tries per blank."
    print "Fill in the blanks in the song '" + song + "' below:\n"
    print LYRICS_DICT[song]
    print ""


def answer_check(artist, level, blank_number, guess, SONGS_DICT, ANSWERS_LIST):
    """
    Checks if the player's guess is correct against the answers' list
    Inputs: the artist and difficulty level selected, the blank number being filled,
            the player's guess, the songs dictionary and the list of answers
    Outputs: True if the guess is correct and False if the guess is wrong
    """
    song = SONGS_DICT[artist][level]
    guess = guess.lower()  # Makes sure the player's input is case-insensitive
    for entry in ANSWERS_LIST:
        if entry[0] == song:  # Finds the song in the answers_list
            if entry[blank_number] == guess:  # Checks the player's input against the right answer
                return True
    return False


def replace_blank(artist, level, blank_number, guess, SONGS_DICT, LYRICS_DICT):
    """
    Updates the lyrics with the correct answer entered by the player
    Inputs: the artist and difficulty level selected by the player, the blank number
            being filled, the player's guess, the songs and lyrics dictionaries
    Output: the updated lyrics with the correct answer entered
    """
    song = SONGS_DICT[artist][level]
    guess = guess.lower()  # Makes sure the player's input is case-insensitive
    LYRICS_DICT[song] = LYRICS_DICT[song].replace("__" + str(blank_number) + "__", guess)
    # Replaces the blank with the correct answer and updates LYRICS_DICT
    return LYRICS_DICT[song]


def game_play(artist, level, no_of_tries_selected, SONGS_DICT, LYRICS_DICT, NO_OF_BLANKS):
    """
    Runs the actual game play, getting the player to fill in the blanks one by one
    and ends the game when the player guesses all the blanks correctly or runs out of tries
    Inputs: the artist and difficulty level selected, the no. of tries determined by the player,
            the songs and lyrics dictionaries, and the dictionary of no. of blanks corresponding
            to the difficulty levels
    Output: result of the game
    """
    song = SONGS_DICT[artist][level]
    blank_number, no_of_tries = 1, 0
    while blank_number <= NO_OF_BLANKS[level] and no_of_tries < no_of_tries_selected:
        # Makes sure the game ends when the player guesses all blanks correctly or runs out of tries
        guess = raw_input("What's the word in __" + str(blank_number) + "__? ")
        if answer_check(artist, level, blank_number, guess, SONGS_DICT, ANSWERS_LIST) is True:
            print "\nYou got it right!\n"
            print replace_blank(artist, level, blank_number, guess, SONGS_DICT, LYRICS_DICT) + "\n"
            blank_number = blank_number + 1  # Progresses to the next blank
            no_of_tries = 0  # Resets the no. of tries for the next blank
            if blank_number > NO_OF_BLANKS[level]:  # When the player fills in all blanks correctly
                print "Yay, you won! :)"
        else:
            no_of_tries = no_of_tries + 1  # Reduces the no. of tries the player has left
            if no_of_tries_selected - no_of_tries < 1:  # When the players maxes out on the no. of tries
                print "\nUh oh, you've failed too many guess(es)! Game over. :("
                break
            print "\nNot quite! Try singing the song again in your head."
            print "You have " + str(no_of_tries_selected - no_of_tries) + " try/tries left!\n\n" + LYRICS_DICT[song] + "\n"


welcome()
artist = select_artist(ARTIST_LIST)
level = select_level(LEVEL_LIST)
no_of_tries_selected = select_no_of_tries(1, 5)
start_of_game(artist, level, no_of_tries_selected, SONGS_DICT, LYRICS_DICT)
game_play(artist, level, no_of_tries_selected, SONGS_DICT, LYRICS_DICT, NO_OF_BLANKS)
