# grayscale.py

from graphics import *

def main():
    print("This program converts an image (GIF or PPM) to grayscale.")
    infile_name = input("Enter the file name: ") # Must include extension

    print("Click on the image to transform to grayscale.")

    # Set up window
    width = 1000
    height = 1000

    win = GraphWin("Image", width, height)

    # Display original image
    infile = Image(Point(width/2, height/2), infile_name)
    infile.draw(win)

    # Convert to grayscle on click
    win.getMouse()

    cols = infile.getWidth()
    rows = infile.getHeight()

    for y in range(0, rows):
        for x in range(0, cols):
            r, g, b = infile.getPixel(x, y)
            brightness = int(round(0.299*r + 0.587*g + 0.114*b))
            infile.setPixel(x, y, color_rgb(brightness, brightness, brightness))
        win.update()

    # Save new file
    outfile_name = input("Enter the save file name: ") # Must include extension

    infile.save(outfile_name)
            
    # Close window and program
    print("Click on image to save and close.")
    
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
