from pipeline import vis
import os

path = 'stimuli/'
key = dict([('movie_name', 'obj1v4')])

clips, names = (vis.Movie.Clip() & key).fetch['clip_number', 'file_name']
for iclip in clips:
    if not os.path.isfile(path+names[iclip-1]):
        (vis.Movie.Clip() & key.update(clip_number=iclip)).fetch1['clip'].tofile(path+names[iclip-1])



