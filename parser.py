from xml.dom.minidom import parse
import xml.dom.minidom


def open_xml(): 

	global DOMTree, start
	DOMTree = xml.dom.minidom.parse("config.xml")
	start = DOMTree.documentElement


def download_link():
	
	global kernels,uboots,gcc_link,linux, u_boot_link, boot_scr_link
	
	kernels = start.getElementsByTagName("kernel")
	for kernel in kernels:
		gcc_link = kernel.getElementsByTagName('gcc_d_link')[0].childNodes[0].data
		linux = kernel.getElementsByTagName('linux_d_link')[0].childNodes[0].data
		
	uboots=start.getElementsByTagName("uboot")
	for uboot in uboots:
		u_boot_link = uboot.getElementsByTagName('u_boot_d_link')[0].childNodes[0].data
		boot_scr_link = uboot.getElementsByTagName('boot_scr_d_link')[0].childNodes[0].data
		
		
def get_tar_files():
	
	global gcc_fname, gcc_dest , extract_uboot
	
	for kernel in kernels:
		extracts= kernel.getElementsByTagName("extract")
		for extract in extracts:
			gcc_fname = kernel.getElementsByTagName('f_name')[0].childNodes[0].data
			gcc_dest = kernel.getElementsByTagName('dest')[0].childNodes[0].data
			
	for uboot in uboots:
		extract_uboot = uboot.getElementsByTagName('extract_f_name')[0].childNodes[0].data
	
 
def get_version():
	
	global kernel_version
	
	for kernel in kernels:
		kernel_version = kernel.getElementsByTagName('kernel_version')[0].childNodes[0].data
		

def get_config():
	
	global gcc_path, board_config,u_boot_config
	
	for kernel in kernels:
		configs= kernel.getElementsByTagName("config")
		for config in configs:
			gcc_path = config.getElementsByTagName('gcc_path')[0].childNodes[0].data
			board_config = config.getElementsByTagName('board_config')[0].childNodes[0].data
	
	for uboot in uboots:
		configs= uboot.getElementsByTagName("config")
		for config in configs:
			u_boot_config = config.getElementsByTagName('uboot_conf')[0].childNodes[0].data 


def get_boot_files():

	global img_type,modules,dtbs,scr_name
	
	for kernel in kernels:
		images= kernel.getElementsByTagName("image")
		for image in images:
			img_type= image.getElementsByTagName('img_type')[0].childNodes[0].data
			modules= image.getElementsByTagName('modules')[0].childNodes[0].data
			dtbs= image.getElementsByTagName('dtb')[0].childNodes[0].data
			
	for uboot in uboots:		
		scr_name= uboot.getElementsByTagName('scr_name')[0].childNodes[0].data
	
def get_boot_files_path():
		
		global zimage_path,dtb_path,overlays_dtb_path,readme_path
		
		flashing=start.getElementsByTagName("flash")
		for flash in flashing:
			zimage_path= flash.getElementsByTagName('zimage_path')[0].childNodes[0].data
			dtb_path= flash.getElementsByTagName('dtb_path')[0].childNodes[0].data
			overlays_dtb_path= flash.getElementsByTagName('overlays_dtb_path')[0].childNodes[0].data
			readme_path= flash.getElementsByTagName('readme_path')[0].childNodes[0].data
		

def change_dir():
	
	global uboot_dir_name
	
	for uboot in uboots:
		uboot_dir_name= uboot.getElementsByTagName('ch_dir_name')[0].childNodes[0].data
	
def get_sd_name():

	global sd_name
	
	flashing=start.getElementsByTagName("flash")
	for flash in flashing:
		sd_name = flash.getElementsByTagName('sd_name')[0].childNodes[0].data
	
def get_partition_details():

	global fat_start_size,fat_end_size,ext_start_size,ext_end_size
	
	flashing=start.getElementsByTagName("flash")
	for flash in flashing:
	
		fat32= flash.getElementsByTagName("fat_32")
		for fat_32 in fat32:
			fat_start_size = fat_32.getElementsByTagName('start_size')[0].childNodes[0].data	
			fat_end_size = fat_32.getElementsByTagName('end_size')[0].childNodes[0].data
			
		ext4= flash.getElementsByTagName("ext4")
		for ext_4 in ext4:
			ext_start_size= ext_4.getElementsByTagName('start_size')[0].childNodes[0].data	
			ext_end_size= ext_4.getElementsByTagName('end_size')[0].childNodes[0].data
			
			
def get_firmware_files():
	
	global firmware_path
	
	firm = start.getElementsByTagName("firmware")
	for firmware in firm:
		firmware_path = firmware.getElementsByTagName('d_link')[0].childNodes[0].data
	
	


def get_rfs():

	global fs_name
	
	rfs = start.getElementsByTagName("rootfs")
	for rootfs in rfs:
		fs_name = rootfs.getElementsByTagName('f_name')[0].childNodes[0].data



def main():
	
	open_xml()
	download_link()
	get_tar_files()
	get_version()
	get_config()
	get_boot_files()
	get_boot_files_path()		
	change_dir()
	get_sd_name()	
	get_partition_details()
	get_rfs()
	get_firmware_files()
		
main()

print "imported variables\n"

