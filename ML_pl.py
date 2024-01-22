# most often used letters for to start a word in polish language 
# ( base on : https://sjp.pwn.pl/poradnia/haslo/frekwencja-liter-w-polskich-tekstach;7072.html)
# a, i, o, e, z, n , r

# most often verb 'end' in polish language:
# base on ( https://depot.ceon.pl/bitstream/handle/123456789/20067/Czasownik_polski.pdf?sequence=6&isAllowed=y )

import pandas

import click


from pypdf import PdfReader
import inquirer


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

def file_opening():
    filename = input('Wrote name of file: ')
    reader = PdfReader(filename)
    page = reader.pages[0]
    page.extract_text()
    
    return page.extract_text()


def list_creation(opening_file):
    lst = opening_file.split()
    return lst


def stop_words_delete(create_list):
    STOPWORDS = '.,;:!?•tekstu…………się…także…'
    new_list = []
    for word in create_list:
        for letter in STOPWORDS:
            if word not in STOPWORDS:
                new_list.append(word)
    return new_list


def checking_for_verb(lst):
    """
    This function is checking if the choosen word is a verb
    in a polish language.
    """
    new_lst = []
    letters_2 = ['ło', 'ć', 'ał', 'ała', 'iesz', 'dzie',]  
    for item in lst:
        for word in letters_2:
            if item.endswith(word):
                new_lst.append(item)
    print('The polish werb, without duplicates of the same word are:', set(new_lst))
                


def check_for_polish_word(lst):
    """
    This function is checking if the choosen 
    word is a polish(stil needed to rework on this part)
    """
    new_lst = []
    letters = ['a','i','e','o','n','r']
    for item in lst:
        for word in letters:
            if item.startswith(word):
                new_lst.append(item)
    print('The polis words without any duplicates of the same word are:', set(new_lst))
                
                
@click.group()
def cli():
    pass

@cli.command()
# @click.option('--filename', prompt='filename')
def main():
    opening_file = file_opening()
    create_list = list_creation(opening_file)
    deleting_stopwords = stop_words_delete(create_list)
    

    
    
    
if __name__ == '__main__':
    cli()
