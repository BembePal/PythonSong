from time import sleep
import sys

def print_lyrics():
    lines = [
        ("Oh-oh-oh-oh-oh-oh",0.14),#1
        ("Oh-oh-oh-oh-oh-oh",0.14),#2
        ("Uptown girl", 0.09),#3
        ("She's been living in her uptown world", 0.075),#4
        ("I bet she never had a back street guy?", 0.050),#5
        ("I bet her mama never told her why", 0.065),#6
        ("I'm gonna try for an uptown girl(uptown girl)", 0.04),#7
        ("She's been living in her white bread world", 0.05),#8
        ("As long as anyone with hot blood can", 0.05),#9
        ("And now she's looking for a downtown man", 0.05),#10
    ]
             
    delays = [1,1,1, 0.90, 1.30, 1.60, 1.50, 1.50, 1.40, 1.60]



              
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])
        print('')

# Call the function
print_lyrics()
