import os, sys, glob

inFilePath = sys.argv[1]
outFilePath = sys.argv[2]

def buildTable(filePath):
    checkFileExists(filePath)
    out = ""

    tableFile = open(filePath)
    headerItems = tableFile.readline().rstrip().split("\t")

    out += "| " + " | ".join(headerItems) + " |\n"
    out += "|" + "|".join(["------" for x in headerItems]) + "|\n"

    lineCount = 0
    for line in tableFile:
        lineCount += 1
        lineItems = line.rstrip().split("\t")
        out += "|" + "|".join(lineItems) + "|\n"

#        if lineCount == 100:
#            break

    return out

def buildFigure(filePath):
    checkFileExists(filePath)

    newFilePath = filePath
    if filePath.endswith(".pdf"):
        newFilePath = "/tmp/" + os.path.basename(inFilePath) + "__" + os.path.basename(filePath).replace(".pdf", ".png")
        os.system("./scripts/convert_pdf_to_png %s %s" % (filePath, newFilePath))

    return "![](%s)\n" % newFilePath

def checkFileExists(filePath):
    if not os.path.exists(filePath):
        print "No file exists at %s" % filePath
        exit(1)

inFile = open(inFilePath)
outFile = open(outFilePath, 'w')

for line in inFile:
    if line.strip().startswith("@"):
        continue

    if line.startswith("Table:"):
        tableFilePath = line.rstrip().replace("Table:", "")

        if tableFilePath.endswith(".txt"):
            outFile.write(buildTable(tableFilePath))
    elif line.startswith("Figure:"):
        figureFilePath = line.rstrip().replace("Figure:", "")
        outFile.write(buildFigure(figureFilePath))
    else:
        outFile.write(line)

outFile.close()
inFile.close()
