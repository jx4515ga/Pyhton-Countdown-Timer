
import time



#user input time in seconds
user_time = input("How long would you like to set the timer for? : ")


# define the countdown function, using the user time in seconds.
def countdown(user_time):
    
    while user_time:
        mins, secs = divmod(user_time, 60)
        hours = int(user_time / 3600)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        user_time -= 1
    #message to aler user
    print('Wake up! Times up')
  
  

  

countdown(int(user_time))