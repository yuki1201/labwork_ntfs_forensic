# coding:utf_8
import binascii
import re
import os
import types
import codecs
path ='./ディスクイメージ.img'
sector_num = int(int(os.path.getsize(path))/256)
list_fname=[]
with open(path,"rb") as f:
	x=1
	while x <sector_num:
		s=f.read(10).hex()

		if re.search(r'^46494c4530', s) is not None:
			#print(s)
			s=f.read(512).hex()
			result = re.findall(r'30000000\w{152}2000000000000000', s)
			if len(result)>0:
				#print([m.end() for m in re.finditer(r'30000000\w{152}2000000000000000', s)])
				name_len=int(s[460:462],16)
				#print(codecs.decode(s[463:463+(name_len*4)],'hex_codec'))
				#print(hex(256*x)+":"+str(name_len)+":"+s[462:462+(name_len*4)])
				try:
					file_name=hex(256*x)+":"+binascii.unhexlify(s[462:462+(name_len*4)]).decode('ascii')
					print(file_name)
					list_fname.append(file_name)
					list_fname.append('\n')
				except:
					pass
		x=x+1
		f.seek(256*x)
with open("filenames.txt", "w") as f:
	f.writelines(list_fname)