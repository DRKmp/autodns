#!usr/bin/env python
# -*- coding: utf-8 -*-

from os import system
from time import sleep

def novaLinha():
    print('')

#Função para fazer backup do arquivo de configurações DNS localizado em
## '/etc/resolv.conf'
def mkbak(yon):

#Se fazer backup for igual a 'sim':
    while True:
        if yon == 'y' or yon == 'Y':
            system('echo > ~/resolv.conf.bakAutoDns')
            system('cp /etc/resolv.conf ~/resolv.conf.bakAutoDns')
            system("echo '#Backup gerado pelo Auto DNS' >> ~/resolv.conf.bakAutoDns")
            print('\nBackup salvo na sua /home')
            sleep(2)
            return False
            continue

        if yon == 'n' or yon == 'N':
            system("clear")
            print('Ok! Prosseguindo...')
            sleep(2)
            return False
            continue
        elif yon != 'y' or yon != 'Y':
            print('Opção inválida! Considerando [y].')
            yon = 'y'
            sleep(3)
            return False
            continue
        elif yon != 'n' or yon != 'N':
            print('Opção inválida! Considerando [y].')
            yon = 'y'
            sleep(3)
            return False
            continue

#Função para verificar se deseja fazer backup e setar as configurações
def dnsserver(valor):
#Verifica se deseja realizar backup do arquivo 'resolv.conf' em '/etc'. 
#Chama a função 'mkbak' passando o valor de 'bak' como argumento.
    system("clear")
    print('-=-'*25)
    bak = str(input('Deseja fazer um backup agora? *O backup será feito em sua /home'+'\n'+'-=-'*25 +'\n[y/n]: '))
    mkbak(yon = bak)

#Adiciona os valores conrrespondentes a opção selecionada no menu.
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
###

#Utiliza os valores recebidos nas variáveis 'dns1', 'dns2', 'dns_n' e adiciona ao arquivo de configurações DNS
##localizado em 'etc/resolv.conf'
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
###
