# coding: utf-8
import sys
import os
import urllib


csv_file = open(sys.argv[1],"r")
for num_line,line in enumerate(csv_file):
    list_line=line.split(",")
    SKU_found=False
    index_for_img=1
    for i,l in enumerate(list_line):
        if l.endswith(sys.argv[2]):
            if SKU_found==False:
                if list_line[i-1]=='':
                    SKU=list_line[i-2]
                else:
                    SKU=list_line[i-1]
                SKU_found=True
                if not os.path.exists(SKU):
                    os.makedirs(SKU)
            urllib.urlretrieve(l, SKU+"/"+SKU+"_"+str(index_for_img)+".jpg")
            index_for_img+=1
    print "line",num_line+1
csv_file.close()
print "done"