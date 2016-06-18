path = '~/stimuli/movies/object3dv2/';
obj = 'obj2';

d = dir([path obj '*.mov']);

for i = 1:length(d)
   vr = VideoReader(fullfile(path,d(i).name));
   offset = vr.Width-vr.Height*1.5-6;
   
   data = vr.read(1);
   data = imresize(data(:,ceil(offset/2):vr.Height*1.5+floor(offset/2),:),1.184);
   imwrite(data,fullfile(path,sprintf('%s_%02u.jpeg',obj,i)))
    
    
end

%%
names = [];

d = dir('images/obj1*');
for i = 1:length(d)
    
    names = [names ', "images/' d(i).name '"'];
    
end