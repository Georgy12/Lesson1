talk={'hi':'hello','how are you?':'fine thanks','goodbye':'see you'}


def get_answer(question,talk):
	return talk.get(question)
def ask_user(talk):
	while True:
		user_input=str(input('Say something:'))
		talk=str(get_answer(user_input,talk))
		print(talk)
		if user_input=='goodbye':
  			break
ask_user(talk)  			
