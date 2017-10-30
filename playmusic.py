from pygame import mixer # Load the required library

x = raw_input("Play?")
if x:
    mixer.init()
    mixer.music.load('f:/Music/DJ Snake - Middle ft. Bipolar Sunshine.mp3')
    mixer.music.play()


y = raw_input("end?")