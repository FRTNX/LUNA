import os
import sys
import json
import time
import random
import datetime
import requests
from colorama import Fore
from func_timeout.StoppableThread import StoppableThread
from prompt_toolkit.shortcuts import prompt


def sprint(text, delay=0.002):
    text.replace('_', ' ')
    for letter in text:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(delay)
    print('\r')


def get_state_bullet():
    try:
        requests.get('https://google.com')
        return Fore.GREEN + u"\u25CF " + Fore.RESET
    except:
        return Fore.LIGHTBLACK_EX + u"\u25CF " + Fore.RESET


def output_prompt(prompt=None):
    if prompt:
        print(prompt, end='')
        return

    standard_output_prompt = '\n[' + Fore.LIGHTBLACK_EX + 'LUNA' + Fore.RESET + '] '
    print(standard_output_prompt, end='')
    time.sleep(0.2)
    return

def input_prompt(username):
    return '\n[' + Fore.LIGHTBLACK_EX + username + Fore.RESET + '] '

beam = "-------------------------------------------------------------------------------"

def list_table(list_str):
    os.system('python3 ./client/resources/banners/db_banner3.py')

    temp, temp2 = prepare_listing(list_str)
    temp.sort(); temp2.sort()

    file_count = len(temp)+len(temp2)

    a_space = 40
    b_space = 40

    # Extra bit of code ensures neat presentation, overengineered, I admit.
    a_sequence = []
    b_sequence = []
    a = 0
    b = 1
    while (a < len(temp) and b < len(temp)):
        a_sequence.append(temp[a])
        b_sequence.append(temp[b])
        a += 3
        b += 3

    tri_release = []

    if len(temp) > 3:
        for i in temp:
            tri_release.append(i)
            if len(tri_release) == 3:
                aSpace = a_space-len(tri_release[0])+2
                bSpace = b_space-len(tri_release[1])+2
                print("%s%s%s%s%s" % (tri_release[0], ' '* aSpace,
                                        tri_release[1], ' '* bSpace,
                                        tri_release[2]))
                tri_release.clear()
                time.sleep(0.01)
    else:
        if len(temp) == 2:
            aSpace = a_space-len(tri_release[0])+2
            print("%s%s%s" % (tri_release[0], ' '* aSpace,
                                tri_release[1]))
        else:
            print(tri_release[0])

    if temp2 != []:
        print(beam)
        for title in temp2:
            print(title)
            time.sleep(0.01)
    print(beam + '%s distinct files' % str(file_count))


def prepare_listing(list_str):
    temp = []
    temp2 = []

    for string in list_str:
        if len(string) < 40:
            temp.append(string.strip().replace('\n', ''))
        else:
            temp2.append(string.strip().replace('\n', ''))

    return temp, temp2

def initialize():
    print(get_state_bullet() + str(datetime.datetime.now()))
    os.system('python3 ./client/resources/banners/banner1.py')
    time.sleep(1)

    response = requests.get('http://localhost:4001/router?cmd=fetch_quote').json()
    output_prompt()
    sprint(response['text'])

    user = prompt(
        '\n                                              Code Name: ').strip()
    time.sleep(1)
    output_prompt()
    sprint(f'Hello {user}')
    return user

if __name__ == '__main__':
    user = initialize()
    user_prompt = input_prompt(user)
    while True:
        print(user_prompt, end='')
        time.sleep(0.2)
        user_input = prompt()
        response = requests.get(f'http://localhost:4001/router?cmd={user_input}').json()
        output_prompt()
        if 'displayIcon' in response.keys():
            print(Fore.GREEN + response['displayIcon'] + Fore.RESET + '\n')
        if response['displayStyle'] == 'matrix':
            sprint(response['text'])
        elif response['displayStyle'] == 'list':
            list_table(response['text'])
        else:
            print(response['text'])

