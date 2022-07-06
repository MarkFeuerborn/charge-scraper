import requests
from subprocess import call

def DownloadFile(url, pathToOutput):
    # create the filename from the download filename
    filename = pathToOutput + '/' + url.split('/')[-1]
    
    # this is a bit of a one-off but some URLs use ? to do a sort of cache control; but we don't want it in the filename
    if "?" in filename:
        filename = filename.split('?')[0]

    print("Downloading " + url + " to " + filename)

	# Uses requests again to actually grab the file and save it
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    print("File downloaded")
    
    # send the new filename back
    return filename

def CopyToDropbox(pathToDropbox, pathToSrcFile):
        
    # figure out the filename
    srcFile = pathToSrcFile.split('/')[-1]
        
    print("Copying {} to Dropbox".format(srcFile))
    Upload = '{}/dropbox_uploader.sh upload {} {}'.format(pathToDropbox, pathToSrcFile, srcFile)
    call ([Upload], shell=True)

def WriteLatest(issue, filename):
    l = RetrieveLatest(filename)
    if issue > l:
        f = open(filename, 'w')
        f.write(issue)
        f.close()

def RetrieveLatest(filename):
    f = open(filename)
    for word in f:
        return word
