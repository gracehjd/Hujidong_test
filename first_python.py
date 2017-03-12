# -*- coding: utf-8 -*-

import os
/*
Source_root = 'G:/Workspace/sockit_gnss'
out_name = "sockit.txt"

p=os.listdir(source_root)
file_list = []
def add_filename(source_root,p,file_list):
    for i in p:
        if i.endswith('.h') or i.endswith('.c'):
            file_list.append(os.path.join(os.path.abspath(source_root), i))
    for i in p:
        _path=os.path.join(os.path.abspath(source_root), i)
        if os.path.isdir(_path):
            add_filename(_path,os.listdir(_path), file_list)



add_filename(source_root,p,file_list)   
for i in file_list:
    print i
    
fout=open(out_name,'w')
for fpath in file_list:
    fin=open(fpath,'r')
    text = ''
    for line in fin.readlines():
        if line.strip():
            if not line.strip().startswith('//'):
                text += line.rstrip()+'\n'
    fout.write("// "+fpath[len(os.path.abspath(source_root))+1:].replace('\\','/')+'\n')
    fout.write(text+'\n\n')

fin.close()
fout.close()

*/

print "OK!!!!!"

