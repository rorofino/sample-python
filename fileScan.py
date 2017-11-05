import os
from itertools import chain

def levelSrtFiles(filename, fullpath, currentDirectory, subDirectories):
    mediaExtentions = ['.mp4', '.avi', '.mkv']
    fileExtention = filename[filename.rindex('.'):]
    if (fileExtention in mediaExtentions):
        for subDirectoryFilename in subDirectories:
            print(subDirectoryFilename)
            for dirname, dirnames, filenames in os.walk(os.path.join(currentDirectory, subDirectoryFilename)):
                for subDirectoryFilename in filenames:
                    if subDirectoryFilename.endswith('.srt') :
                        srcFilePath = os.path.join(dirname, subDirectoryFilename)
                        fileDestination = os.path.join(currentDirectory, subDirectoryFilename)
                        if os.path.isfile(fileDestination) :
                            print(srcFilePath, os.path.join(currentDirectory, '_'+subDirectoryFilename))
                        else:
                            print(srcFilePath, fileDestination)
    return

#mediaPaths = ['E:\Movies', 'E:\American Shows']
mediaPaths = ['E:\Movies']
# for dirname, dirnames, filenames in chain.from_iterable(os.walk(path) for path in mediaPaths):
#     for filename in filenames:
#         levelSrtFiles(filename, os.path.join(dirname, filename), dirname, dirnames)

for dirname, dirnames, filenames in chain.from_iterable(os.walk(path) for path in mediaPaths):
    srtFiles = {}
    for partialName in filenames:
        filename = os.path.join(dirname, partialName)
        if partialName.endswith('.srt') and not(partialName.endswith('.en.srt')) :
            srtFiles[filename] = os.path.getsize(filename)
    
    if (len(srtFiles.keys()) > 1):
        sortedLt = sorted(srtFiles, key=srtFiles.get, reverse=True)
        finalFileName = filename
        if not(finalFileName.endswith('.pt.srt')):
            finalFileName = finalFileName.replace('.srt', '.pt.srt')

        if sortedLt[0] != finalFileName:
            if os.path.isfile(finalFileName):
                print(finalFileName, 'OLD_'+finalFileName)

            print(sortedLt[0], finalFileName)
        