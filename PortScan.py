import socket

print("""

|=-=-=-=-=-=-=-=-=-=-=-=-=-=-|
| SCRIPT CODADO PELO SROLOKO |
|                            |
|        PORT SCANERR        |
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-|

""")

ip = raw_input("DIGITA A URL DO SITE: ")
for port in range(1,65535):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.05)
    if cliente.connect_ex((ip, port)) == 0:
        print "PORTA ",port," ABERTA"
        cliente.close()
