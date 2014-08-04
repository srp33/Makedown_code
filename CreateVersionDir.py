import os, sys, glob
from time import gmtime, strftime

destParentDirPath = sys.argv[1]

timeStamp = strftime("%Y/%m/%d/%H_%M_%S", gmtime())

destDirPath = "%s/%s" % (destParentDirPath, timeStamp)
os.makedirs(destDirPath)

print destDirPath
