from bs4 import BeautifulSoup
import docx
import urllib.request
import os

with open("source.txt", 'rb') as fp:
    soup = BeautifulSoup(fp, "html.parser")
    title=soup.select('h1[class*="video-name"]')[0].get_text()
    # Create an instance of a word document
    doc = docx.Document()
    
    # Add a Title to the document
    doc.add_heading(title, 0)
    
    for img_tag in soup.find_all('img', {'alt': 'Video thumbnail'}):
        # download image from img url, save to `video.png`
        urllib.request.urlretrieve(img_tag['src'], 'video.png')
        doc.add_picture('video.png')

    # Now save the document to a location
    doc.save('export.docx')
    os.remove('video.png')