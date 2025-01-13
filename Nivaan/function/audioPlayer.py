from pygame import mixer as mx
import time

def playMusic(fileName):
  mx.init()
  mx.music.load(fileName)
  mx.music.set_volume(1)
  mx.music.play()
  # while mx.music.get_busy():
  #       time.sleep(1)
  # infinite loop 
  while True: 
      
    print("Press 'p' to pause, 'r' to resume") 
    print("Press 'e' to exit the program") 
    query = input("  ") 
      
    if query == 'p': 
  
        # Pausing the music 
        mx.music.pause()      
    elif query == 'r': 
  
        # Resuming the music 
        mx.music.unpause() 
    elif query == 'e': 
  
        # Stop the mixer 
        mx.music.stop() 
        break


playMusic(r"C:\Users\Lenovo\OneDrive\Desktop\TechUp\Nivaan\function\Our-God-Is-Good.mp3")