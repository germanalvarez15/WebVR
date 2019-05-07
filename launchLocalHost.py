import os

def launch():
		print("RECUERDA TENER PYTHON2 INSTALADO")
		port = input('Numero de puerto: ')
		line = 'python -m SimpleHTTPServer ' + str(port)
		return line
os.system(launch())
