import pyglet
vidPath='/Users/manolis/github/Python/obj1.mov'
window = pyglet.window.Window()
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vidPath, streaming=False)

player.queue(MediaLoad)
player.play()

@player.event
def on_eos():
    print('video end')

@window.event
def on_draw():
    window.clear()
    if player.source and player.source.video_format:
        player.get_texture().blit(0,0)

@window.event
def on_mouse_press():
    window.close()

pyglet.app.run()