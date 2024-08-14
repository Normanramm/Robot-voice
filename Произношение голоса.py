import pyttsx3

# Произношение текста 
friend = pyttsx3.init()
voices = friend.getProperty('voices')
friend.setProperty('voice', voices [1].id)
friend.say("Harshit, You are superb. Also, I am your subscriber and I like your videos too muc")
friend.runAndWait()
friend. stop()