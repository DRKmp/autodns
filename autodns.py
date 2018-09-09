#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################
#                              #
#     Software: Auto DNS       #
#     Versão  : 1.1            #
#     Cod. by : ~DRK~          #
#                              #
################################

from time import sleep
from os import system
from func.autoip_title import apresentacao
from func.autoip_change import autochange
from sys import argv
from servers import DnsList 
import json

def novaLinha():
	print('')


dns_servers = DnsList('dnslist.json')

vf = False
while vf == False:
	system("clear")
	novaLinha()
	print('\033[1;32m'+'-=-'*30)
	apresentacao()

	with open('meta.json', 'r') as f:
		meta = json.load(f)
		print(f'\nVersão: {meta["version"]}')
		print(f'Autor: {meta["author"]["name"]} - '
			  + meta["author"]["mail"])
		for contrib in meta["contrib"]:
			print(f'Colaborador: {contrib["name"]} - '
				  + contrib["mail"])
		print('\033[1;32m'+'-=-'*30)

	novaLinha()
	print('--- '*9)
	print('Quais servidores dns quer usar?')
	print('--- '*9)

	servers = dns_servers.get_options()
	options = []

	for i, opt in enumerate(servers):
		print(f'{i + 1}: {opt}')
		options.append(str(i))

	print('\nSair: exit')

	choice = input('\033[1;31m'+'\nConsole >>>'+' \033[0m').strip()

	if not choice:
		print('Digite um comando!')
		sleep(2)
		continue

	if choice.lower() in ['0', 'back', 'exit', 'close', 'sair', 'fechar']:
		system("clear")
		break

	if choice in options:
		autochange.dnsserver(valor=choice)
	else:
		print('Opção inválida!')
		sleep(2)
		continue

system("clear")
print('\033[1;32m')
print('-=-'*20)
print('Ok! Irei encerrar. Um momento, por favor...')
novaLinha()
print('Obrigado por utilizar o Auto DNS! Até mais!')
print('-=-'*20)
novaLinha()
print("Saindo...")
print('\033[0m')
sleep(3)

