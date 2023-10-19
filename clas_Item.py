import tkinter as tk

btn=None

class Item:
    def __init__(self, name=None) -> None:
        self.name = name
        self.bg_color = "white"
        
    def __repr__(self) -> str:
        return f"{self.name}"
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    def btn_create(self,_master):
        self.btn=tk.Button(master=_master,text=self.name, width=(len(self.name)+2), height=2,relief=tk.RAISED,borderwidth=4,bg=self.bg_color)
    

class Substract(Item):
    def __init__(self, name) -> None:
        super().__init__(name)  
        self.bg_color = "#5171d1" #blue

    def __eq__(self, other): # it is required for win_check method()
        if isinstance(other, Substract):
            return self.name == other.name
        return False

class Tool(Item):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.bg_color = "#edfa8e" #yellow

    def CutVegetables(self,room):
        found = False
        for vege in list(room.items):           #iteration for copy a list, room items is changed in code below so it would have been overwritten !!! 
            if vege.name == "uncut vegetables":
                room.items.remove(vege)
                room.items.append(Substract("vegetables"))
                found = True
                print(f"You've cut vegetables, they are ready to be used in a burger.")
        if not found:
            print("There is nothing to cut here")

    def cookMeat(self,room):
        found = False
        for meat in list(room.items):           #iteration for copy a list, room items is changed in code below so it would have been overwritten !!! 
            if meat.name == "raw meat":
                room.items.remove(meat)
                room.items.append(Substract("burger meat"))
                found = True
                print(f"You've cooked meat, it's ready to be used in a burger.")
        if not found:
                print("There is nothing to cook here")


    



