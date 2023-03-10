from email.mime import image
from tkinter import *
from tkinter import font
from tkinter import ttk




# Main APP:
root = Tk()

# Images used in the APP:
bg_P_S_R = PhotoImage(file="IMAGES/IMG_BACKGROUND/Paper_Scisors_Rock.png")
bg_GameInstruct = PhotoImage(file="IMAGES/IMG_BACKGROUND/HowToPlay.png")
bg_Sci = PhotoImage(file="IMAGES/IMG_BUTTONS/Scisors.png")
bg_Pap = PhotoImage(file="IMAGES/IMG_BUTTONS/Paper.png")
bg_Rock = PhotoImage(file="IMAGES/IMG_BUTTONS/Rock.png")
bg_Start = PhotoImage(file="IMAGES/IMG_BUTTONS/PLAY.png")
bg_back = PhotoImage(file="IMAGES/IMG_BUTTONS/BACK.png")
bg_PlyAgain = PhotoImage(file="IMAGES/IMG_BUTTONS/PLAYAGAIN.png")
bg_Instruction = PhotoImage(file="IMAGES/IMG_BUTTONS/INSTRUCTION.png")
bg_Results = PhotoImage(file="IMAGES/IMG_BUTTONS/RESULTS.png")

# APP window parameters:
root.title("Rock Paper Siscors                                                               Version 1.1")
root.geometry("700x500")
root.resizable(False, False)
root.iconbitmap("IMAGES/APP_ICON/ICON.ico")

# Define variables used inside functions to store players' choices & calculate results:
p1 = ""
p2 = ""
Result1 = 0
Result2 = 0

# Function controling buttons (START, BACK, INSTRUCTIONS, PLAY AGAIN):

def Control(vlue):
   global p1
   global p2
   global Result1
   global Result2

   # START button Click:
   if vlue == "start":
      label_Pl_choose.place(x=250, y=10)
      label_P1.place(x=230, y=40)
      label_P2.place(x=380, y=40)

      btn_Result.place(x=290, y=360)
      btn_Back.place(x=600, y=460)

      btn_Rock1.place(x=10, y=20)
      btn_Sci1.place(x=10, y=180)
      btn_Pap1.place(x=10, y=340)  

      btn_Sci2.place(x=588, y=20)
      btn_Pap2.place(x=588, y=180)
      btn_Rock2.place(x=588, y=340)

      btn_start.place_forget()
      btn_Instruct.place_forget()

   # BACK button Click:
   if vlue == "back":
      p1 = ""
      p2 = ""
      Result1 = 0
      Result2 = 0

      btn_Result.place_forget()
      lbl_Warn_choice.place_forget()

      btn_start.place(x=280, y=360)
      btn_Instruct.place(x=305, y=440)
      btn_Back.place_forget()
      label_Pl_choose.place_forget()
      label_P1.place_forget()
      label_P2.place_forget()

      label_main_ttle.configure(image= bg_P_S_R)

      btn_Rock1.place_forget()
      btn_Sci1.place_forget()
      btn_Pap1.place_forget()

      btn_Sci2.place_forget()
      btn_Pap2.place_forget()
      btn_Rock2.place_forget()

   # INSTRUCTIONS button Click:
   if vlue == "instruction":
      btn_Result.place_forget()
      btn_start.place_forget()
      btn_Instruct.place_forget()

      btn_Rock1.place_forget()
      btn_Sci1.place_forget()
      btn_Pap1.place_forget()  

      btn_Sci2.place_forget()
      btn_Pap2.place_forget()
      btn_Rock2.place_forget()

      btn_Back.place(x=600, y=460)
      label_main_ttle.configure(image= bg_GameInstruct)

   # PLAY AGAIN button Click:
   if vlue == "P_again":
      # Empty players' choices:
      p1 = ""
      p2 = ""

      frame_Rslt.place_forget()
      frame_main.place(x=0, y= 0)

      lbl_PL1.place_forget()
      lbl_Choice1.place_forget()
      lbl_rs_P1.place_forget()

      lbl_PL2.place_forget()
      lbl_Choice2.place_forget()
      lbl_rs_P2.place_forget()

      lbl_win.place_forget()
      lbl_win_pic.place_forget()
      btn_PlyAgain.place_forget()


# Player 1 choice:
def Pl1_choice(V):
   global p1
   p1 = V

# Player 2 choice:
def Pl2_choice(V):
   global p2
   p2 = V

