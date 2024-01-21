# most often used letters for to start a word in polish language 
# ( base on : https://sjp.pwn.pl/poradnia/haslo/frekwencja-liter-w-polskich-tekstach;7072.html)
# a, i, o, e, z, n , r

# most often verb 'end' in polish language:
# base on ( https://depot.ceon.pl/bitstream/handle/123456789/20067/Czasownik_polski.pdf?sequence=6&isAllowed=y )


class MyClass:
    
    letters = ['a','i','e','o','n','r']
    letters_2 = ['ło', 'ć', 'ał', 'ała', 'iesz', 'dzie',]  
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

    def check_if_verb2(self, letters_2):
        if self.object[-1] in letters_2:
            self.new_list.append(self.object)   

lst = ['gas', 'oil', 'water', 'chem', 'ala', 'ela']


# my_obje = []

# for item in lst:
#     obj = MyClass(item)
#     obj.check_and_append(MyClass.letters)
#     print(obj)
#     my_obje.append(obj)
    
    
  
    
lst_2 = ['spała', 'biegał', 'latało', 'kichało', 'wylało', 'krowa', 'las', 'piękny',]


def checking_for_verb(lst):
    """
    This function is checking if the choosen word is a verb
    in a polish language.
    """
    letters_2 = ['ło', 'ć', 'ał', 'ała', 'iesz', 'dzie',]  
    for item in lst:
        for word in letters_2:
            if item.endswith(word):
                print(item)
                

checking_for_verb(lst_2)


def check_for_polish_word(lst):
    """
    This function is checking if the choosen 
    word is a polish(stil needed to rework on this part)
    """
    letters = ['a','i','e','o','n','r']
    for item in lst:
        for word in letters:
            if item.startswith(word):
                print(item)
                
                
check_for_polish_word(lst) # need to work on it.
