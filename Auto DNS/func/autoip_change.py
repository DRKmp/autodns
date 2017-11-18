#!usr/bin/env python
# -*- coding: utf-8 -*-

from os import system
from time import sleep

backup = False

def novaLinha():
    print('')

def mkbak(yon):
    if yon == 'y' or yon == 'Y':
        system('cp /etc/resolv.conf ~/resolv.conf.bakAutoDns')
        system("echo '#Backup gerado pelo Auto DNS' >> ~/resolv.conf.bakAutoDns")
        print('Backup salvo na sua /home')
        sleep(2)
        backup = True

    if yon == 'n' or yon == 'N':
        system("clear")
        print('Ok! Prosseguindo...')
        sleep(2)
        backup = True

def dnsserver(valor):

    if backup == False:
        system("clear")
        bak = str(input('Deseja fazer um backup agora? [y/n]: '))
        mkbak(yon = bak)

    if valor == '1':
        dns1 = '8.8.8.8'
        dns2 = '8.8.4.4'
        dns_n = 'Google'

    if valor == '2':
        dns1 = '4.2.2.1'
        dns2 = '4.2.2.2'
        dns_n = 'Level3'

    if valor == '3':
        dns1 = '200.252.98.162'
        dns2 = ''
        dns_n = 'OpenNIC'

    if valor == '4':
        dns1 = '208.67.222.222'
        dns2 = '208.67.220.220'
        dns_n = 'OpenDns.org'

    if valor == '5':
        dns1 = '189.38.95.95'
        dns2 = '189.38.95.96'
        dns_n = 'GigaDns.com.br'

    if valor == '6':
        dns1 = '67.138.54.100'
        dns2 = '207.225.209.66'
        dns_n = 'ScrubIt'

    if valor == '7':
        dns1 = '156.154.70.1'
        dns2 = ''
        dns_n = 'Dns Advantage'

    system("clear")
    print('-=-'*20)
    print("""DNS escolhido: {}
IP: {} e {}""".format(dns_n, dns1, dns2))
    system('echo > /etc/resolv.conf') #Apaga tudo dentro de /etc/resolv.conf
    system("echo '#Gerado por Auto DNS' >> /etc/resolv.conf") #Créditos
    system("echo '#{} DNS' >> /etc/resolv.conf".format(dns_n)) #Comenta o DNS usado
    system("echo 'nameserver {}' >> /etc/resolv.conf".format(dns1)) #DNS Primário
    system("echo 'nameserver {}' >> /etc/resolv.conf".format(dns2)) #DNS Secundário
    novaLinha()
    print('DNS {} configurado!'.format(dns_n))
    print('Boa navegação!')
    print('-=-'*20)
    input('Pressione <enter> para voltar ao menu principal...')