# Players result:
def Result():
   # Define global variables:
   global p1
   global p2
   global Result1
   global Result2
   p_1 = p1
   p_2 = p2

   # Define The winner after Players' choices:

      # If one or both Players don't make a choice:
   if p_1 == "" and p_2 == "":
      # Display warning msg for both players:
      label_Pl_choose.place(x=250, y=10)
      label_P1.place(x=230, y=40)
      label_P2.place(x=380, y=40)
      lbl_Warn_choice.configure(bg= "Yellow", text=" Both Players \ndid not choose")
      lbl_Warn_choice.place(x=270, y=70)

      # If Player 1 doesn't make a choice:  
   elif p_1 == "":
      # Display warning msg for player 1:
      label_Pl_choose.place(x=250, y=10)
      label_P1.place(x=230, y=40)
      label_P2.place(x=380, y=40)
      lbl_Warn_choice.configure(bg="Green", text="    Player 1 \ndid not choose")
      lbl_Warn_choice.place(x=270, y=70)

      # If Player 2 doesn't make a choice:  
   elif p_2 == "":
      # Display warning msg for player 2:
      label_Pl_choose.place(x=250, y=10)
      label_P1.place(x=230, y=40)
      label_P2.place(x=380, y=40)
      lbl_Warn_choice.configure(bg="Red", text="    Player 2 \ndid not choose")
      lbl_Warn_choice.place(x=270, y=70)

      # After both Players make their choices:
   else:
         # Hide Main frame & show Result frame:
      frame_main.place_forget()
      frame_Rslt.place(x=0,y=0)
         # Hide Label choice warning which it shows when one or both Players do not choose:
      lbl_Warn_choice.place_forget()

      # Show all labels and results on Result frame:

         # Player 1:
      lbl_PL1.place(x=15,y=3)
      lbl_Choice1.place(x=120,y=70)
      lbl_rs_P1.place(x=45, y=25)

         # Player 2:
      lbl_PL2.place(x=385,y=3)
      lbl_Choice2.place(x=490,y=70)
      lbl_rs_P2.place(x=420, y=25)

         # Winner result labels:
      lbl_win.place(x=290,y=170)
      lbl_win_pic.place(x=170,y=220)
      btn_PlyAgain.place(x=310 ,y= 390)

      # If both players have same choice:
      if p_1 == p_2:

         if p_1 == 'PAPER' and p_2 == 'PAPER':
            lbl_Choice1.configure(image= bg_Pap)
            lbl_Choice2.configure(image= bg_Pap)
            lbl_win_pic.configure(bg="Yellow", text = "DRAW")
            lbl_rs_P1.configure(text= str(Result1))
            lbl_rs_P2.configure(text= str(Result2))

         elif p_1 == 'SCISOR' and p_2 == 'SCISOR':
            lbl_Choice1.configure(image= bg_Sci)
            lbl_Choice2.configure(image= bg_Sci)
            lbl_win_pic.configure(bg="Yellow", text = "DRAW")
            lbl_rs_P1.configure(text= str(Result1))
            lbl_rs_P2.configure(text= str(Result2))

         elif p_1 == 'ROCK' and p_2 == 'ROCK':
            lbl_Choice1.configure(image= bg_Rock)
            lbl_Choice2.configure(image= bg_Rock)
            lbl_win_pic.configure(bg="Yellow", text = "DRAW")
            lbl_rs_P1.configure(text= str(Result1))
            lbl_rs_P2.configure(text= str(Result2))

      # If players have different choices:

      elif p_1 == 'PAPER' and p_2 == 'ROCK':
         Result1 += 1
         lbl_win_pic.configure(bg="Green", text = "PLAYER 1")
         lbl_Choice1.configure(image= bg_Pap)
         lbl_Choice2.configure(image= bg_Rock)
         lbl_rs_P1.configure(text= str(Result1))
         lbl_rs_P2.configure(text= str(Result2))

      elif p_1 == 'PAPER' and p_2 == 'SCISOR':
         Result2 += 1
         lbl_win_pic.configure(bg="Red", text = "PLAYER 2")
         lbl_Choice1.configure(image= bg_Pap)
         lbl_Choice2.configure(image= bg_Sci)
         lbl_rs_P1.configure(text= str(Result1))
         lbl_rs_P2.configure(text= str(Result2))
         
      elif p_1 == 'ROCK' and p_2 == 'PAPER':
         Result2 += 1
         lbl_win_pic.configure(bg="Red", text = "PLAYER 2")
         lbl_Choice1.configure(image= bg_Rock)
         lbl_Choice2.configure(image= bg_Pap)
         lbl_rs_P1.configure(text= str(Result1))
         lbl_rs_P2.configure(text= str(Result2))

      elif p_1 == 'ROCK' and p_2 == 'SCISOR':
         Result1 += 1
         lbl_win_pic.configure(bg="Green", text = "PLAYER 1")
         lbl_Choice1.configure(image= bg_Rock)
         lbl_Choice2.configure(image= bg_Sci)
         lbl_rs_P1.configure(text= str(Result1))
         lbl_rs_P2.configure(text= str(Result2))

      elif p_1 == 'SCISOR' and p_2 == 'PAPER':
         Result1 += 1
         lbl_win_pic.configure(bg="Green", text = "PLAYER 1")
         lbl_Choice1.configure(image= bg_Sci)
         lbl_Choice2.configure(image= bg_Pap)
         lbl_rs_P1.configure(text= str(Result1))
         lbl_rs_P2.configure(text= str(Result2))

      elif p_1 == 'SCISOR' and p_2 == 'ROCK':
         Result2 += 1
         lbl_win_pic.configure(bg="Red", text = "PLAYER 2")
         lbl_Choice1.configure(image= bg_Sci)
         lbl_Choice2.configure(image= bg_Rock)
         lbl_rs_P1.configure(text= str(Result1))
         lbl_rs_P2.configure(text= str(Result2))



      # FRAMES & LABELS:
 
