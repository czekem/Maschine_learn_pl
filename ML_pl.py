# most often used letters for to start a word in polish language 
# ( base on : https://sjp.pwn.pl/poradnia/haslo/frekwencja-liter-w-polskich-tekstach;7072.html)
# a, i, o, e, z, n , r




class MyClass:
    
    letters = ['a','i','e','o','n','r']
    def __init__(self, object: str):
        self.object = object
        self.new_list = []
        
    def check_and_append(self, letters):
        if self.object[0] in letters:
            self.new_list.append(self.object)
    
    def __str__(self) -> str:
        return ', '.join(self.new_list)
    
    def __repr__(self) -> str:
        return f"{self.object!r}"

            

lst = ['gas', 'oil', 'water', 'chem', 'ala', 'ela']
my_obje = []

for item in lst:
    obj = MyClass(item)
    obj.check_and_append(MyClass.letters)
    print(obj)
    my_obje.append(obj)
    
