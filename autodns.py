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
import json

def novaLinha():
	print('')

version = 1.1
credit = 'Codado por ~DRKmp~    Skype: derick-mp    Mail: derickmotta@outlook.com\n\nContribuição do Gabriel Chiconi    gabrielchiconi.github.io\n\nSalve a todos os membros do #UniãoHacker, tmj!'

class DnsOption:
	def __init__(self, name, addr):
		self.name, self.addr = name, addr

	def __str__(self):
		return f'{self.name}: {", ".join(self.addr)}'

dns_options = []

with open('dnslist.json', 'r') as dnsfile:
	dnslist = json.load(dnsfile)
	for opt in dnslist:
		dns_options.append(DnsOption(opt['name'], opt['addr']))


vf = False
while vf == False:
	system("clear")
	novaLinha()
	print('\033[1;32m'+'-=-'*30)
	apresentacao()
	print('\nVersão: {}'.format(version))
	print('\n'+credit)
	print('\033[1;32m'+'-=-'*30)
	novaLinha()
	print('--- '*9)
	print('Quais servidores dns quer usar?')
	print('--- '*9)

	for i, opt in enumerate(dns_options):
		print(f'{i + 1}: {opt}')

	print('\n |0| - Sair                (Exit)')

	svr = str(input('\033[1;31m'+'\nConsole >>>'+' \033[0m'))
	svr = svr.strip()
	lista = ['1','2','3','4','5','6','7','8','9','10','11','12']

	if svr in ['0', 'back', 'exit', 'close', 'sair', 'fechar']:
		system("clear")
		break
	elif svr == '':
		print('Digite um comando!')
		sleep(2)
		continue

	if svr in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
		autochange.dnsserver(valor = svr)
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

