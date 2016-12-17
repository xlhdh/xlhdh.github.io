# from subprocess import * 
import sys

qual = sys.argv[1]
choice = sys.argv[2] # manifest or fragments

line = raw_input()
linenum = 1
while (line):
	base, start, nfrags, file_base = line.split(" , ")

	if choice=='manifest':
		print ' '.join(['echo','php',
			'../AdobeHDS.php',
			'--manifest', r"\'"+'$xF4M?$xAuth'+r"\'",
			'--auth', r"\'"+"$xAuth"+r"\'",
			'--start', str(start),
			'--quality', qual,
			'--nfrags', str(nfrags), 
			'--outfile', '$xComp\_'+str(linenum)+"_"+qual])

		print >>sys.stderr, ' '.join(['echo',
			'ffmpeg','-i','$xComp\_'+str(linenum)+"_"+qual+'.flv', 
			'-i','$xComp\_'+str(linenum)+"_"+str(56)+'.flv', 
			'-vcodec', 'copy',
			'-acodec', 'copy',
			'$xComp\_'+str(linenum)+'.flv'])

	elif choice=='fragments':
		print ' '.join(['echo','php',
			'../AdobeHDS.php',
			'--fragments', file_base,
			'--start', str(start),
			'--quality', str(56),
			'--nfrags', str(nfrags), 
			'--outfile', '$xComp\_'+str(linenum)+"_"+str(56)])
	else:
		exit()
	# Popen(['php',
	# 	'../AdobeHDS.php',
	# 	'--fragments', "b1d79ad25bd171dcce5419bdc3882950_3653299fa5624afb7c342e61a230fbe0_Seg1-Frag", 
	# 	'--start', str(start),
	# 	'--nfrags', str(nfrags), 
	# 	'--outfile', name+str(linenum)])
	linenum += 1
	try:
		line = raw_input()
	except:
		break