# Frames & labels for MAIN:
frame_main = Frame(root, width=700, height=500)
frame_main.place(x=0, y=0)
label_main_ttle = Label(frame_main, image= bg_P_S_R, bg= "White")
label_main_ttle.place(x=0, y=0)
lbl_Warn_choice = Label(frame_main, fg="black", bg= "Yellow", font= "Arial 15 bold")

# Label "Choose your Player" text:
label_Pl_choose = Label(label_main_ttle, text= "Make your choice", font="Arial 15 bold", bg= "White", fg= "Black" )
# Player 1 label:
label_P1 = Label(label_main_ttle, text= "PLAYER 1", font="Arial 10 bold", bg= "White", fg= "Green" )
# Player 2 label:
label_P2 = Label(label_main_ttle, text= "PLAYER 2", font="Arial 10 bold", bg= "White", fg= "Red" )

# Player1 Buttons:
btn_Pap1 = Button(frame_main, image=bg_Pap, bg= "Green", command= lambda: Pl1_choice("PAPER"))
btn_Sci1 = Button(frame_main, image=bg_Sci, bg= "Green", command= lambda: Pl1_choice("SCISOR"))
btn_Rock1 = Button(frame_main, image=bg_Rock, bg= "Green", command= lambda: Pl1_choice("ROCK"))

# Player2 Buttons:
btn_Pap2 = Button(frame_main, image=bg_Pap, bg= "Red", command= lambda: Pl2_choice("PAPER"))
btn_Sci2 = Button(frame_main, image=bg_Sci, bg= "Red", command= lambda: Pl2_choice("SCISOR"))
btn_Rock2 = Button(frame_main, image=bg_Rock, bg= "Red", command= lambda: Pl2_choice("ROCK"))


#Frame Result:
frame_Rslt = Frame(root, width=700, height=500)
label_fr_rslt = Label(frame_Rslt).place(x=0, y=0)

# Players Result labels:
lbl_rs_P1 = Label(label_fr_rslt, fg="Black", font="Arial 20 bold", width=14, height=1)
lbl_rs_P2 = Label(label_fr_rslt, fg="Black", font="Arial 20 bold", width=14, height=1)

# Player1 Label and choice:
lbl_PL1 = Label(label_fr_rslt, fg="Green", text= "PLAYER 1", font="Arial 15 bold", width=25, height=1)
lbl_Choice1 = Label(label_fr_rslt, bg= "Green")

# Player2 Label and choice:
lbl_PL2 = Label(label_fr_rslt, fg="Red", text= "PLAYER 2", font="Arial 15 bold", width=25, height=1)
lbl_Choice2 = Label(label_fr_rslt, bg= "Red")

# Winner Label:
lbl_win = Label(label_fr_rslt, fg="Black",text= "THE WINNER IS", font="Arial 15 bold", width=12, height=2)
lbl_win_pic = Label(label_fr_rslt, font="Arial 45 bold", width=10, height=2)

# Play again Button:
btn_PlyAgain = Button(label_fr_rslt, image=bg_PlyAgain, borderwidth=0, command= lambda: Control("P_again"))


# CONTROL buttons:

   # START button:
btn_start = Button(frame_main, image= bg_Start, borderwidth=0, command= lambda: Control("start"))
btn_start.place(x=280, y=360)

   # Back button:
btn_Back = Button(frame_main, image=bg_back, borderwidth=0, command= lambda: Control("back"))


   # RESULT button:
btn_Result = Button(frame_main, image= bg_Results, borderwidth=0, command= Result)

   # INSTRUCTION button:
btn_Instruct = Button(frame_main, image= bg_Instruction, borderwidth=0,  command= lambda: Control("instruction"))
btn_Instruct.place(x=305, y=440)



root.mainloop()