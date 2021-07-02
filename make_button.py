from PIL import Image

alarm = 1
 
if alarm == 1:
    img = Image.new('RGB', (2, 2), color = 'red')
else:
    img = Image.new('RGB', (2, 2), color = 'green')


img.save('/srv/http/button_color.png')
