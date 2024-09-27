
from tkinter import *
from tkinter import simpledialog
import time

player_1_title= 'Player 1'

player_2_title= 'Player 2'





def change_name():
    global player_1_title,player_2_title

    left_name= str(left_entry.get())
    player_1_title= left_name

    right_name= str(right_entry.get())
    player_2_title= right_name

    if left_name == '':
        player_1_title = 'Player 1'

    if right_name == '':
        player_2_title = 'Player 2'


    root.destroy()




root= Tk()
root.title("PyPong")
root.geometry('500x230')
root.config(bg='light blue')


window_title= Label(root,text= 'ENTER PLAYER NAMES',font=('comic sans',30),bg='light green')
window_title.pack()
    #-----------------------
    #top labels & Entry boxes

left_label= Label(root,text='Player 1 Name',font=('arial',10,'bold')).pack(side= 'left',anchor='w')
right_entry = Entry(root)
right_entry.pack(side='right', anchor='e')

right_label=Label(root,text='Player 2 Name',font=('arial',10,'bold')).pack(side='right',anchor='e')
left_entry= Entry(root)
left_entry.pack(side='left',anchor='w')
    #-------------------------------------------------------
    #submit button

submit_names= Button(text='SUBMIT',font=('arial',10,'bold'),fg='green',bg='light blue',width=100,command=change_name)
submit_names.pack(side='bottom')

root.mainloop()



def add_points_left():

    current = int(player_1.get())
    new_score = current + 1
    player_1.set(str(new_score))
    window.update()
    window.after(10000000, add_points_left)

def add_points_right():
    current = int(player_2.get())
    new_score = current + 1
    player_2.set(str(new_score))
    window.update()
    window.after(10000000, add_points_right)


def ball_moving():
    global xVelocity,yVelocity,ball,ball_size,width,height

    while True:
        coordinates= canvas.coords(ball)
        left_paddle_coord= canvas.coords(left_paddle)
        right_paddle_coord= canvas.coords(right_paddle)

        if coordinates[0]>= (width-ball_size):  #bounce off walls
            xVelocity= -xVelocity
            add_points_left()      #add points

        if coordinates[0] <= 0:
            xVelocity = -xVelocity
            add_points_right()      #add points

        if coordinates[1]>= (height-ball_size): #bounce off walls
            yVelocity= -yVelocity

        if coordinates[1] <= 0:
            yVelocity = -yVelocity

        if (coordinates[2] >= canvas.coords(left_paddle)[0] and coordinates[0] <= canvas.coords(left_paddle)[2]) and \
                (coordinates[3] >= canvas.coords(left_paddle)[1] and coordinates[1] <= canvas.coords(left_paddle)[3]):
            xVelocity = abs(xVelocity)

        if (coordinates[2] >= canvas.coords(right_paddle)[0] and coordinates[0] <= canvas.coords(right_paddle)[2]) and \
                (coordinates[3] >= canvas.coords(right_paddle)[1] and coordinates[1] <= canvas.coords(right_paddle)[3]):
            xVelocity = -abs(xVelocity)

        canvas.move(ball,xVelocity,yVelocity)
        window.update()
        time.sleep(.01)


def up(event): # w
    global left_up
    x = 0

    canvas.move(left_paddle, x, left_up)

left_up= -30

def down(event):  # s
    global left_down
    x = 0

    canvas.move(left_paddle, x, left_down)

left_down = 30

def up_2(event):  # up
    global right_y_up
    x = 0

    canvas.move(right_paddle, x, right_up)

right_up= -30
def down_2(event):  # down
    global right_y_down2
    x = 0

    canvas.move(right_paddle, x, right_down)


right_down= 30

def reset_button():
    global  xVelocity,yVelocity,right_up,right_down,left_down,left_up
    player_1.set('0')
    player_2.set('0')

    xVelocity= 3   #ball
    yVelocity= 2

    right_up = -30   #paddles
    right_down = 30

    left_up = -30
    left_down = 30

    left_side_title.config(text=player_1_title)
    right_side_title.config(text=player_2_title)
    canvas.itemconfig(ball,fill='black')

    canvas.itemconfig(left_paddle,fill= 'black')
    canvas.itemconfig(right_paddle, fill='black')



    time.sleep(1)
    canvas.coords(ball,180, 130, 200, 150)

    window.update()


def quit_b():
    window.destroy()
#-----------------------------
#menu settings

def ball_speed_x():
    global xVelocity

    new_x_speed= simpledialog.askinteger('X Speed','Enter X Axis Speed')

    if new_x_speed is not None:
        xVelocity=new_x_speed

def ball_speed_y():
    global yVelocity

    new_x_speed= simpledialog.askinteger('Y Speed','Enter Y Axis Speed')

    if new_x_speed is not None:
        yVelocity=new_x_speed

def left_paddle_speed():
    global left_up,left_down

    new_paddles_speed= simpledialog.askinteger('Left Paddle Speed','Enter Left Paddle Speed')

    if new_paddles_speed is not None:
        left_down= new_paddles_speed
        left_up= - new_paddles_speed



