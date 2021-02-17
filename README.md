# Human-Robot-Interaction
This repository is about Human-Robot interaction. It uses Google Cloud API for speech recognition, parser Spacy. Programming language - Python 3.6.
---------------------------------
I met folloving error: 
"Microsoft Visual C++ 14.0 is required".

To install spacy you'll need to install also MS Visual Studio C++ 14.0 Build tools.
It is possible to solve by the following way:

Use the link to Visual C++ 2015 Build Tools ( http://go.microsoft.com/fwlink/?LinkId=691126&fixForIE=.exe. ). That will install Visual C++ 14.0 without installing Visual Studio and will save your hard memory.

---------------------------------
Very big stuck I had with text-to-speech file playing. I solved it by the following way: just asked the OS to play this file using my default music player (AIMP3)

---------------------------------
Still I have a problem, which I didn't solve: when I use in the program not only my voice, but the program also tells me a story/ask some questions, algorythm recognizes computer speech together with my and sometimes mix it. Sometimes it starts to overwork not my words, but words which were told by computer. It's so stupid. I solved this problem by using an external microphone from my headphones.

---------------------------------
Program automatically creates 'temp.mp3' file in the path of program file. Don't worry, it will be only one file, which will always contain only information from the last speech of the bartender.
