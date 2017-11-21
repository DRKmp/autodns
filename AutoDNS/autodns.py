#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################
#                              #
#     Software: Auto DNS       #
#     Versão  : 1.0            #
#     Cod. by : ~DRK~          #
#                              #
################################

from time import sleep
from os import system
from func.autoip_title import apresentacao
from func.autoip_change import dnsserver

def novaLinha():
	print('')

vf = False
version = 1.0
credit = 'Codado por ~DRKmp~    Skype: derick-mp    Mail: derickmotta@outlook.com'
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
	print('Lista de servidores \n---')
	print("""|1| - Google: 8.8.8.8 e 8.8.4.4
|2| - Level3: 4.2.2.1 e 4.2.2.2
|3| - OpenNIC: 200.252.98.162
|4| - opendns.org: 208.67.222.222 e 208.67.220.220
|5| - gigadns.com.br: 189.38.95.95 e 189.38.95.96
|6| - ScrubIt: 67.138.54.100 e 207.225.209.66
|7| - Dnsadvantage: 156.154.70.1
|0| - Sair 					      (Exit)
------------------------------------------------------------""")
	svr = str(input('\033[1;31m'+'\nConsole >>>'+' \033[0m'))
	svr = svr.strip()
	if svr == '0' or svr == 'back' or svr == 'exit' or svr == 'close' or svr == 'sair' or svr == 'fechar':
		system("clear")
		break
	
	if svr == '':
		continue
	dnsserver(valor = svr)

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

