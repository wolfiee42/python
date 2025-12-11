

import threading
import time

def walk_dog(first, second):
    time.sleep(8)
    print(f"You finish walking {first} {second}")
    

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")
    
    
def get_mail():
    time.sleep(4)
    print("You get the mail")
    
chore01 = threading.Thread(target=walk_dog, args=("scooby", "doo"))
chore01.start()

chore02 = threading.Thread(target=take_out_trash)
chore02.start()

chore03 = threading.Thread(target=get_mail)
chore03.start()


chore01.join()
chore02.join()
chore03.join()


print("All chores are complete!")