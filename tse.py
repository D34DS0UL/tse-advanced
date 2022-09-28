from rich.progress import Progress
from rich.console import Console
from rich import print as rprint
from rich.progress import track
from bs4 import BeautifulSoup
from rich.table import Table
from time import sleep
import mechanize
import argparse
import climage
import signal
import sys
import os

 
def main():
	parser = argparse.ArgumentParser(description='CR DOXING TOOL')
	parser.add_argument('-N','--name', type=str,default=None,help='name from the target')
	parser.add_argument('--surname-1', type=str,default=None,help='first surname')
	parser.add_argument('--surname-2', type=str,default=None,help='last surname')
	parser.add_argument('-Ag','--age', type=int,default=None,help='age from the target')
	parser.add_argument('-Rg','--range-age', type=str,default=None,help='range of age from the target. ex: 18,21')
	parser.add_argument('-Bd','--birthday', type=str,default=None,help='birthday format: 01/12/1999')
	parser.add_argument('-Fn','--father-name', type=str,default=None,help='father name')
	parser.add_argument('-Mn','--mother-name', type=str,default=None,help='mother name')
	parser.add_argument('-Pv','--province', type=int,default=None,help='provinces:\nSanjose=1\nAlajuela=2\nCartago=3\nHeredia=4\nGuanacaste=5\nPuntarenas=6\nLimon=7\n')
	parser.add_argument('--proxy', type=str,default=None,help='set a proxy for private search')
	parser.add_argument('--timeout', type=float,default=None,help='set timeout. default = 0.5')
	parser.add_argument('--output', type=str,default=None,help='name for text file to save the output')
	args = parser.parse_args()
	sys.stdout.write(str(scrapper(args)))

# ----- define mechanize parameters -----

console = Console()
	
BR = mechanize.Browser()
BR.set_handle_robots(False)
BR.set_handle_equiv(False)
BR.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36')] 
URL = 'https://servicioselectorales.tse.go.cr/chc/consulta_nombres.aspx'

# ----- scrapper function -----

def signal_handling(signum,frame):
	os.system('clear')
	rprint("[bold red]El usuario aborto el programa")
	sys.exit()

signal.signal(signal.SIGINT,signal_handling)
def scrapper(args):
	outstr = []
	stxps = 1
	if args.proxy != None:
		stxps = stxps +1
		ctt = False
		pxtype = 'socks4' 
		pxstr = args.proxy
		if pxstr[0:7] == 'http://':
			bpnum = 7
			pxtype = 'http'
		elif pxstr[0:8] == 'https://':
			bpnum = 8
			pxtype = 'https'
		elif pxstr[0:9] == 'socks4://' or pxstr[0:9] == 'socks5://':
			pxtype = 'socks5'
			if pxstr[0:9] == 'socks4://':
				pxtype = 'socks4'
			bpnum = 9
		else:
			rprint("[red]El valor del proxy deve estar en el siguiente formato: '(http|https|socks4|socks5)://address:port'")
			exit()
		pxurl = pxstr[bpnum:]
		if pxurl.find('@') != -1:
			dpx = pxurl.split('@')
			cdt = dpx[0]
			if cdt.find(':') != -1:
				cdt = cdt.split(':')
				psswd = cdt[1]
				usrpx = cdt[0]
				ctt = True
				proxy = dpx[1]
			else:
				rprint("[red]El valor del proxy deve estar en el siguiente formato: 'http|https|socks4|socks5)://address:port'")
				exit()
			if proxy.find(':') != -1:
				proxy = proxy.split(':')
				pxport = proxy[1]
				proxy = proxy[0]
			else:
				rprint("[red]El valor del proxy deve estar en el siguiente formato: '(http|https|socks4|socks5)://address:port'")
				exit()	
		else:
			proxy = pxurl
			if proxy.find(':') != -1:
				proxy = proxy.split(':')
				pxport = proxy[1]
				proxy = proxy[0]				
		if ctt != False:
			BR.set_proxies(
			{pxtype: f"{pxtype}://{usrpx}:{psswd}@{proxy}:{pxport}"}
			)
		else:
			BR.set_proxies(
			{pxtype: f"{pxtype}://{proxy}:{pxport}"}
			)
	if args.timeout != None:
		stxps = stxps +1
		timeout = args.timeout
	else:
		timeout = 0.5
	if args.name == None:
		rprint("[red]El nombre de el objetivo es obligatorio")
		exit()
	stxps = stxps +1
	if args.surname_1 == None and args.surname_2 == None:
		rprint("[red]Es nesesario indicar almenos un apellido")
		exit()
	
	if args.surname_1 != None:
		stxps = stxps +1
		fsn = args.surname_1
	else:
		fsn = ""
	if args.surname_2 != None:
		stxps = stxps +1
		ssn = args.surname_2	
	else:
		ssn = ""	
	os.system("clear")
	outpt = climage.convert(".resources/icon.png",is_256color=True, width=50)
	print(outpt+"\n\n")
	rprint('[bold red]redes sociales:\n')
	rprint('[bold cyan]🕷  [bold wheat4]https://github.com/D34DS0UL                \n')
	rprint('[bold cyan]🕷  [bold wheat4]https://www.facebook.com/dead.soul.6669    \n')
	rprint('[bold cyan]🕷  [bold wheat4]https://www.instagram.com/_brain_death__/  \n')
	if args.proxy != None:
		rprint('[bold][cyan1]\n✅ [bold bright_cyan]conexion proxy establecida\n\n')
	with console.status("[bold wheat4]Agregando datos...") as status:
		for xvv in range(0,stxps):
			num = xvv
			sleep(1)
			console.log(f"[chartreuse4]Agregando parametros de busqueda...[/chartreuse4]")
		rprint("[bold red] Finalizado!\n\n")
	try:
		BR.open(URL)   
		BR.select_form(nr= 0)
	except:
		rprint("\n\n[red]Algo salio mal, checkee su internet y vulvalo a intentar\n")
		sleep(5)
		os.system('clear')
		for n in range(1,10):
			rprint('[bold red]ERROR')
			sleep(0.1)
		sleep(0.1)
		os.system('clear')
		exit()			
	nme = args.name
		
