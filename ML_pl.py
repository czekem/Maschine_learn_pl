# most often used letters for to start a word in polish language 
# ( base on : https://sjp.pwn.pl/poradnia/haslo/frekwencja-liter-w-polskich-tekstach;7072.html)
# a, i, o, e, z, n , r

# most often verb 'end' in polish language:
# base on ( https://depot.ceon.pl/bitstream/handle/123456789/20067/Czasownik_polski.pdf?sequence=6&isAllowed=y )

import pandas

import click
from PyPDF2 import PdfReader
import inquirer
from dataclasses import dataclass


@dataclass # word in progress
class Words:
    MAIN_DICTIONARY = 'slownik_pl.pdf'
    STOPWORDS = ".,;:!?•tekstu…………się…także…1)2)L=<SW)Ob(!)3)y)-(niedok.)N7Strug.2.1.6)7)6.7\n"
    word = str
    file = str
    number_of_apperance = int
    


def writing_main_info():
    """
    Here is a main logick of the program.
    This base it's a polish dictionary with over 161903 unique words.
    It's dirst
    """
    STOPWORDS = '.,;:!?•tekstu…………się…także…1)2)L=<SW)Ob(!)3)y)-(niedok.)N7Strug.2.1.6)7)6.7'
    new_lst = []
    make_lower = []
    filename = 'slownik_pl.pdf'
    reader = PdfReader(filename)
    num_pages = len(reader.pages)
    full_text = ''

    for page in range(num_pages):
        full_text += reader.pages[page].extract_text()

    words = full_text.split()
    
    for word in words:
        if word not in STOPWORDS:
            new_lst.append(word)
    
    # new_unique_words = set(new_lst)
    # with open('short_dict.csv', 'w', encoding='utf-8') as output:
    #     output.write(str(new_unique_words))
    
    for word in new_lst:
        word = word.lower()
        make_lower.append(word)
    
    return make_lower


def checking_if_word_is_polish(whole_dictionary):
    """
    This function is checking if the choosen word is in the dictionary
    """
    word = input('write word: ')
    if word in whole_dictionary:
        print(word, 'is in the dictionary')
    else:
        print(word, 'is not in the dictionary')


def count_number_of_apperance(whole_dictionary):
    new_count = 0
    question = input('Please enter the word that you want to count in occurance: ')
    for word in whole_dictionary:
        if word == question:
            new_count += 1
    print(f'The number of occurance of the word {question} is {new_count}')


def checking_for_verb(whole_dictionary):
    """
    This function is checking if the choosen word is a verb
    in a polish language.
    """
    new_lst = []
    letters_2 = ['ło', 'ć', 'ał', 'ała', 'iesz', 'dzie',]  
    for item in whole_dictionary:
        for word in letters_2:
            if item.endswith(word):
                new_lst.append(item)
    print('The polish werb, without duplicates of the same word are:', set(new_lst))



def polish_words(whole_dictionary):
    lst = ['plates', 'krowa', 'ćwiek', 'karczek', 'kiwi', 'aqua', 'platter', 'bolt', 'gun']
    for word in lst:
        if word in whole_dictionary:
            print(word, 'is in the dictionary')
        else:
            print(word, 'is not in the dictionary')


def file_open():
    filename = inpurt("Please write the name of file and it's extension:" )
    STOPWORDS = '.,;:!?•tekstu…………się…także…1)2)L=<SW)Ob(!)3)y)-(niedok.)N7Strug.2.1.6)7)6.7'
    new_lst = []
    make_lower = []

    reader = PdfReader(filename)
    num_pages = len(reader.pages)
    full_text = ''

    for page in range(num_pages):
        full_text += reader.pages[page].extract_text()

    words = full_text.split()
    
    for word in words:
        if word not in STOPWORDS:
            new_lst.append(word)
    
    # new_unique_words = set(new_lst)
    # with open('short_dict.csv', 'w', encoding='utf-8') as output:
    #     output.write(str(new_unique_words))
    
    for word in new_lst:
        word = word.lower()
        make_lower.append(word)
    
    return make_lower



def list_creation(opening_file):
    lst = opening_file.split()
    return lst


def check_for_words_in_text(open_file, whole_dictionary):
    for word in open_file:
        if word in whole_dictionary:
            print(word, 'is polish word.')
        else:
            print(word, 'is not a polish word.')



@click.group()
def cli():
    pass

@cli.command()
# @click.option('--filename', prompt='filename')
def main():
    whole_dictionary = writing_main_info()
    # create_list = list_creation(opening_file)
    open_file = file_open()
    print(open_file)
    
    question = [inquirer.List('first_question', message="What do you want to do?", choices=['checking_for_verb', 
                                                                                            'check_for_polish_word', 
                                                                                            'count_number_of_words',
                                                                                            'print_all',
                                                                                            'checking_is_word_is_verb',
                                                                                            'checking_for_polish_word_in_text'])]
    answers = inquirer.prompt(question)
    
    if answers['first_question'] == 'checking_for_verb':
        checking_for_verb(whole_dictionary)
    elif answers['first_question'] == 'check_for_polish_word':
        polish_words(whole_dictionary)
    elif answers['first_question'] == 'count_number_of_words':
        count_number_of_apperance(whole_dictionary)
    elif answers['first_question'] == 'print_all':
        print(whole_dictionary)
    elif answers['first_question'] == 'checking_is_word_is_verb':
        print(checking_if_word_is_polish)
    elif answers['first_question'] == 'checking_for_polish_word_in_text':
        print(check_for_words_in_text(open_file, whole_dictionary))
    
if __name__ == '__main__':
    cli()
    
    



