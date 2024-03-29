##################################################################################################

###########
###########
###########
###########
###########
###########                   ########            ##########################                     ######
###########                   ########            ###########################                   ########
###########                   ########            ############################                 ##########
###########                   ########            #######           ###########               ############
###########                   ########            #######           ###########              #####    #####
###########                                       #######           ###########             #####      #####
###########                   ########            #######           ###########            #######    #######
###########                   ########            #######           ###########           ####################
###########                                       #######           ###########          ######################
###########                   ########            #######           ###########         ########################
###########                   ########            #######           ###########        ########          ########
###########                   ########            #######           ###########       ########            ########
###########                   ########            #######           ###########      ########              ########
###########                   ########            #######           ###########     ########                #######
#####################         ########            #######           ###########    ########                  ######
#############################  ########           #######           ###########   ########                    #####
############################### ########          #######           ###########  ########                      ####
##############################   ################ #######           ###########    #####                        ###
#############################     ###############    ####           ############ ######                          ##
#############################       ################ ####            ########### ##########                 #######


##################################################################################################


# Greetings.

#     Copyright (c) FRTNX [Busani P. Ndlovu]

# All rights reserved under the 3-clause BSD License:

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import random
import time
from colorama import Fore

ban = ["                     ########################################################################",
       "                     ########################################################################",
       "                     ####### LLLL ####### UUU ### UUU ## NN NNNNNN ######### AAAA ###########",
       "                     ####### LLLL ####### UUU ### UUU ## NNNNNNNNNNN ###### AAAAAAA ######### ",
       "                     ####### LLLL ####### UUU ### UUU ## NNN ### NNNN #### AAA # AAA ########",
       "                     ####### LLLL ####### UUU ### UUU ## NNN ##### NNN ## AAAAAAAAAAA #######",
       "                     ####### LLLL ####### UUU ### UUU ## NNN ##### NNN ## AAAAAAAAAAA #######",
       "                     ####### LLLL ####### UUU ### UUU ## NNN ##### NNN ## AAA ### AAA #######",
       "                     ####### LLLLLLLLL ### UUUUUUUUUU ## NNN ##### NNN ## AAA ### AAA #######",
       "                     ####### LLLLLLLLL ##### UUUUUUUU ## NNN ##### NNN ## AAA ### AAA #######",
       "                     ########################################################################",
       "                     ###############################################################"]

x = ['#########']

char_set = ['1','2','3','4','5','6','7','8','9','#','@','F','R','T','N','X']

random_char = ['\u2648', 
               '\u2649', 
               '\u2650', 
               '\u2652', 
               '\u2651', 
               '\u2653', 
               '\u264c', 
               '\u264d', 
               '\u264a', 
               '\u264f',
               '\u264e',
               '\u26ce'
              ]

char_set.append(random.choice(random_char))

banner_line = 1

x_column = 1

print('\n\n')
for line in ban:
    for letter in line:
        if letter == '#':
            print(Fore.LIGHTBLACK_EX+random.choice(char_set), end='')
            time.sleep(0.0001)
            sys.stdout.flush()
        elif letter == ' ':
            print(letter, end='')
            sys.stdout.flush()
        else:
            print(Fore.GREEN+random.choice(char_set), end='')
            time.sleep(0.0001)
            sys.stdout.flush()
    banner_line += 1
    if banner_line == 13:
        for line in x:
            for char in line:
                if x_column == 9:
                    # time.sleep(1)
                    print(Fore.GREEN+random.choice(char_set))
                    # time.sleep(1)
                else:
                    print(Fore.LIGHTBLACK_EX+random.choice(char_set), end='')
                    time.sleep(0.05)
                    sys.stdout.flush()
                    x_column += 1
            print()
    else:
        print()

print(Fore.RESET+'\n\n')