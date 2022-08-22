import requests
from bs4 import BeautifulSoup
from csv import writer
import numpy as np

headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

i = 1

urls = [('https://www.bible.com/bible/1423/GEN.'+ str(i) +'.LBR')]

for i in range(50):

    for url in urls:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        info = soup.find_all('div', {'class': 'yv-bible-text'})
        
        #Creating new file to store data
        with open('bible_Scrap.csv', 'w', encoding='utf8', newline='') as f:
            thewriter = writer(f)
            header = ['title', 'heading', 'content']
            thewriter.writerow(header)

            for item in info:
                    #content to be located
                    title = item.find('h1').text.replace('\n', '')
                    heading = item.find('span', {'class': 'heading'}).text.replace('\n', '')
                    content = item.find('div', {'class': 'version vid1423 iso6393lug'}).text.replace('\n', '')
                

                    details =[title, heading, content]
                    
                    
                    thewriter.writerow(details)
                    i = i+1
                    #for variable j
                     j = j+1
