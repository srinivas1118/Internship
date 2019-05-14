import function
from parser import *

class Flash(function.Functions):

	# Function For Flashing Module
	@staticmethod
	def flash():
	
		#Flash.ch_dir('..')
		Flash.ch_dir('linux')
		
		
		Flash.unmount_device(sd_name+'*')
		
		cmd = [["sudo","dd","if=/dev/zero","of="+sd_name,"bs=512","count=1","conv=notrunc"],
			   ["sudo","parted","-s",sd_name,"mklabel","msdos"],
			   ["sudo","parted","-s",sd_name,"mkpart","primary","fat32",fat_start_size,fat_end_size ],
			   ["sudo","parted","-s",sd_name,"mkpart","primary","ext4",ext_start_size,ext_end_size],
			   ["sudo","mkfs.vfat",sd_name+"p1"],
			   ["sudo","mkfs.ext4","-F",sd_name+"p2"]]
		
		for val in cmd:
			Flash.subprocess(val)
		
		Flash.create_directory('mnt')
		Flash.create_directory('mnt/fat32')
		Flash.create_directory('mnt/ext4')
		
		
		Flash.mount_device(sd_name+"p1",'mnt/fat32')
		Flash.mount_device(sd_name+"p2",'mnt/ext4')
		
		Flash.create_directory('mnt/fat32/overlays')
		
		Flash.copy_single_content(zimage_path,'mnt/fat32/zImage')
		Flash.copy_multiple_files(dtb_path,'mnt/fat32/')
		Flash.copy_multiple_files(overlays_dtb_path,'mnt/fat32/overlays/')
		Flash.copy_single_content(readme_path,'mnt/fat32/overlays/')
		
		firm_url = firmware_path 
		bootcode_bin = firm_url+'/bootcode.bin'
		start_elf = firm_url+'/start.elf'
		fixup_dat = firm_url+'/fixup.dat'
		
		Flash.download(bootcode_bin)
		Flash.download(start_elf)
		Flash.download(fixup_dat)
		
		Flash.copy_single_content('bootcode.bin','mnt/fat32/')
		Flash.copy_single_content('start.elf','mnt/fat32/')
		Flash.copy_single_content('fixup.dat','mnt/fat32/')
		Flash.copy_single_content('boot.scr','mnt/fat32/')
		Flash.copy_single_content('u-boot.bin','mnt/fat32/kernel7.img')
		
		Flash.unmount_device('mnt/fat32')
		Flash.unmount_device('mnt/ext4')
		

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Function For Root File System Module 

	@staticmethod
	def root_file():
		
		Flash.ch_dir('..')

		Flash.create_directory('mnt')
		Flash.create_directory('mnt/ext4')

		Flash.mount_device(sd_name+"p2",'mnt/ext4')
		
		cmd = ["sudo", "tar", "-xzvf",fs_name, "-C", "mnt/ext4"]
		Flash.subprocess(cmd)
		print('\n  Compressed Root files are successfully extracted to the SD card  \n')

		Flash.unmount_device('mnt/ext4')

		Flash.ch_dir('linux')
		Flash.mount_device(sd_name+"p2",'mnt/ext4')
		

		cmd = ["sudo", "make", "ARCH=arm", "CROSS_COMPILE="+gcc_path, "INSTALL_MOD_PATH=mnt/ext4", "modules_install"]
		Flash.subprocess(cmd)
		print('\n  Loaded the kernel modules successfully \n')

		Flash.unmount_device('mnt/ext4')



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	
def flash_main():
	Flash.flash()
	Flash.root_file()



flash_main()
