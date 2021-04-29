#!/usr/bin/env python3

"""
COMP0015 Quilt
"""
import random
import sys
from ezgraphics import GraphicsWindow

QUILT_WIDTH = 300
QUILT_HEIGHT = 200 
N = 2                       # default dimensions of quilt if no 
                            # selection made by the user

OUTLINE_COLOUR = "black"    # patch outline
FILL_COLOUR = "orange"      # patch colour


def draw_HH(canvas, x, y, width, height):
    """
    Draw pattern HH on the canvas at x, y, with width, height.

    Parameters
    ----------
    canvas : canvas object
        ezgraphics canvas on which we draw the design
    x : int
        x coordinate of top-left of rectangle
    y : int
        y coordinate of top-left of rectangle    
    width : int
        patch width
    height : int
        patch height
        
    """
    canvas.setFill("white")
    canvas.setOutline(OUTLINE_COLOUR)
    canvas.drawRectangle(x, y, width, height)
    canvas.setFill(FILL_COLOUR)
    canvas.drawPolygon(x, y, x+width, y, x, y+height)


def draw_TH(canvas, x, y, width, height):
    """
    Draw pattern TH on the canvas at x, y, with width, height.

    Parameters
    ----------
    canvas : canvas object
        ezgraphics canvas on which we draw the design
    x : int
        x coordinate of top-left of rectangle
    y : int
        y coordinate of top-left of rectangle    
    width : int
        patch width
    height : int
        patch height
        
    """
    canvas.setFill("white")
    canvas.setOutline(OUTLINE_COLOUR)
    canvas.drawRectangle(x, y, width, height)
    canvas.setFill(FILL_COLOUR)
    canvas.drawPolygon(x, y, x, y+height, x+width, y+height)


def draw_HT(canvas, x, y, width, height):
    """
    Draw pattern TH on the canvas at x, y, with width, height.

    Parameters
    ----------
    canvas : canvas object
        ezgraphics canvas on which we draw the design
    x : int
        x coordinate of top-left of rectangle
    y : int
        y coordinate of top-left of rectangle    
    width : int
        patch width
    height : int
        patch height
        
    """
    canvas.setFill("white")
    canvas.setOutline(OUTLINE_COLOUR)
    canvas.drawRectangle(x, y, width, height)
    canvas.setFill(FILL_COLOUR)
    canvas.drawPolygon(x+width, y, x+width, y+height, x, y+height)


def draw_TT(canvas, x, y, width, height):
    """
    Draw pattern TT on the canvas at x, y, with width, height.

    Parameters
    ----------
    canvas : canvas object
        ezgraphics canvas on which we draw the design
    x : int
        x coordinate of top-left of rectangle
    y : int
        y coordinate of top-left of rectangle    
    width : int
        patch width
    height : int
        patch height
        
    """
    canvas.setFill("white")
    canvas.setOutline(OUTLINE_COLOUR)
    canvas.drawRectangle(x, y, width, height)
    canvas.setFill(FILL_COLOUR)
    canvas.drawPolygon(x, y, x+width, y, x+width, y+height)


def draw_quilt(canvas, width, height, n):
    """ 
    Draw a quilt of dimensions width, height with n patches in each row and col.

    Parameters
    ----------
    canvas : canvas object
        ezgraphics canvas on which we draw the design
    x : int
        x coordinate of top-left of rectangle
    y : int
        y coordinate of top-left of rectangle    
    width : int
        patch width
    height : int
        patch height
    n : int
        number of patches in one dimension    
    """
    width = width/n
    height = height/n
    nslice = 0
    symbols = generate_truchet(n, n)
    for x in range (n):
        for y in range (n):
            sliced = symbols[nslice] + symbols[nslice+1]
            nslice +=2
            if sliced == "TT":
                draw_TT(canvas, x*width, y*height, width, height)
            elif sliced == "TH":
                draw_TH(canvas, x*width, y*height, width, height)
            elif sliced == "HT":
                draw_HT(canvas, x*width, y*height, width, height)
            elif sliced == "HH":
                draw_HH(canvas, x*width, y*height, width, height)


def generate_truchet(width, depth):
    """ 
    Return a string of characters. Each pair of characters in the string represents a
    Truchet tile.

    The symbol for a truchet tile must be one of the options: HH, HT, TH, TT. 
    The number of symbols in the string will be equal to the number of 
    patches in the quilt. The number of patches = width x depth.

    Parameters
    ----------
    width : int
        Width of the quilt in number of patches.
    depth : int
        Depth of the quilt in number of patches.

    Returns
    -------
    str
        truchet values
    """
    symbols = ''
    myList = ["T", "H"]
    n = 2*width*depth
    for x in range (n):
        symbols += random.choice(myList)
    return symbols
        

def main():

    # DO NOT EDIT THIS CODE
    # main() is lengthy because we are handling all the test cases.
    n = N                   # default value for number of patches
    width = QUILT_WIDTH     # default value for quilt width in pixels
    height = QUILT_HEIGHT   # default value for quilt height in pixels

    args = sys.argv[1:]
    if len(args) < 1 or len(args) > 4:
        print('usage: (one of -TT -TH, -HT, -HH, -quilt) [n] [width] [height]')
        return    

    # Parse [n]/[width]/[height] from command line, giving a helpful
    # error message if it fails.

    try:
        if len(args) > 1:
            n = int(args[1])
            print("n is: ", n)

        if len(args) > 2:
            width = int(args[2])
            height = int(args[3])
    except Exception:
        print("Error parsing int n/width/height from command line:" + ' '.join(args))
        return

    if args[0] == '-HH':
        win = GraphicsWindow(width * 2, height * 2)
        canvas = win.canvas()
        draw_HH(canvas, 0, 0, width, height)
        draw_HH(canvas, width, height, width, height)
    elif args[0] == '-HT':
        win = GraphicsWindow(width * 2, height * 2)
        canvas = win.canvas()
        draw_HT(canvas, 0, 0, width, height)
        draw_HT(canvas, width, height, width, height)
    elif args[0] == '-TH':
        win = GraphicsWindow(width * 2, height * 2)
        canvas = win.canvas()
        draw_TH(canvas, 0, 0, width, height)
        draw_TH(canvas, width, height, width, height)
    elif args[0] == '-TT':
        win = GraphicsWindow(width * 2, height * 2)
        canvas = win.canvas()
        draw_TT(canvas, 0, 0, width, height)
        draw_TT(canvas, width, height, width, height)
    else: # args[0] is assumed to be -quilt
        win = GraphicsWindow(width, height)
        canvas = win.canvas()
        draw_quilt(canvas, width, height, n)

    win.wait()

if __name__ == "__main__":
    main()
