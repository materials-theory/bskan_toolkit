import os, shutil, glob
import math 
import sys
import time

print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print "!!                                                                                         !!"
print "!!                         Welcome to CURSAVE2CURRENT python code                          !!"
print "!!                                                                                         !!"
print "!!         This code convert CURSAVE file (BSKAN) to CURRENT file (CHGCAR format)          !!"
print "!!                                                                                         !!"
print "!!                  Please DELETE the first line of CURSAVE 'Backup file'                  !!"
print "!!                                                                                         !!"
fft_grid = raw_input("                       INPUT the FFT grid (nx ny nz). e.g. 73 37 101: ");
fft_split = fft_grid.split();

fft_nx = fft_split[0]
fft_ny = fft_split[1]
fft_nz = fft_split[2]

fft_total = int(fft_nx) * int(fft_ny) * int(fft_nz) 

f = open("CURSAVE", 'r')
lines = f.readlines()
f.close()

cnt = 1
fileName_nx = 1
fileName_ny = 1

method = raw_input("                              Type the STM method, TH or Chen: ");

###Tersoff-Hamann method
if method == "TH":
    ## divider part
    for line in lines:
        fileName = "CURSAVE_" + str(fileName_nx) + "_" + str(fileName_ny) + ".txt"

        fw = open(fileName, "a")
        fw.write(line)
        fw.close()

        if cnt == int(fft_nz) + 1:
            if fileName_ny != int(fft_ny):
                fileName_ny = fileName_ny + 1
            else:
                fileName_ny = 1
                fileName_nx = fileName_nx + 1
            cnt = 0

        cnt = cnt + 1


    ## converter part
    nx = 1
    for nz in range(1, int(fft_nz)+1):
        for ny in range(1, int(fft_ny)+1):
            for nx in range(1, int(fft_nx)+1): 
                fr = open("CURSAVE_%s_%s.txt" % (str(nx), str(ny)), 'r')
                lineslines = fr.readlines()
                fr.close()

                ftw = open("CURRENT_temp", "a")
                ftw.write(lineslines[nz])
                ftw.close()


    ## make archive folder to back up the divided files
    dirname = '/user/aaa'
    if not os.path.isdir('./archive'):
        os.mkdir('./archive')

    src = "./"
    dst = "./archive"

    for txt_file in glob.glob(src+"/*.txt"):
        shutil.move(txt_file, dst);


    ## rearrange CURRENT_temp to CURRENT
    ftr = open('./CURRENT_temp')
    ftr_split = [float(num) for num in ftr.read().split()];

    save = open("CURRENT", "w")

    if fft_total % 5 == 0:
        for i in range(0, fft_total, 5):
            print >> save, str(ftr_split[i])+"   "+str(ftr_split[i+1])+"   "+str(ftr_split[i+2])+"   "+str(ftr_split[i+3])+"   "+str(ftr_split[i+4])+"   "
    else:
        fft_max = int(fft_total / 5) * 5
        fft_remain = fft_total - fft_max
        for i in range(0, fft_max, 5):
            print >> save, str(ftr_split[i])+"   "+str(ftr_split[i+1])+"   "+str(ftr_split[i+2])+"   "+str(ftr_split[i+3])+"   "+str(ftr_split[i+4])+"   "
        print >> save, '   '.join([str(ftr_split[j]) for j in range(fft_total-fft_remain, fft_total)])
    print "!!                                                                                         !!"
    print "!!                                        JOBS DONE                                        !!"
    print "!!                                                                                         !!"
    print "!! PLEASE CHECK the initial value and the final value in CURRENT_temp and CURRENT are SAME !!"
    print "!!                                                                                         !!"
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

###Chen method
elif method == "Chen":
    volume = raw_input("                                      Type the volume: ");
    ## divider part
    for line in lines:
        fileName = "CURSAVE_" + str(fileName_nx) + "_" + str(fileName_ny) + ".txt"

        fw = open(fileName, "a")
        fw.write(line)
        fw.close()

        if cnt == int(fft_nz) + 1:
            if fileName_ny != int(fft_ny):
                fileName_ny = fileName_ny + 1
            else:
                fileName_ny = 1
                fileName_nx = fileName_nx + 1
            cnt = 0

        cnt = cnt + 1


    ## converter part
    nx = 1
    for nz in range(1, int(fft_nz)+1):
        for ny in range(1, int(fft_ny)+1):
            for nx in range(1, int(fft_nx)+1): 
                fr = open("CURSAVE_%s_%s.txt" % (str(nx), str(ny)), 'r')
                lineslines = fr.readlines()
                fr.close()

                ftw = open("CURRENT_temp", "a")
                ftw.write(str(float(lineslines[nz])/float(volume))+"\n")
                ftw.close()


    ## make archive folder to back up the divided files
    dirname = '/user/aaa'
    if not os.path.isdir('./archive'):
        os.mkdir('./archive')

    src = "./"
    dst = "./archive"

    for txt_file in glob.glob(src+"/*.txt"):
        shutil.move(txt_file, dst);


    ## rearrange CURRENT_temp to CURRENT
    ftr = open('./CURRENT_temp')
    ftr_split = [float(num) for num in ftr.read().split()];

    save = open("CURRENT", "w")

    if fft_total % 5 == 0:
        for i in range(0, fft_total, 5):
            print >> save, str(ftr_split[i])+"   "+str(ftr_split[i+1])+"   "+str(ftr_split[i+2])+"   "+str(ftr_split[i+3])+"   "+str(ftr_split[i+4])+"   "
    else:
        fft_max = int(fft_total / 5) * 5
        fft_remain = fft_total - fft_max
        for i in range(0, fft_max, 5):
            print >> save, str(ftr_split[i])+"   "+str(ftr_split[i+1])+"   "+str(ftr_split[i+2])+"   "+str(ftr_split[i+3])+"   "+str(ftr_split[i+4])+"   "
        print >> save, '   '.join([str(ftr_split[j]) for j in range(fft_total-fft_remain, fft_total)])
    print "!!                                                                                         !!"
    print "!!                                        JOBS DONE                                        !!"
    print "!!                                                                                         !!"
    print "!! PLEASE CHECK the initial value and the final value in CURRENT_temp and CURRENT are SAME !!"
    print "!!                                                                                         !!"
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

else:
    print "!!                                                                                         !!"
    print "!!                                       WRONG INPUT                                       !!"
    print "!!                                                                                         !!"
    print "!!                             TH or Chen is only available                                !!"
    print "!!                                                                                         !!"
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    

