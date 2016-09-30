#phrases={'hi':'hello','how are you?':'fine thanks','goodbye':'see you'}
#def get_answer(key,phrases):
#	return phrases.get(key)
#def ask_user(phrases):
#	while True:
#		try:
#			user_input=str(input('Введите сообщение:'))
#			print(talk)
#			if user_input=='goodbye':
#				break 

	
#		except KeyboardInterrupt:
#			return "Уже уходите?"				
#ask_user(phrases)




phrases={'hi':'hello','how are you?':'fine thanks','goodbye':'see you'}


def get_answer(key,phrases):
  return phrases.get(key)


def ask_user(phrases):
  while True:
    try:
	    user_input=str(input('Введите сообщение:'))
	    talk=get_answer(user_input,phrases)
	    print(talk)
	    if user_input=='goodbye':
	        break 
    except KeyboardInterrupt:
      print("Уже уходите?")	
      break


if __name__=='__main__'      
ask_user(phrases)