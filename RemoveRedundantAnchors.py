import os, sys, glob, re
from utilities import *

inFilePath = sys.argv[1]

text = readTextFromFile(inFilePath)

pattern = '<a href="#.*?">'

p = re.compile(pattern, re.IGNORECASE)

uniqueMatches = set([match.group() for match in re.finditer(p, text)])

for match in uniqueMatches:
    #re.purge() # clear the cache

    p = re.compile(match, re.IGNORECASE)

    subMatchPositions = []
    for subMatch in re.finditer(p, text):
        subMatchPositions.append(subMatch.span())

    if len(subMatchPositions) < 2:
        continue

    subMatchPositions.pop(0)

    for position in reversed(subMatchPositions):
        text = text[:position[0]] + text[position[1]:]

writeScalarToFile(text, inFilePath)
