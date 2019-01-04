#file-name: pdf_download.py
__author__ = 'rxread'
import requests
from bs4 import BeautifulSoup
import html5lib


def download_file(url, index):
	local_filename = index+"-"+url.split('/')[-1]
    # NOTE the stream=True parameter
    #r = requests.get(url, stream=True)
	r = requests.get(url)
	with open(local_filename, "wb") as f:
		f.write(r.content)
	return local_filename
          # for chunk in r.iter_content(chunk_size=1024):
              # if chunk: # filter out keep-alive new chunks
                  # f.write(chunk)
                  # f.flush()
      # return local_filename

  #http://ww0.java4.datastructures.net/handouts/
root_link="https://scholar.google.com.hk/scholar?hl=zh-TW&as_sdt=0%2C5&q=news+predict+stock+market&btnG="
r=requests.get(root_link)
if r.status_code==200:
	soup=BeautifulSoup(r.text, "html5lib")
      # print soup.prettify()
	index=1
	for link in soup.find_all('a'):
		new_link=link.get('href')
		if new_link.endswith(".pdf"):
			#urlw = "https://www.researchgate.net/profile/Rob_Schumaker/publication/220515646_Textual_analysis_of_stock_market_prediction_using_breaking_financial_news_The_AZFin_text_system/links/56d49bd208aefd177b0f5c73.pdf"  
			file_path=download_file(new_link,str(index))
			print ("downloading:"+new_link)
			index+=1
			  