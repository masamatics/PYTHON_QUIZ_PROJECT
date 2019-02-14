
restart = 1

list_of_blanks = ["___1___", "___2___", "___3___", "___4___"]

game_data = {

	'1': {
		'string': "Never gonna ___1___ you up, Never gonna ___2___ you down, Never gonna ___3___ around, and ___4___ you",
		'answer': [["___1___", "GIVE"], ["___2___", "LET"], ["___3___", "TURN"], ["___4___","DESERT"]]
	},
	'2': {
		'string': "The ___1___ thing isn't really real. Don't forget, I'm also just a ___2___, standing in front of a ___3___, asking him to ___4___ her.",
		'answer': [["___1___", "FAME"], ["___2___", "GIRL"], ["___3___", "BOY"], ["___4___", "LOVE"]]
	},
	'3': {
		'string': "___1___ is more important than knowledge. The important thing is not to stop ___2___. ___3___ has its own reason for existing. Anyone who has never made a ___4___ has never tried anything new.",
		'answer': [["___1___", "IMAGINATION"], ["___2___", "QUESTIONING"], ["___3___", "CURIOSITY"], ["___4___","MISTAKE"]]
	}
}

output_message = {
	
		"1": "\n****************** Level 1: A SONG *******************\n",
		"2": "\n****************** Level 2: A MOVIE ******************\n",
		"3": "\n************* Level 3: ALBERT EINSTEIN ***************\n"
}


#word_in_pos function
#output the blank in the right format to be replaced. 
def word_in_pos(word, list_of_answers):
	for pos in list_of_answers:
		if pos in word:
			return pos
	return None

#Code to be used in the play_game function
#This will validate the answer and output the correct answer. 
#This function meet the below criteria:
#When player guesses incorrectly, they are prompted to try again
def answers_validation(blank_number, user_answer, check_list):
	
	while [blank_number, user_answer.upper()] not in check_list:

		if [blank_number, user_answer.upper()] in check_list:
			break
		else:
			print "Incorrect! Try Again!"
			user_answer = raw_input("Answer for " + blank_number + ": ")

	print "Correct!\n"
	return user_answer
	

#Code to be used in the play_game function
#This will be used just for output style
def final_answer_style(output):
	print "\n****************** Correct Answer **********************\n"
	print output
	print "\n******** This is the end of the game...******************\n"


#Code for the game
#This function meet the below criteria:
#When player guesses correctly, new prompt shows with correct answer in the previous blank 
#  and a new prompt for the next blank

def play_game(ml_string, list_of_answers, correct_answer):
	full_answer = []
	print ml_string
	ml_string = ml_string.split()

	for word in ml_string:

		replacement = word_in_pos(word, list_of_answers)

		if replacement != None:

			print "\n"

			user_input = raw_input("Answer for " + replacement + ": ")

			word = word.replace(replacement, answers_validation(replacement, user_input, correct_answer))
			full_answer.append(word)
			partial_answer = full_answer + ml_string[len(full_answer):]
			partial_answer = " ".join(partial_answer)
			print partial_answer

		else:
			full_answer.append(word)
	
	full_answer = " ".join(full_answer)

	final_answer_style(full_answer)



#User input game level and output the game level
#User select from 1 - 3 or enter n or N to exit this program. 
#Loop until the user input the desired number.
#This function meet the below criteria:
#Immediately after running the program, user is prompted to select a difficulty level from easy or 1/ medium or 2/ hard or 3
def select_level():
	print "Enter a difficulty level from 1 through 3. If you want to quit, enter N."
	level_selected = raw_input("Enter: ")
	while level_selected not in ['1', '2', '3', 'n', 'N']:
			print "Error. Select between 1 and 3."
			level_selected = raw_input("Enter a difficulty level from 1 through 3: ")
	return level_selected




#Depending on the user's input on select_level function, the game will provide different level of questions. 
#This function meet the below criteria:
#Once a level is selected, game displays a game_level and a prompt to fill in the first blank.

def start():
	level = select_level()
	if level in ['1', '2', '3']:
		print output_message[level]
		return play_game(game_data[level]['string'], list_of_blanks, game_data[level]['answer'])
	else:
		print "\nGoodbye!\n"
		exit()
	
	

# The beginning of this program
print "\n**************** Welcome to Masa's Quiz. ******************\n"

#To ask if player wants to continue the game after finishing a question
while restart!="x":
    start()
    restart = raw_input("press any key to start again, or x to exit.")


