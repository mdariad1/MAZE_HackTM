
import glob

sprite_images = []
for filename in glob.glob('images/*.gif'): #assuming gif
    filename = filename.replace('images\\', '')
    sprite_images.append(filename)

print(sprite_images)


# sprite_images = ["player-left.gif",
#                  "player-right.gif",
#                  "jungle.gif",
#                  "gold.gif", "enemy-left.gif", "enemy-right.gif"]
