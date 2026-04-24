import shutil
import threading
from threading import Thread, Event

# set route
original = r'E:\\Visualstudio\\Work_Projects\\Excel_projects\\Auto_save_file\\ttss.xlsx'
target = r'E:\\Visualstudio\\Work_Projects\\Excel_projects\\Auto_save_file\\Auto_save_file_copy\\copy_ttss.xlsx'

# defines a custom thread class MyThread that inherits from the built-in Thread class in Python's threading module. 
# The __init__ method initializes an instance of the class and takes an argument event which is an instance of the Event class.
class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event
# The run method is overridden to define the behavior of the thread when it is started. 
# Inside the run method, there is a while loop that runs until the stopped event is set, 
# which is initially set to False. 
# This while loop runs every 3 seconds and copies a file from original to target using the shutil.copyfile method, 
# and then prints "Guardando" (which means "Saving" in Spanish) to the console.
    def run(self):
        while not self.stopped.wait(3):
            shutil.copyfile(original, target)
            print("Guardando")

# Finally, an instance of Event class is created and passed to an instance of MyThread as an argument. 
# The thread is then started using the start() method.
my_event = Event()
thread = MyThread(my_event)
thread.start()               

#stops
#my_event.set()