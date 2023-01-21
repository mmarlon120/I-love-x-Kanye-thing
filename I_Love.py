from gtts import gTTS
import os

x = input("Who do you miss?\n")

if x == "Kanye":
  print("https://www.youtube.com/shorts/ch8g-sJb6ow")
  exit(0)

counter = 0
while True:
  lang = int(input("Choose the accent\n(1)=American\n(2)=British\n(3)=Irish\n(4)=Australia\n(5)=Canadian\n(6)=Indian\n(7)=African\n"))
  if counter > 2:
    print(f"Fuck you {x} we didn't miss you")
    exit(248)
  elif lang not in{1, 2, 3, 4, 5, 6, 7}:
    print("thats not an accent")
    counter = counter + 1
  else:
    break
#  lang = int(input("Choose the accent\n(1)=American\n(2)=British\n(3)=Irish\n(4)=Australia\n(5)=Canadian\n(6)=Indian\n(7)=African\n"))

langlist = ["us", "co.uk", "ie", "com.au", "ca", "co.in", "co.za"]
accent = langlist[lang-1]

lyrics = (f"I miss the old {x}, straight from the 'Go {x} \nChop up the soul {x}, set on his goals {x} \nI hate the new {x}, the bad mood {x} \nThe always rude {x}, spaz in the news {x} \nI miss the sweet {x}, chop up the beats {x} \nI gotta to say at that time I'd like to meet {x} \nSee I invented {x}, it wasn't any {x}s \nAnd now I look and look around and there's so many {x}s \nI used to love {x}, I used to love {x} \nI even had the pink polo, I thought I was {x} \nWhat if {x} made a song about {x} \nCalled 'I Miss The Old {x}', man that would be so {x} \nThat's all it was {x}, we still love {x} \nAnd I love you like {x} loves {x}") 

tts = gTTS(lyrics, lang = 'en', tld = accent)
tts.save("I Love " + x)
print(lyrics)


