#!/usr/bin/python3
import random
import time
import os

running = True

def clear_scr() -> None:
    os.system("clear")

class CoinFlip:
    def __init__(self, choices) -> None:
        self.choice_1 = choices[0]
        self.choice_2 = choices[1]
        self.result = None
        self.tails = r"""
                    ---:::..:                    
              -=++=-:.    ..-===--:              
           :+=:.                 .-+=-           
         =+.  .                     .-+:         
       =+-  -=-=+.                     -+-       
     -+-    +-+++=                      .-=      
    -=.      ..:+:                       .=+:    
   -=        .-+-                          :=    
   +:     .:=+++.                           =+   
  =:     .=++++:  .::==  =-:-:.             .+:  
  +.    :+++++=      .+.+:   :: +.+-::.:-    -+  
 =+    :++++++.     .+..+.   :- ++. :+=+.    .*- 
 ==   .+++++++.   .:=:...+..:+. +.==:+..+.    +- 
 ==  .=+++++++-                               +- 
 -+. .++++==+++-.                            .+- 
  +. .+++++=++=++-..                         .+  
  =-  :+++++=+=++==+==--:...       .... ....:+:  
   +:  =+++++++=+==++===++++++++++++++++++++++   
   .+.  .=++++++++++++++++++++++++++++++++==+    
    :+.  ...=+++++++++++++++++++++++++++===+.    
      +=.         ...::-==++++++==-:---:.+-      
       :+:                           . -+.       
        .-+-.                       .-+:.        
          ..=*-.                ..=*=..          
             .:=**+=:......::=*#+-...            
                ..:-=**##**+=-:..                
                        .         
        """

        self.heads = r"""
                    .........                    
               .:-=-.:.    ..:-+-..              
            .--.                  -=:.           
          :=.                        .=.         
       .:+.      ..:-========-..       .=.       
      .+..      .======+=+++++==.        :-      
     :-       .-++++++++++++++++=         .=.    
    :-        .++====+=+++++++++=-.        :=    
   .+.        .+==++===+=++++++=+=:         --.  
  .-:         :==++++=++==+++=-====:        .+.  
  .+.         =++++=+++++===++*++==:         ::  
  .-          :+++++=+==+++++=====+=:        .-. 
  .-          .++++++=++++++++++++===:       .=. 
  .=.          .++==+++=+=+++++++++:..       .-. 
  .+.           =++++=+++++++++++++-         =:  
   .:           =++++++++++++++++++:        .+.  
   .=.          =++++++++++++++++++.       .=.   
    .=.          .+*+++++++++++++-.       .=:    
    ..=:            .:=*++++++.          .=:     
      .-+.                ..            :+.      
       ..=-.                         .:+:.       
        ...=+.                     .=+..         
          ...-+*-..            .-+=:..           
             ...:=*###*+++***+-....              
                  .............                                        
        """

        self.coinflip()
        self.animate()
        self.print_result()
        self.end_menu()

    def coinflip(self) -> None:
        self.result = random.choice([self.choice_1, self.choice_2])

    def animate(self) -> None:
        clear_scr()
        for i in range(0, 5):
            print(self.heads)
            time.sleep(0.2)
            clear_scr()
            print(self.tails)
            time.sleep(0.2)
            clear_scr()

    def print_result(self) -> None:
        if (self.result == self.choice_1):
            print(self.heads)
            print("Du må gjøre: ")
            print(self.choice_1)
        
        elif (self.result == self.choice_2):
            print(self.tails)
            print("Du må gjøre: ")
            print(self.choice_2)

    def end_menu(self) -> None:
        global running
        choice = input("\n[y]\tSpin igjen?\n[i]\tSpin igjen med samme valg\n[enter] Exit\n\nDitt valg: ")
        match(choice):
            case 'y':
                clear_scr()
                CoinFlip(choices())
            case 'i':
                clear_scr()
                CoinFlip([self.choice_1, self.choice_2])
            case _:
                clear_scr()
                running = False
                return

def choices() -> [str]: 
    choices = []
    choice_1 = input("Legg inn et valg: ")
    choice_2 = input("Legg inn enda et valg: ")
    choices.append(choice_1)
    choices.append(choice_2)
    return choices

def main() -> None:
    while (running):
        CoinFlip(choices())

if __name__ == '__main__':
    main()