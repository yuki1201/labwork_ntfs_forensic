import binascii
import re
import os
import types
# coding:utf_8
path ='./ディスクイメージ.img'
sector_num = int(int(os.path.getsize(path))/4096)
with open(path,"rb") as f:
	x=1

	while x <sector_num:
		seek_add=0
		y=0
		s=f.read(8).hex()
		if re.search(r'^504b0304', s) is not None:
			print('head'+hex(4096*x))
			for y in range(1,sector_num-x):
			#for y in range(1,2048):
				f.seek(4096*(x+y))
				s=f.read(4096).hex()
				if re.search(r'504b0506', s) is not None:
					f.seek(4096*x)
					s=f.read(4096*y).hex()
					s2=re.search(r'^504b0304.*5b436f6e74656e745f54797065735d2e786d6c.*?504b0506\w{36}', s)
					if s2 is not None:
						print(str(4096*y)+":"+hex(4096*x))
						#print(s[0])
						b_arr=binascii.unhexlify(s2[0])
						with open(str(hex(4096*x))+".docx", "wb") as fw:
							fw.write(b_arr)
						break
					s2=re.search(r'^504b0304.*?504b0506\w{36}', s)
					if s2 is not None:
						print(str(4096*y)+":"+hex(4096*x))
						#print(s[0])
						b_arr=binascii.unhexlify(s2[0])
						with open(str(hex(4096*x))+".zip", "wb") as fw:
							fw.write(b_arr)
							seek_add=y
						break

		if re.search(r'^ffd8ffe', s) is not None:
			print('headpic'+hex(4096*x))
			for y in range(1,sector_num-x):
			#for y in range(1,2048):
				#print(y)
				f.seek(4096*(x+y))
				s=f.read(4096).hex()
				if re.search(r'ffd900', s) is not None:
					print(str(y)+"***")
					f.seek(4096*x)
					s=f.read(4096*y).hex()
					s2=re.search(r'^ffd8ff.*?ffd900', s)
					if s2 is not None:
						print(str(4096*y)+":"+hex(4096*x))
						#print(s[0])
						try:
							b_arr=binascii.unhexlify(s2[0])
							with open(str(hex(4096*x))+".jpeg", "wb") as fw:
								fw.write(b_arr)
								seek_add=y
							break
						except:
							break
		#x=x+1+seek_add
		x=x+1
		f.seek(4096*x)