def right_paddle_speed():
    global right_down,right_up

    new_paddles_speed2 = simpledialog.askinteger('Right Paddle Speed', 'Enter Right Paddle Speed')

    if new_paddles_speed2 is not None:
        right_down = new_paddles_speed2
        right_up = - new_paddles_speed2


def left_paddle_color():
    new_color= simpledialog.askstring('Color', 'Enter Color')

    if new_color is not None:
        canvas.itemconfig(left_paddle,fill= new_color)

def right_paddle_color():
    new_color = simpledialog.askstring('Color', 'Enter Color')

    if new_color is not None:
        canvas.itemconfig(right_paddle, fill=new_color)

def ball_color():
    new_color = simpledialog.askstring('Color', 'Enter Color')

    if new_color is not None:
        canvas.itemconfig(ball, fill=new_color)

def left_menu_name():
    new_name = simpledialog.askstring('Name', 'Enter New Name')

    if new_name is not None:
        left_side_title.config(text=new_name)

    if new_name == (''):
        left_side_title.config(text='Player 1')


def right_menu_name():
    new_name = simpledialog.askstring('Name', 'Enter New Name')

    if new_name is not None:
        right_side_title.config(text=new_name)

    if new_name == (''):
        right_side_title.config(text='Player 2')

xVelocity= 3
yVelocity= 2

#--------------------------------
#window

window= Tk()
window.title("PyPong")
window.geometry('780x460')
window.config(bg= 'light green')

#---------------------------
window_menu= Menu(window)   #menu
window.config(menu=window_menu)
#---------------------------------
#ball
ball_setting_menu= Menu(window_menu,tearoff=0)
window_menu.add_cascade(label='Ball Game Settings',menu=ball_setting_menu)

ball_setting_menu.add_command(label='Ball Color',command=ball_color)
ball_setting_menu.add_command(label='Ball X Speed',command=ball_speed_x)
ball_setting_menu.add_command(label='Ball Y Speed',command=ball_speed_y)
#---------------------------------------------
# paddles
paddle_setting_menu= Menu(window_menu,tearoff=0)

window_menu.add_cascade(label='Paddle Settings',menu=paddle_setting_menu)

paddle_setting_menu.add_command(label='Left Paddle Speed',command=left_paddle_speed)
paddle_setting_menu.add_command(label='Right Paddle Speed',command=right_paddle_speed)

paddle_setting_menu.add_command(label='Left Paddle Color',command=left_paddle_color)
paddle_setting_menu.add_command(label='Right Paddle Color',command=right_paddle_color)
#--------------------------------------------------
#name change

gamer_tag_menu= Menu(window_menu,tearoff=0)

window_menu.add_cascade(label='Change Player Names',menu=gamer_tag_menu)

gamer_tag_menu.add_command(label='Left Player Name',command=left_menu_name)
gamer_tag_menu.add_command(label='Right Player Name',command=right_menu_name)


#-------------------------------
#player 1 & 2

player_1 = StringVar()
player_1.set('0')

player_2 = StringVar()
player_2.set('0')
#---------------------------------------
# player 1 & 2 title



#------------------------
# players score sides  player1 = left score  and player 2 = right score
left_side_title = Label(window,text=player_1_title,font=('comic sans',10,'bold'),bg='light blue')
left_side_title.pack(side='left',anchor='nw')

right_side_title = Label(window,text=player_2_title,font=('comic sans',10,'bold'),bg='light blue')
right_side_title.pack(side= 'right',anchor='ne')

play_1_scoreside= Label(window,width=3,height=2, textvariable=player_1,font=('comic sans',20),bg='light green')
play_1_scoreside.pack(side='left',anchor= 'nw')

play_2_scoreside= Label(window,width=3,height=2, textvariable= player_2,font=('comic sans',20),bg='light green')
play_2_scoreside.pack(side='right',anchor= 'ne')


#-----------------------------------------
#canvas

canvas= Canvas(window, width=440, height=400,bg='light blue')
canvas.pack(side='bottom')

width= 440
height= 400
#---------------------------------
#split line

line= canvas.create_line(220,400,220,0)

#----------------------------
#paddles

left_paddle= canvas.create_rectangle(10,160,20,240,fill='black')

right_paddle= canvas.create_rectangle(420,160,430,240,fill='black')

#--------------------------
#binding keys

window.bind('<w>',up)
window.bind('<s>',down)
window.bind('<Up>',up_2)
window.bind('<Down>',down_2)

#-------------------------
#ball
ball= canvas.create_oval(180, 130, 200, 150,fill='black')

#xVelocity= 3
#yVelocity= 2

ball_size= 20

#-------------------------
# restart button

reset= Button(window,text='RESET GAME', font=('comic sans',10,'bold'),fg='dark blue',bg='light blue',padx=1,pady=1,command=reset_button)
reset.pack(side='top')

quit_button= Button(window,text='QUIT',font=('comic sans',10,'bold'),fg='red',bg='light blue',padx=1,pady=1,command= quit_b)
quit_button.pack(side='bottom')
#---------------------------------------


#---------------------------------------
#ball moving
ball_moving()
window.mainloop()