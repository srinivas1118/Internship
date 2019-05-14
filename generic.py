import function

from parser import *

class Modules(function.Functions):

# Function for Kernel Module	
	@staticmethod
	def kernel_compile():
		
			Modules.download(gcc_link)
			cmd = ["git", "clone", linux]
			Modules.subprocess(cmd)
			print('Linux source file successfully fetched')

			cmd = ["tar", "-xf", gcc_fname, "-C", gcc_dest]
			Modules.subprocess(cmd)
			print('Gcc-arm successfully extracted')
			
			Modules.ch_dir('linux')
			
			val = kernel_version
			Modules.subprocess_Popen(val)
			print('Kernel version set to kernel7')

		
			Modules.config("CROSS_COMPILE="+gcc_path,board_config)
			print('Configuration of Kernel done!')

			cmd = ["make", "ARCH=arm","CROSS_COMPILE="+gcc_path, img_type, modules, dtbs]
			Modules.subprocess(cmd)
			print('Zimage generated successfully')

		
			
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------			

# Function for U-Boot module	
	@staticmethod
	def uboot_compile():
			
			Modules.ch_dir('..')
			Modules.download(u_boot_link)
			Modules.extract_tar( '-xjf',extract_uboot)
			
			Modules.ch_dir(uboot_dir_name)
			
			Modules.download(gcc_link)
			Modules.extract_tar('-xf',gcc_fname)
			
			Modules.config("CROSS_COMPILE="+gcc_path,u_boot_config)
			
			cmd = ["make","ARCH=arm","CROSS_COMPILE="+gcc_path]
			Modules.subprocess(cmd)
			
			print "compiling of uboot completed!!"
			print "------------------------------------------------------------"
			
			Modules.download(boot_scr_link)
			cmd = 'mkimage -A arm -T script -C none -n "Boot script" -d ' +scr_name+ ' boot.scr '
			Modules.os_call(cmd)
			print "boot.scr created!!" 
			
			Modules.copy_single_content('boot.scr','../linux/')
			print('Boot.scr copying done!')
			Modules.copy_single_content('u-boot.bin','../linux/')
			print('U-boot.bin copying done!')
		
			print "------------------------------------------------------------"
		


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------		



# Function For Copying Image Files Module 
	@staticmethod
	def copy_image_files():
		#Modules.ch_dir('..')
		Modules.create_directory('images')
		flash_single_contents = ['config.xml','parser.py','function.py','generic.py','ubuntumate_root_file.tar.gz','log.txt','flash.py']
		flash_dir_contents = ['linux','u-boot-2017.09']
		for content in flash_single_contents:
			Modules.copy_single_content(content,'images/')
		for content in flash_dir_contents:
			Modules.copy_dir(content,'images/')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def main():


	#Modules.kernel_compile()
	#Modules.uboot_compile()
	Modules.copy_image_files()
	




main()	
