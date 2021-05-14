import os
import vlc
import random

def playsong(mood):
    
    while True:
                     
        songlist=os.listdir('music/'+mood)
        h=random.randrange(0,len(songlist),1)
        song=songlist[h]
        player=vlc.MediaPlayer('music/'+mood+'/'+song)
        print('music/'+mood+'/'+song)
        player.audio_set_volume(80)
        player.play()
        inn=input('press n for next song and e to exit')
    
        if 'n' in inn:
            player.stop()

            if(h==len(songlist)-1):
                h=0
            else:
                h=h+1
            
        elif 'e' in inn:
            player.stop()
            break
        
