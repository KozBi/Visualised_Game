
from clas_Item import Item

class Player:
   
    max_inventory =4 
    def __init__(self, name="Unknow") -> None:
        self.name = name
        self.items = [] 
    
    def name_a_player(self,txt:str):
        self.name =txt

    def take_item(self,item:Item):
        if len(self.items)<self.max_inventory:
            self.items.append(item)
        else: return print("Your inventory is already full")

    def drop_item(self,item:Item):
        try:
            self.items.remove(item)
        except: pass
   
    def _show_plaer_item(self,_master):
        for _item in self.items:
            _item.btn_create(_master)
            _item.pack()


