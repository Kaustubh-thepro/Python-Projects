import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle



class Rectangle(object):

    def __init__(self, xy = (0,0), length=4,width = 10, color = "Red"):
        self.xy =xy
        self.length = length
        self.width = width
        self.color = color

    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle(self.xy,self.length,self.width, fc = self.color))
        plt.axis('scaled')
        plt.show()

redrect = Rectangle((200,100),70,30, 'purple')
SkinnyBlueRectangle = Rectangle((0,0),2, 3, 'blue')
SkinnyBlueRectangle.drawRectangle()
redrect.drawRectangle()
