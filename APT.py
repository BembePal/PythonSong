from time import sleep
import sys
def print_lyrics():

    lines = [
        ("Uh-Huh, Uh-Huh", 0.17),
        ("\nKissy face, Kissy face", 0.25),
        ("Sent to your phone, but", 0.15),
        ("I'm tryna kiss your lips for real", 0.1),
        ("\nUh-Huh, Uh-Huh", 0.17),
        ("\nRed hearts, red hearts", 0.15),
        ("That's what I'm on, yeah", 0.17),
        ("Come give me somethin' I can feel, oh-oh, oh", 0.25),
        ("\nDon't you want me like I want you, baby?", 0.27),
        ("Don't you need me like I need you now?", 0.27),
        ("Sleep tomorrow, but tonight, go crazy", 0.35),
        ("All you gotta do is just meet me at the", 0.29),

        ("\n아파트, 아파트", 0.15),
        ("아파트, 아파트", 0.15),
        ("아파트, 아파트", 0.15),
        ("\nUh-Huh, Uh-Huh", 0.17),
        ("\n아파트, 아파트", 0.15),
        ("아파트, 아파트", 0.15),
        ("아파트, 아파트", 0.15),
        
    ] 
             #uhuh   kiss  send  I'm     uhuh   redHeart  that's  come    dontbaby  dont    sleep    all     apateu           uhuh        apateu
    delays = [0.60, 0.55,  .85,   1.5,    0.6,    0.6,    1.1,     0.64,    0.60,      0.60,    0.9,     0.8,   1.2,1.2,1.2,     1.5,     1.2,1.2,1.2 ]

    for i, (line, char_delay) in enumerate(lines):
        words = line.split(" ")
        for word in words:
            if "baby" in word.lower():
                print("\033[31m" + word + "\033[0m", end=' ')
            elif "hearts" in word.lower():
                print("\033[31m" + word + "\033[0m", end=' ')
            else:
                print(word, end=' ')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])
        print('')
print_lyrics()
