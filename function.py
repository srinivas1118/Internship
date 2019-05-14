import subprocess
import os

class Functions:

	@staticmethod
	def subprocess(arg):
		subprocess.call(arg)
		
	@staticmethod
	def download(url):
		cmd = ['sudo','wget',url]
		Functions.subprocess(cmd)
		print "file is downloaded!!"
		print "------------------------------------------------------------"
	
	@staticmethod
	def subprocess_Popen(arg):
		return subprocess.Popen(arg,shell=True)
	
	@staticmethod
	def os_call(arg):
		os.system(arg)

	@staticmethod
	def extract_tar(option,url):
		cmd = ['tar',option, url]
		Functions.subprocess(cmd)
		print "extracting of tar file finished!!"
		print "------------------------------------------------------------"

	@staticmethod
	def ch_dir(cd):
		os.chdir(cd)
		print "changed the directory to "
		cmd = ['pwd']
		Functions.subprocess(cmd)
		print "------------------------------------------------------------"
	
	@staticmethod	
	def config(cross_compiler,rpi_bits):
		cmd = ["make","ARCH=arm",cross_compiler,rpi_bits]
		Functions.subprocess(cmd);
		print "config file created!!"
		print "------------------------------------------------------------"""
	
	@staticmethod
	def unmount_device(device_name):
		strng='sudo umount '+device_name                                       
		a= Functions.subprocess_Popen(strng)
		a.wait()
		print("Unmounted %s" %device_name)
		print "------------------------------------------------------------"

	@staticmethod
	def create_directory(dir_name):
		Functions.subprocess(["sudo","mkdir",dir_name])
		print("%s created" %dir_name)
		print "------------------------------------------------------------"

	@staticmethod
	def mount_device(device_name,mount_target):
		strng='sudo mount '+device_name+' '+mount_target
		p= Functions.subprocess_Popen(strng)
		p.wait()
		print "Partition mounted"
		print "------------------------------------------------------------"

	@staticmethod
	def copy_single_content(source,dest):
		Functions.subprocess(["sudo","cp",source,dest]);
		print("Contents copied from %s to %s" %(source,dest))
		print "------------------------------------------------------------"
	
	@staticmethod
	def copy_multiple_files(source,dest):
		strng='sudo cp '+source+' '+dest
		r=Functions.subprocess_Popen(strng)
		r.wait()

	@staticmethod
	def copy_dir(source,dest):
		Functions.subprocess(["sudo","cp","-R",source,dest]);
		print("Contents copied from %s to %s" %(source,dest))
		print "------------------------------------------------------------"


