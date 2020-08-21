#	INI Data merge tool
#	Author:
#		Evgeniy Vigovskiy aka Weegee
#
#	Version:
#		1.0
#
#	Usage:
#		Merge all .INI file from the module into single file	
#
#		MergeDataModule.py <module.rte>
#
#	Example:
#		MergeDataModule.py Psyclones.rte
#
#	Warning:
#		This priimitive tool simply dumps all the contents of the ini files into single file to speed-up load times. 
#		It respects IncludeFile statetemnts and removes them from the output file.
#		It's intended to use only for mod creators to speed up game loading time when they have to reload the game very often to test stuff.
#

import sys
import os

def ParseFile(modpath, inifile, out, indent):
	print(inifile)
	
	input = open(os.path.join(modpath, inifile), 'r')
	lines = input.readlines()
	
	curobject = dict()
	
	nextcommentmode = False
	commentmode = False
	
	for l in lines:
		writeline = True
	
		#Discard comments
		cmnts = l.split("//")
		ln = cmnts[0]
		
		cmnts = ln.split("/*")
		ln = cmnts[0]
		if len(cmnts) > 1:
			nextcommentmode = True

		cmnts = ln.split("*/")
		if len(cmnts) > 1:
			ln = cmnts[1]
			nextcommentmode = False
			commentmode = False

		if not commentmode: 
			v = ln.split("=");
			t = list()

			for i in range(0, len(v)):
				v[i] = v[i].strip()
			
			if len(v) > 1:
				v[0] = v[0].lower()
				
				#Parse included files
				if v[0] == "includefile":
					ParseFile(modpath, v[1], out, True)
					writeline = False

		commentmode = nextcommentmode
		
		if writeline:
			if indent:
				out.write("\t" + l);
			else:
				out.write(l);

	out.write("\n");
	input.close()

RootFolder = sys.argv[1]
ModName = sys.argv[2]

OutputFile = os.path.join(RootFolder, ModName, "MergedIndex.ini");

out = open(OutputFile, 'w')

ParseFile(RootFolder, os.path.join(ModName, "Index.ini"), out, False)
	
out.close()