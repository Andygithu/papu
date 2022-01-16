import tkinter as tk
from tkinter.constants import BOTTOM, RIGHT


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right,scene_bottom):

    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """

    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    # tree_center = scene_left + 500
    # tree_top = scene_top + 100
    # tree_height = 150
    # draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    draw_sky(canvas)
   
    draw_cloud(canvas,scene_left,scene_top,scene_right,scene_bottom,120)
    draw_sun(canvas)
    draw_tree(canvas,scene_left,100)
    draw_stem_tree(canvas,scene_left,100)
    draw_ground(canvas)
    #Draws the snow man body
    draw_snow_man(canvas,600,200,scale = .75)
    draw_snow_man(canvas,590,270,scale = 1)
    draw_snow_man(canvas,570,350,scale= 1.5)
    #Bottons
    draw_snow_man(canvas,630,280,scale= .2)
    draw_snow_man(canvas,630,320,scale= .2)
    #nose
    draw_snow_man(canvas,600,240,scale= .2)
    #eyes
    draw_snow_man(canvas,620,220,scale= .1)
    draw_snow_man(canvas,650,220,scale= .1)

    


    draw_ground(canvas)
    draw_arms(canvas,600,500)
    draw_arms(canvas,680,760)

    

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.
def draw_snow_man(canvas,left,top,scale = 1,color='#D3FFF3'):
    width = 100 * scale
    height = 100 * scale
    right = left + width
    bottom = top + height
    color = '#D3FFF3'

    canvas.create_oval(left,top,right,bottom,fill = color)
def draw_arms(canvas,left,top):
   
    canvas.create_line(left,300,top,250)
    

def draw_sky(canvas):
    canvas.create_rectangle(0,0,799,499,fill = '#90DDF0')
def draw_ground(canvas):
    canvas.create_rectangle(0,499,799,450,fill = '#230C0F')
def draw_cloud(canvas,left,top,right,bottom,grid_spacing):
    for i in  range(left,right,grid_spacing):
      canvas.create_oval(i,0,i + 290,100,fill = '#F1F7EE')
    for i in  range(left,right,grid_spacing):
      canvas.create_oval(i+10,160,i + 200,75,fill = '#F1F7EE')
def draw_sun(canvas):
    canvas.create_oval(-70,-70,150,150,fill = '#F0F757')
def draw_tree(canvas,left,grid_spacing):
    for i in range(left,300,grid_spacing):
      canvas.create_oval(i,499,i+100,200,fill='#81E979')
def draw_stem_tree(canvas,left,grid_spacing):
    for i in range(left,300,grid_spacing):
        canvas.create_rectangle(i+40,499,i+60,270,fill ='#523A34')

# def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    # """
    # trunk_width = height / 10
    # trunk_height = height / 8
    # trunk_left = peak_x - trunk_width / 2
    # trunk_right = peak_x + trunk_width / 2
    # trunk_bottom = peak_y + height

    # skirt_width = height / 2
    # skirt_height = height - trunk_height
    # skirt_left = peak_x - skirt_width / 2
    # skirt_right = peak_x + skirt_width / 2
    # skirt_bottom = peak_y + skirt_height

    # # Draw the trunk of the pine tree.
    # canvas.create_rectangle(trunk_left, skirt_bottom,
    #         trunk_right, trunk_bottom,
    #         outline="gray20", width=1, fill="tan3")

    # # Draw the crown (also called skirt) of the pine tree.
    # canvas.create_polygon(peak_x, peak_y,
    #         skirt_right, skirt_bottom,
    #         skirt_left, skirt_bottom,
    #         outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()