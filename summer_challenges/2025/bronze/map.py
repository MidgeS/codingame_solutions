from tileType import TileType 

class Map:
    __width = 0
    __height = 0
    __cells = []

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        for i in range(width*height):
            self.__cells.append(TileType.EMPTY)

    def getHeight(self):
        return self.__height
    
    def getWidth(self):
        return self.__width

    def getIndex(self,x,y):
        return y*self.__width + x

    def setCell(self,x,y,type):
        index = self.getIndex(x,y)
        self.__cells[index] = type

    def getCell(self,x,y):
        if(x < 0 or x > self.__width or y < 0 or y > self.__height):
            return -1
        
        index = self.getIndex(x,y)
        return self.__cells[index]
    
    def printMap(self):
        for y in range(self.__height):
            line = ""
            for x in range(self.__width):
                line += str(self.getCell(x,y))