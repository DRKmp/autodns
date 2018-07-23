#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################
#                              #
#     Software: Auto DNS       #
#     Versão  : 1.1            #
#     Cod. by : ~DRK~          #
#                              #
################################

import json
from time import sleep
from os import system
from sys import argv

from func.autoip_title import apresentacao
from func.autoip_change import autochange
from servers import DnsList 


# Character sequences
EMPTY_LINE = ''
SEPARATOR = '-=-' * 20

# Formatting
BEGIN_GREEN = '\033[1;32m'
BEGIN_WHITE = 
END_COLOR = '\033[0m'

# Prompt
PS1 = BEGIN_WHITE + '\nConsole >>>' + END_COLOR

# Messages
INVALID_OPTION = 'Opção inválida!'
NULL_OPTION = 'Digite um comando!'
EXIT_COMMAND_HELPER = '\nSair: exit'


def printm(*lst):
    '''Prints each argument as a separate line and returns None'''
    list(map(print, lst))


dns_servers = DnsList('dnslist.json')


def main():
    while True:
        system("clear")
        printm(BEGIN_GREEN, SEPARATOR)
        apresentacao()

        with open('meta.json', 'r') as f:
            meta = json.load(f)

            print(f'\nVersão: {meta["version"]}')
            print(f'Autor: {meta["author"]["name"]} - '
                + meta["author"]["mail"])
            for contrib in meta["contrib"]:
                print(f'Colaborador: {contrib["name"]} - '
                    + contrib["mail"])

            print(BEGIN_GREEN + SEPARATOR)

        printm(EMPTY_LINE, SEPARATOR)
        printm('Quais servidores DNS quer usar?', SEPARATOR)

        servers = dns_servers.get_options()
        options = []

        for i, opt in enumerate(servers):
            print(f'{i + 1}: {opt}')
            options.append(str(i))

        print(EXIT_COMMAND_HELPER)
        choice = input(PS1).strip()

        if choice.lower() in ['0', 'exit', 'close', 'sair', 'fechar']:
            break

        if choice in options:
            autochange.dnsserver(valor=choice)
            continue

        print(INVALID_OPTION if choice else NULL_OPTION)
        sleep(2)

    system("clear")
    printm(BEGIN_GREEN, SEPARATOR)
    printm('Ok! Irei encerrar. Um momento, por favor...', EMPTY_LINE)
    printm('Obrigado por utilizar o Auto DNS! Até mais!', SEPARATOR, EMPTY_LINE)
    printm('Saindo...', END_COLOR)
    sleep(3)


if __name__ = '__main__':
    main()
