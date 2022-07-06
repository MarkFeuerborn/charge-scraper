import config
import helpers
import requests
from bs4 import BeautifulSoup

def FindPageCount():
        # Open the first page
    f = requests.get(config.GetIssuePageUrl(1))
    soup = BeautifulSoup(f.text,'lxml')
    
    print("Looking for page count indicators")
    pagesNode = soup.find("div",class_="c-pagination__label")
    
    #print(pagesNode)
    if pagesNode is not None:
        pageCount = pagesNode.text.split(' ')[-1]
        return int(pageCount)

def FindIssues(pageCount, latestIssueNo):
    for page in range(1, pageCount):
               
        print("Opening site on page {}...".format(page))    
        f = requests.get(config.GetIssuePageUrl(page))
        soup = BeautifulSoup(f.text,'lxml')
        
        print("Hunting...")
        for link in soup.find_all('a'):
            url = link.get('href')
            if url is not None:
                if url.endswith('/pdf'):
                    issue = url.split('/')[-2]                                        
                    print("Issue is {}".format(issue))
                    
                    # determine if we found a new one
                    if issue > latestIssueNo:
                        print("New issue found!")
                        DownloadIssue(url)

                        # capture the latest issue no   
                        helpers.WriteLatest(issue, config.LatestFileName)
                    else:
                        print("No new issues :(")
                        return            

def DownloadIssue(url): 
    #pull html info from link
    f = requests.get(config.GetDownloadPageUrl(url), stream=True)
    soup = BeautifulSoup(f.text, 'lxml')
    
    print("Looking for download link")
    for link in soup.find_all('a'):
        downloadUrl = link.get('href')
        if downloadUrl is not None:
            if ".pdf" in downloadUrl:                
                print("Found! {}".format(downloadUrl))
                downloadFile = helpers.DownloadFile(downloadUrl, config.PathToOutput)

                # fire it up to Dropbox
                print("File downloaded to {}".format(downloadFile))

                if config.UploadToDropbox:
                    helpers.CopyToDropbox(config.PathToDropbox, downloadFile)
