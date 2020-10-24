from socket import *
import optparse
from threading import *
from termcolor import colored

def connScan(host,port):
	try:
		s=socket(AF_INET,SOCK_STREAM)
		s.connect((host,port))
		print (colored('[+] %d tcp open ' %(port),'green'))
	except:
		print (colored('[+] %d tcp closed ' %(port),'red'))
	

def portscan(tgthost,tgtports):
	try:
		ip=gethostbyname(tgthost)
	except:
		print('Unknow Host %s ' %(tgthost))
	try:
		name=gethostbyaddr(tgtip)
		print( '[+] Scan Results for : '+ name[0])
	except:
		print('[+] Scan Resuts for : ' + ip)
	setdefaulttimeout(1)
	if tgtports[0]=='all':
		for i in range(1,1000):
			connScan(tgthost,i)
	else:
		for port in tgtports:
			t=Thread(target=connScan,args=(tgthost,int(port)))
			t.start()

def main():
	parser=optparse.OptionParser('Usage of program : ' + '-H <targer host> -p <targer ports> or all')
	parser.add_option('-H',dest='tgthost',type='string',help='specify targer host')
	parser.add_option('-p',dest='tgtports',type='string',help='specify targer ports')
	(options,args)=parser.parse_args()
	tgthost=options.tgthost
	tgtports=str(options.tgtports).split(',')
	if(tgthost==None)| (tgtports[0]==None):
		print (parser.usage)
		exit(0)
	portscan(tgthost,tgtports)
	
if __name__=='__main__':
	main()

	
