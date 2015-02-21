'''
Generic system that basically digs deep into the folder specified, pulls out all links and then zips them via bzip2. Technically bzip2 could be replaced with whatever, but for my needs bzip2 was required.
Molded into a class so it can be dumped anywhere. Use the path karg to define where you want to pull your files from, and then  use PackageFiles to zip them up.
Will automatically ignore files with an already-in-use bz2 extension and hidden files on POSIX systems (. indication private / hidden file)

You can use this file independantly / without it being a class, just do <python3 bzapper.py 'path/to/folder'> and it'll work just as well. If you don't specify a path to a folder, 
	it'll auto look for a content folder instead.

Todo eventually: Try and restrain bz2 from eating up CPU like the filthy pig that it is (7zip support maybe?).
'''
import sys, os, subprocess

class Bzapper:

	validFilepaths=[]
	runningProcesses=[]
	maxProcesses = 3 #Change this to how many concurrent operations you want ongoing.
	
	def GrabAllLinks(self,path=os.getcwd() + '/content'):
	
		dirs = os.walk(path, followlinks=True)
	
		for filepath,irrelevant,files in dirs:
			for item in files:
				ext = os.path.splitext(item)[1]
				if ext == '.bz2':
					print('Cannot compress ' +item +' this due to ext being bz2.')
					continue
	
				if item[:1] == '.':
					continue
	
				fullURI = filepath + '/' + item 
				self.validFilepaths.append(fullURI)
	
	def PackageFiles(self):
		print('Starting compression of files!')
		self.maxProcesses
	
		while len(self.validFilepaths) > 1:
			if self.maxProcesses > 0:
				self.maxProcesses -= 1

				item = self.validFilepaths.pop()
				self.runningProcesses.append(subprocess.Popen(['bzip2', item]))
	
			for process in self.runningProcesses:
				if process.poll() == None:
					continue
				elif process.poll() == 0:
					self.runningProcesses.remove(process)
					self.maxProcesses += 1
				else:	
					print('Something went wrong! Halp, need an adult!')
					print('Code returned was: ' + process.returncode())
					return
	
		print('Finished compressing.')


if __name__ == '__main__':
	args = sys.argv

	zipit = Bzapper()

	if len(args) > 1 and args[1] != None:
		zipit.GrabAllLinks(path=args[1])
		zipit.PackageFiles()
	else:
		zipit.GrabAllLinks()
		zipit.PackageFiles()



