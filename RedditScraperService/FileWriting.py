def writeRidiculouslyHighOrLowToFile(comment):
    outFile = open("resources/files/ridiculouslyHighOrLowReason", "a")
    outFile.write(comment)
    outFile.write("\n\n")
    outFile.close()

def writeClosePositionFailureToFile(msg):
    outFile = open("resources/files/closePositionFailure", "a")
    outFile.write(msg+"\n\n")
    outFile.close()

def writeValidPositionsToFile(comment, newPosition):
    outFile = open("resources/files/commentFileOut", "a")
    outFile.write("\n\n")
    outFile.write(comment)
    outFile.write("\n")
    outFile.write(newPosition.__str__())
    outFile.write("\n\n")
    outFile.close()