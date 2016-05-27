class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

same_old = Song(["Take away your things and go You can't take back what you said, I know"
                   ])

stiches_shawn = Song(["And now that I'm without your kisses.I'll be needing stitches",
                      ])

same_old.sing_me_a_song()
stiches_shawn.sing_me_a_song()
