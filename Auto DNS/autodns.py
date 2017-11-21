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

def novaLinha():
	print('')

version = 1.1
credit = 'Codado por ~DRKmp~    Skype: derick-mp    Mail: derickmotta@outlook.com \n\nSalve a todos os membros do #UniãoHacker, tmj!'
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
	print(' |1| - Google: 8.8.8.8 e 8.8.4.4')
	print(' |2| - Level3: 4.2.2.1 e 4.2.2.2')
	print(' |3| - OpenNIC: 200.252.98.162')
	print(' |4| - opendns.org: 208.67.222.222 e 208.67.220.220')
	print(' |5| - gigadns.com.br: 189.38.95.95 e 189.38.95.96')
	print(' |6| - ScrubIt: 67.138.54.100 e 207.225.209.66')
	print(' |7| - Dnsadvantage: 156.154.70.1')
	print(' |8| - Brasil Telecom: 201.10.120.2')
	print(' |9| - Claro: 200.255.121.39 e 200.169.117.14')
	print('|10| - CTBC: 200.225.197.3 e 200.225.197.37')
	print('|11| - OI: 201.10.120.2')
	print('|12| - TIM: 208.67.222.222 e 208.67.220.220')
	print('\n |0| - Sair 				(Exit)')
	svr = str(input('\033[1;31m'+'\nConsole >>>'+' \033[0m'))
	svr = svr.strip()
	lista = ['1','2','3','4','5','6','7','8','9','10','11','12']

	if svr == '0' or svr == 'back' or svr == 'exit' or svr == 'close' or svr == 'sair' or svr == 'fechar':
		system("clear")
		break
	elif svr == '':
		print('Digite um comando!')
		sleep(2)
		continue

	if svr == '1' or svr == '2' or svr == '3' or svr == '4' or svr == '5' or svr == '5' or svr == '6' or svr == '7' or svr == '8' or svr == '9' or svr == '10' or svr == '11' or svr == '12':
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

