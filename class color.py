class color(object):
    """Represents a color"""

color_1= color()
color_1.r = '0'
color_1.g = '204'
color_1.b = '0'
color_1.name = 'green'

color_2 = color()
color_2.r = '0'
color_2.g = '0'
color_2.b = '255'
color_2.name = 'royal blue'

color_3 = color()
color_3.r = '255'
color_3.g = '102'
color_3.b = '178'
color_3.name = "pink"

color_s = [color_1,color_2, color_3]
print type(color_s)
for color in color_s:
    print color.name

