import tkinter
import pygame


pygame.mixer.init()

clickkk=pygame.mixer.Sound("Sounds/click.mp3")
clickkk.set_volume(1.0)
restarttt=pygame.mixer.Sound("Sounds/click2.mp3")
restarttt.set_volume(1.0)
victory=pygame.mixer.Sound("Sounds/victory.mp3")
victory.set_volume(1.0)
drawww=pygame.mixer.Sound("Sounds/draw.mp3")
drawww.set_volume(1.0)
theme=pygame.mixer.Sound("Sounds/theme.mp3")
theme.set_volume(0.5)
theme.play(-1)

# Main Window

mw = tkinter.Tk()
mw.geometry("500x680")
mw.title("TIC TAC TOE")
mw.configure(bg="#151A2D")
mw.resizable(False, False)


def restart():
    global turn,game_over

    restarttt.play()

    turn = "X"
    game_over=False
    nlabel.configure(text="")

    for i in buttons:
        i.configure(text="",
                    bg="#292F43",
                    fg="#FFFFFF",
                    highlightthickness=0,
                    highlightbackground="#292F43",
                    highlightcolor="#292F43"
                    )

    plabel.configure(text="X",
                     fg="#35C8FF"
                     )

mw.grid_rowconfigure(0, weight=1)


# Title Frame
tframe = tkinter.Frame(
    mw,
    bg="#151A2D",
    width=500,
    height=60
)
tframe.grid(
    column=0,
    row=0,
    sticky="ew"
)
tlabel=tkinter.Label(tframe,
                     text=" Tic Tac Toe",
                     bg="#151A2D",
                     fg="#35C8FF",
                     font=("Arial",20,"bold")
                     )
tlabel.pack()

# Score Card
sframe = tkinter.Frame(
    mw,
    bg="#151A2D",
    width=500,
    height=80
)
sframe.grid(
    column=0,
    row=1,
    sticky="ew"
)

xwin=0
owin=0
draw=0

# Win and Draw Frame
xwframe = tkinter.Frame(
    sframe,
    bg="#292F43",
    width=145,
    height=70
)

xwframe.grid(
    column=0,
    row=0,
    sticky="nsew",
    padx=10,
    pady=10
)

xwlabel=tkinter.Label(xwframe,
                      text=" X Wins:",
                      font=("Arial",15,"bold"),
                      fg="#35C8FF",
                      bg="#292F43"
                      )
xwlabel.pack(pady=15)

count1=tkinter.Label(xwframe,
                     text=xwin,
                     font=("Arial",15,"bold"),
                     fg="#FFFFFF",
                     bg="#292F43"
                     )
count1.pack()

xwframe.pack_propagate(False)

owframe = tkinter.Frame(
    sframe,
    bg="#292F43",
    width=145,
    height=70
)
owframe.grid(
    column=1,
    row=0,
    pady=10,
    padx=10,
    sticky="ew"
)

owlabel=tkinter.Label(owframe,
                      text=" O Wins:",
                      font=("Arial",15,"bold"),
                      fg="#55E6A5",
                      bg="#292F43"
                      )
owlabel.pack(pady=15)

count2=tkinter.Label(owframe,
                     text=owin,
                     font=("Arial",15,"bold"),
                     fg="#FFFFFF",
                     bg="#292F43"
                     )
count2.pack()

owframe.pack_propagate(False)

dframe = tkinter.Frame(
    sframe,
    bg="#292F43",
    width=145,
    height=70
)
dframe.grid(
    column=2,
    row=0,
    padx=10,
    pady=10,
    sticky="ew"
)

dlabel=tkinter.Label(dframe,
                      text="Draws:",
                      font=("Arial",15,"bold"),
                      fg="#FFD166",
                      bg="#292F43"
                      )
dlabel.pack(pady=15)

count3=tkinter.Label(dframe,
                     text=draw,
                     font=("Arial",15,"bold"),
                     fg="#FFFFFF",
                     bg="#292F43"
                     )
count3.pack()

dframe.pack_propagate(False)

for col in range(3):
    sframe.grid_columnconfigure(col, weight=1)


# Player Turn

pframe = tkinter.Frame(
    mw,
    bg="#292F43",
    width=490,
    height=15
)
pframe.grid(
    column=0,
    row=2,
    padx=10,
    pady=10,
    sticky="ew"
)

player_label = tkinter.Label(
    pframe,
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#292F43",
    text="Player "
)
player_label.pack(side="left", padx=(160, 0))

plabel = tkinter.Label(
    pframe,
    font=("Arial", 20, "bold"),
    fg="#35C8FF",
    bg="#292F43",
    text="X"
)
plabel.pack(side="left")

