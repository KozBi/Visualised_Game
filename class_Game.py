import pathlib
# from pathlib import Path
# from clas_Item import Tool
# from clas_Item import Substract
import tkinter as tk
from class_Player import Player
from class_Room import Room
from class_Room import Kitchen
from PIL import Image, ImageTk



HELP_txt=pathlib.Path(r"C:\Users\kozlo\OneDrive\Pulpit\Game-Coocking\HELP.txt")
with HELP_txt.open(mode="r", encoding="utf-8") as file:
    HELP=file.read()


storage= {"name" : "storage",
          "tool" : ["pan", "knife"]}

pantry= {"name" : "pantry",
          "item" : ["uncut vegetables" , "uncut vegetables", "raw meat" ,"raw meat"],
          "substract": ["burger bun" , "burger bun"]}

kitchen= {"name" : "kitchen",
          "item" : [],
          "substract": []}

str_start=("you're in the kitchen. You need to make 2 burgers. You need burger buns, meat and vegetables. You'll find them in the pantry." "\n" 
        "To make it, you need tools: a pan and a knife. Bring everything to the Kitchen and use knife and pan. That's all, 2 burgers will be created" "\n" 
        "Write /help to get info about commands.")

class Game:
    

    player=Player()
    window = tk.Tk()

    image_path = r'C:\\Users\\kozlo\\OneDrive\\Pulpit\\Game-Coockingwith GUI\\_img\\cocker.jpg'
    _image = Image.open(image_path)
    resized_image = _image.resize((200, 200))
    photo_image = ImageTk.PhotoImage(resized_image)
    
    lbl_player_widg=tk.Label(window,relief=tk.RAISED,borderwidth=4,width=10,height=5)
    player_img=tk.Label(lbl_player_widg,relief=tk.RAISED,borderwidth=4,image=photo_image)
    player_eq=tk.Label(lbl_player_widg,relief=tk.RAISED,borderwidth=4,width=30,height=15,text="Twoje przedmioty:",background="blue")

    for n in range(player.max_inventory):
        button = tk.Button(player_eq, relief=tk.RAISED, borderwidth=4, width=10, height=5)
        button.grid(row=n // 2, column=n % 2)

    lbl_buttons=tk.Label(window)
    lbl_items=tk.Label(window,text="")

    @classmethod
    def start(cls):

        Game._init_game()

        
        cls.window.title("Game")

        entry_text = tk.StringVar()
        entry_text.set("Player")
        lbl_start_text=tk.Label(cls.window,text="Wellcome in the Game""\n"" Enter your name")
        
        ent_name=tk.Entry(cls.lbl_buttons,textvariable=entry_text)
        
        btn_name=tk.Button(master=cls.lbl_buttons,
                           text="Submit name",
                           command= lambda:(Game.player.name_a_player(ent_name.get()),
                                            lbl_start_text.config(text=f"Hello {Game.player.name}, \n {str_start}"),
                                            ent_name.pack_forget(),
                                            btn_name.pack_forget(),
                                            Game._show_rooms(),                                           
                                            Game._btn_collor_room(),
                                            Game._show_items_in_room(),
                                            cls.lbl_player_widg.grid(row=1, padx=10,pady=5)                                                                               
                                            ))
                           

        cls.window.columnconfigure(0,minsize=500)
        #cls.window.rowconfigure(0,weight=200,minsize=200)
        cls.window.rowconfigure(2,minsize=200)
        lbl_start_text.grid(row=0,sticky="ew", padx=10,pady=10)
        cls.player_img.pack(side="left")
        cls.player_eq.pack(side="left")
        #cls.lbl_player_widg.grid(row=1, padx=10,pady=5)
        
        #ent_name.grid(row=1,padx=10)
        cls.lbl_buttons.grid(row=2, column=0, padx=10, columnspan=3)
        cls.lbl_items.grid(row=3, column=0, padx=10, columnspan=3)
        ent_name.pack(pady=5)
        btn_name.pack()
        #btn_name.grid(row=1,column=1,padx=10)

        cls.window.mainloop()
        
        # print(f"{cls.player.name} You're in the kitchen. You need to make 2 burgers. You need burger buns, meat and vegetables. You'll find them in the pantry." "\n" 
        #         "To make it, you need tools: a pan and a knife. Bring everything to the Kitchen and use knife and pan. That's all, 2 burgers will be created" "\n" 
        #         "Write /help to get info about commands.")
        
  

 
    
    def _describe_me(cls):
        if   cls.player.items ==[]:
            print(f"{cls.player.name}, you are in the {cls.current_room.name}, you dont have any tools")
        else:
            print(f"{cls.player.name}, you are in the {cls.current_room.name}, your tools are: ")
            for item in cls.player.items:
                print (f"{item}") 
            



    @classmethod
    def action(cls):
        command = input("Type your action or /help ").lower()
        match command:
            case "/help":
                print(HELP)
            case "/me":
                cls._describe_me(cls)
            case "/move":               
                cls.move(cls)
            case "/get":
                if len(cls.player.items) >3:
                    print ("Your inventory is already full")
                elif cls.current_room.items:                
                    cls.get((cls),input("Which item: ").lower())
                else: print("This room is empty")
            case "/drop":    
                if cls.player.items:           
                    cls.drop((cls),input("Which item: ").lower())
                else: print("You have nothing") 
            case "/use":
                if cls.current_room.name != "kitchen":    
                    print("You can use tools only in kitchen") 
                else:cls.use_tool((cls),input("Which item: ").lower())    
            case _:
                print("This commend is unknow, you can ask for /help")

    @classmethod
    def move(cls,target):
        #target = (input("Write '1' to move to kitchen \nWrite '2' to move to pantry \nWrite '3' to Move to storage \n "))
        match target:
            case 1:
                cls.current_room = cls.Kitchen 
            case 2:
                cls.current_room = cls.Pantry
            case 3:
                cls.current_room = cls.Storage 
            case _:
                print("Try again")      
                return True 


    
    def get(cls, item):
        found_item = None       
        for room_item in cls.current_room.items:
            if room_item.name == item:
                found_item = room_item
                break
        if found_item:
            cls.current_room.items.remove(found_item)
            cls.player.take_item(found_item)
            print (f"You have now {cls.player.items}.")
        else: print (f"You cannot find {item} here")


    def drop(cls, item):
        if item=="all":
            cls.current_room.items.extend(cls.player.items)
            cls.player.items=[]
            print(f"You've dropped all. You can find now here {cls.current_room.items}")
        else:
            for player_item in cls.player.items:   
                if player_item.name == item:           
                    cls.player.drop_item(player_item)
                    cls.current_room.items.append(player_item)
                    print(f"You've dropped {player_item}")
                    break
            else: print (f"You don't have {item} ")




    def use_tool(cls,tool):
        if cls.player.items:    
            for item in cls.player.items:
                    if item.name ==tool=="knife":
                        item.CutVegetables(cls.current_room)
                        return True
                    elif item.name ==tool =="pan":
                        item.cookMeat(cls.current_room)      
                        return True           
                    else: print(f"You cannot use {tool}")
        else: print(f"You cannot use{tool}")

    @classmethod
    def win_check(cls) -> bool:
    
        required_ingredients = [("burger bun", 2), ("burger meat", 2), ("vegetables", 2)]
        for ingredient, count in required_ingredients:
            # add to generator object 1 if item.name ==ingredient and then sum the generator value #using_generator not a list!
            ingredient_count = sum(1 for item in cls.Kitchen.items if item.name == ingredient) 
            if ingredient_count < count:
                return False
        return True
    @classmethod
    def _init_game(cls):
        cls.Kitchen = Kitchen(**kitchen)
        cls.Storage = Room(**storage)
        cls.Pantry = Room(**pantry)

        cls.current_room = cls.Kitchen   
    @classmethod
    def _show_rooms(cls):
        cls.Kitchen.btn_create(cls.lbl_buttons)
        cls.Pantry.btn_create(cls.lbl_buttons)
        cls.Storage.btn_create(cls.lbl_buttons)


        cls.Kitchen.btn.pack(side="left", padx=10)
        cls.Pantry.btn.pack(side="left", padx=10)
        cls.Storage.btn.pack(side="left", padx=10)

        cls.Kitchen.btn.config(command=lambda _case=1:(cls.move(_case),Game._btn_collor_room(),Game._show_items_in_room()  ))
        cls.Pantry.btn.config(command=lambda _case=2:(cls.move(_case),Game._btn_collor_room(),Game._show_items_in_room()  ))
        cls.Storage.btn.config(command=lambda _case=3:(cls.move(_case),Game._btn_collor_room(),Game._show_items_in_room()  ))

        



    @classmethod
    def _show_items_in_room(cls):
        for widget in cls.lbl_items.winfo_children():
            widget.pack_forget()

        #if cls.current_room.items.e
        if len(cls.current_room.items) ==0:
            cls.lbl_items.config(text="Brak itemów w EQ")
        else:
            cls.lbl_items.config(text="")
        #else:
        for _item in cls.current_room.items:
            _item.btn_create(cls.lbl_items)
            _item.btn.pack(side="left", padx=10)

    @classmethod
    def _btn_collor_room(cls):
        cls.Kitchen.btn.config(background="white")
        cls.Pantry.btn.config(background="white")
        cls.Storage.btn.config(background="white")
        cls.current_room.btn.config(background='#b7d5ac')

    @classmethod
    def _show_player_item(cls,_master):
        for n in range(cls.player.max_inventory+1):
            button=tk.Button(_master)
            button.pack()