# ----- start scraping -----	

	BR.form[ 'txtnombre' ] = nme
	BR.form[ 'txtapellido1' ] = fsn
	BR.form[ 'txtapellido2' ] = ssn
	data = BR.submit('btnConsultarNombre')
	BR.select_form("form1")
	BR.find_control("chk2", type="checkbox").items[0].selected=True
	try:
		data = BR.submit("Button1")
		soup = BeautifulSoup(data, 'lxml')
	except:
		rprint("Error de conexion, asegurese de estar conectado a internet y vuelva a intentar")
		exit()
	try:
		date = soup.find('span', {'id': 'Label1'}) #lblmensajes
		page = date.text.split()
		page = int(page[7])
		cntr = page
		BR.back()
	except:
		BR.back()
		page = 1
		cntr = 1	
	try:
		BR.select_form("form1")
		BR.find_control("chk1$0", type="checkbox").items[0].selected=True
		data = BR.submit("Button1")	
	except:
		rprint("[red]Algo salio mal, checkee su internet y vulvalo a intentar")
		exit()
		
	soup = BeautifulSoup(data, 'lxml')

# ----- start get information -----
	
	table = Table(title="Personas")
	table.add_column("Num", style="cyan2", no_wrap=True)
	table.add_column("ID", style="light_sea_green")
	table.add_column("Nombre", style="dark_green")
	table.add_column("Nacimiento", style="dark_red")
	table.add_column("Edad", style="orange4")
	table.add_column("Nacionalidad", style="chartreuse4")
	table.add_column("Padre", style="grey37")
	table.add_column("ID", style="wheat4")
	table.add_column("Madre", style="medium_purple3")
	table.add_column("ID", style="light_slate_grey")
	table.add_column("Marginal", style="dark_slate_gray2")
	with Progress() as progress:
		taskn1 = progress.add_task("[bold red]Buscando...", total=100)
		for n in range(0,cntr):
			progress.update(taskn1, advance=2)
			dni = soup.find('span', {'id': 'lblcedula'})
			nmb = soup.find('span', {'id': 'lblnombrecompleto'})
			p_nmb = soup.find('span', {'id': 'lblnombrepadre'})
			p_dni = soup.find('span', {'id': 'lblid_padre'})
			m_nmb = soup.find('span', {'id': 'lblnombremadre'})
			m_dni = soup.find('span', {'id': 'lblid_madre'})
			bd = soup.find('span', {'id': 'lblfechaNacimiento'})
			ncd = soup.find('span', {'id': 'lblnacionalidad'})
			age = soup.find('span', {'id': 'lbledad'})
			mrg = soup.find('span', {'id': 'lblLeyendaMarginal'})
			chid = int(dni.text[0])
			ag = age.text.split()
			ag = int(ag[0])
			
	# ----- check arguments -----

			if args.age != None:
				if ag != args.age:
					sleep(timeout)
					BR.back()
					BR.select_form("form1")
					BR.find_control(f"chk1${n}", type="checkbox").items[0].selected=True
					data = BR.submit("Button1")
					soup = BeautifulSoup(data, 'lxml')
					continue						
			if args.birthday != None:
				if bd.text != args.birthday:
					sleep(timeout)
					BR.back()
					BR.select_form("form1")
					BR.find_control(f"chk1${n}", type="checkbox").items[0].selected=True
					data = BR.submit("Button1")
					soup = BeautifulSoup(data, 'lxml')
					continue		
			if args.father_name != None:
				try:
					nmp_1 = p_nmb.text.split()
					nmp_1 = nmp_1[0]
				except:
					nmp_1 = ""
				if nmp_1 != args.father_name.upper():
					sleep(timeout)
					BR.back()
					BR.select_form("form1")
					BR.find_control(f"chk1${n}", type="checkbox").items[0].selected=True
					data = BR.submit("Button1")
					soup = BeautifulSoup(data, 'lxml')				
					continue		
			if args.mother_name != None:
				try:
					nmm_1 = m_nmb.text.split()
					nmm_1 = nmm_1[0]
				except:
					nmm_1 = ""
				if nmm_1 != args.mother_name.upper():
					sleep(timeout)
					BR.back()
					BR.select_form("form1")
					BR.find_control(f"chk1${n}", type="checkbox").items[0].selected=True
					data = BR.submit("Button1")
					soup = BeautifulSoup(data, 'lxml')
					continue		
			if args.province != None:
				if chid != args.province:
					sleep(timeout)
					BR.back()
					BR.select_form("form1")
					BR.find_control(f"chk1${n}", type="checkbox").items[0].selected=True
					data = BR.submit("Button1")
					soup = BeautifulSoup(data, 'lxml')
					continue				
			rwcp = 'False'		
			if args.range_age != None:
				rag = args.range_age.split(',')
				try:
					ragi = int(rag[0])
					rage = int(rag[1])
					rage = rage+1
					if ragi > rage:
						sww = rage
						rage = ragi
						ragi = sww
				except:
					rprint('[bold red]Esto no es un rango de edad valido')
					exit()
				for nk in range(ragi,rage):
					if ag == nk:
						rwcp = 'True'
						break
					else:
						pass
				if rwcp != 'True':
					sleep(timeout)
					BR.back()
					BR.select_form("form1")
					BR.find_control(f"chk1${n}", type="checkbox").items[0].selected=True
					data = BR.submit("Button1")
					soup = BeautifulSoup(data, 'lxml')
					continue	
			if args.output != None:
				outstr.append(f"ID: {dni.text}\nNombre: {nmb.text}\nNacimiento: {bd.text}\nEdad: {age.text}\nNacionalidad: {ncd.text}\nPadre: {p_nmb.text}\nID: {p_dni.text}\nMadre: {m_nmb.text}\nID: {m_dni.text}\nMarginal: {mrg.text}\n\n\n")
			table.add_row(str(n),dni.text,nmb.text,bd.text,age.text,ncd.text,p_nmb.text,p_dni.text,m_nmb.text,m_dni.text,mrg.text)
			sleep(timeout)
			BR.back()
			try:
				BR.select_form("form1")
			except:
				rprint("[red]Algo salio mal, checkee su internet y vulvalo a intentar")
				exit()		
			try:
				BR.find_control(f"chk1${n}", type="checkbox").items[0].selected=True
			except:
				rprint("[red]Algo salio mal, checkee su internet y vulvalo a intentar")
				exit()					
			data = BR.submit("Button1")
			soup = BeautifulSoup(data, 'lxml')
	os.system('clear')
	console.print(table)
	if args.output != None:
		nmout = args.output
		with open(f'{nmout}_output.txt','w') as svot:
			for element in outstr:
				svot.write(element)
			svot.close()
	exit()
	
	
if __name__ == '__main__':
	main()