turn_text = tkinter.Label(
    pframe,
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#292F43",
    text="'s Turn"
)
turn_text.pack(side="left")

# Notifiction Frame

nframe=tkinter.Frame(mw,
                     bg="#151A2D",
                     width=500,
                     height=45
                     )

nframe.grid(row=3,
            column=0,
            )

nlabel=tkinter.Label(nframe,
                     text="",
                     bg="#151A2D",
                     font=("Arial",20,"bold")
                     )
nlabel.pack()

nframe.pack_propagate(False)



# Game Area
gframe = tkinter.Frame(
    mw,
    bg="#151A2D",
    width=500,
    height=390
)
gframe.grid(
    column=0,
    row=4,
    sticky="nsew"
)


# Buttons Frame
buttonframe = tkinter.Frame(
    gframe,
    width=300,
    height=390,
    bg="#292F43"
)

buttonframe.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)

buttonframe.pack_propagate(False)


# Functions
buttons = []

def check_winner():
    global game_over,xwin,owin,draw

    for a, b, c in wins:
        if (
            a["text"] == "X"
            and b["text"] == "X"
            and c["text"] == "X"):
            game_over=True
            xwin=xwin+1
            drawww.play()
            nlabel.configure(text="━━ X WINS! ━━",
                             fg="#35C8FF"
                             )
            a.configure(highlightthickness=2,
                        highlightbackground="#35C8FF",
                        highlightcolor="#292F43"
                        )
            b.configure(highlightthickness=2,
                        highlightbackground="#35C8FF",
                        highlightcolor="#292F43"
                                                 )
            c.configure(highlightthickness=2,
                        highlightbackground="#35C8FF",
                        highlightcolor="#292F43"
                                    )
            

        elif (
            a["text"] == "O"
            and b["text"] == "O"
            and c["text"] == "O"):
            game_over=True
            owin=owin+1
            drawww.play()
            count2.configure(text=owin)
            nlabel.configure(text="━━ O WINS! ━━",
                             fg="#55E6A5"
                             )
            a.configure(highlightthickness=2,
                        highlightbackground="#D4AF37",
                        highlightcolor="#292F43"
                        )
            b.configure(highlightthickness=2,
                        highlightbackground="#D4AF37",
                        highlightcolor="#292F43"
                                                 )
            c.configure(highlightthickness=2,
                        highlightbackground="#D4AF37",
                        highlightcolor="#292F43"
                                    )
            
    if not game_over and all(button["text"]!="" for button in buttons) :
        draw=draw+1
        victory.play()
        count3.configure(text=draw)
        nlabel.configure(text="━━ IT'S A DRAW! ━━",
                         fg="#FFD166"
                         )
        game_over=True




game_over=False
turn="X"
def click(button):
    global turn

    if game_over:
        return 

    clickkk.play()


    if button["text"] == "":
        if turn == "X":
            button.configure(
                text="X",
                fg="#35C8FF"
            )
            turn = "O"
            plabel.configure(text="O",
                             fg="#55E6A5"
                             )

        else:
            button.configure(
                text="O",
                fg="#55E6A5"
            )
            turn = "X"
            plabel.configure(text="X",
                             fg="#35C8FF"
                             )

        check_winner()


# Buttons Creation
for row in range(3):
    for col in range(3):
        button = tkinter.Button(
            buttonframe,
            bg="#292F43",
            width=8,
            height=4,
            font=("Impact", 20)
        )

        button.grid_propagate(False)

        button.configure(
            command=lambda b=button: click(b)
        )

        button.grid(
            column=col,
            row=row,
            padx=2,
            pady=2,
            sticky="nsew"
        )

        buttons.append(button)


# Winning Combinations


wins = [
    (buttons[0], buttons[1], buttons[2]),
    (buttons[3], buttons[4], buttons[5]),
    (buttons[6], buttons[7], buttons[8]),

    (buttons[0], buttons[3], buttons[6]),
    (buttons[1], buttons[4], buttons[7]),
    (buttons[2], buttons[5], buttons[8]),

    (buttons[0], buttons[4], buttons[8]),
    (buttons[2], buttons[4], buttons[6])
]


# Restart Frame
rframe = tkinter.Frame(
    mw,
    bg="#151A2D",
    width=500,
    height=60
)
rframe.grid(
    column=0,
    row=5,
    sticky="ew"
)


# Restart Button
restart_button = tkinter.Button(
    rframe,
    text=" ⟳ Restart",
    bg="#35C8FF",
    anchor="center",
    command=restart
)

restart_button.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    width=250,
    height=40
)


mw.mainloop()