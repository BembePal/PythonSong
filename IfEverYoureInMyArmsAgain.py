from time import sleep
import sys
# ANSI escape codes for colors
green = '\033[92m'

# Reset color
reset = '\033[0m'

def print_lyrics():
    lines = [
        ("The best of romances", 0.08), 
        ("Deserve second chances", 0.07), 
        ("I'll get to you somehow", 0.06), 
        ("'Cause I promise now", 0.07), 
        ("If ever you're in my arms again", 0.13),  
        ("This time I'll love you much better", 0.09),  
        ("If ever you're in my arms again", 0.13),  
        ("This time I'll hold you forever", 0.09), 
        ("This time we'll never end", 0.1)

    ]
             
    # Calculated delays in seconds, divided by 2.5
    delays = [0.65, #romaces -> deserve
              0.86, #deserve -> somehow
              0.65, #somehow -> promise now
              1.75, #promise now -> arms again
              1.0, #arms again -> much better
              1.3, #much better -> arms again2
              1.2, #arms again2 -> forever
              1,#forever -> end
              1]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(green + char + reset, end='')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])
        print('')

# Call the function
print_lyrics()
