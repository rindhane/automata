from pdf_link_scraper import url_generator,month_yielder, year_yielder
import requests


for idx,url in enumerate(url_generator()) : 
    r=requests.get(url)
    if r.status_code==requests.codes.ok:
        name=str(year_yielder(idx))+month_yielder(idx)
        file_=open(f'./files/{name}.pdf','wb')
        file_.write(r.content)
        file_.close()
    else :
        print(r.url)

