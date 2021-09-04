import pyttsx3
from pydub import AudioSegment
import sys
import math
import shutil
import os

MAX_STRING_LENGHT = 4980
# 4990
engine = pyttsx3.init() # object creation  """ RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate                #printing current voice rate
engine.setProperty('rate', 160)     # setting up new voice rate  
# """VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
                       #printing current volume level
engine.setProperty('volume',1)    # setting up volume level  between 0 and 1  """VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice

engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female  # engine.say("xin chào Các bạn!")
# engine.say('Tỉ lệ giộng nói của tôi lúc này là ' + str(rate))
# engine.runAndWait()
# engine.stop()  """Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('xin chào Các bạn!', 'test.mp3')
stringTemp = sys.argv[1] 
# stringTemp = "xin chào các bạn nha"
def convert(str):
    try:
        names = ''
        
        # get string lenght, subString lenght
        group = len(str)//MAX_STRING_LENGHT
        if group == 0:
            group = 1
        strLenght, subStringLenght = len(str), len(str)//group

        # remove folder temp & all sub files
        try:
            shutil.rmtree('voices')
        except Exception as e:
            print(e)
        try:
            os.mkdir("voices")
        except Exception as e:
            print(e)

        # create folder temp
       

        # AudioSegment.ffmpeg = 'C:/ffmpeg/bin/ffmpeg.exe'
        # AudioSegment.ffprobe = 'C:/ffmpeg/bin/ffprobe.exe'

        # make split mp3 file, because max lenght input of func 'save_to_file' is 4998
        for i in range(0, strLenght, subStringLenght):
            pathFile = "voices/%d.mp3" %(i)
            names=names+';'+pathFile
            subStr = str[i:i+subStringLenght]
            engine.save_to_file(subStr, pathFile)

            # sound = AudioSegment.from_file(file=pathFile, format="mp3") 
            # combined_wav += sound  
            
    except Exception as e:
        print(e)
    engine.runAndWait()
    return 'return'+names
print(convert(stringTemp))

sys.stdout.flush()