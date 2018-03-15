import requests
from pyquery import PyQuery as pq
from pyh import *
from EmailBox import EmailBox
url="https://www.scientificamerican.com/podcast/60-second-science/"
def CurrentUrlParser(index_page_url):
    index_page_text=requests.get(index_page_url).text
    index_page_dom=pq(index_page_text)
    # "t_feature-title podcasts-header__title" are the two class label for
    # the current url
    current_url=index_page_dom(".podcasts-header__title").children().attr("href")
    return current_url
def CurrentPageGeter(current_page_url):
    curren_page_text = requests.get(current_page_url).text
    curren_page_dom = pq(curren_page_text)
    title = curren_page_dom(".podcasts-header__title")
    transcript = curren_page_dom(".transcript__inner")
    return (title,transcript)
def DomGenerator(title,transcript):
    page=PyH(title.text()).toString()
    page_dom=pq(page)
    page_dom("body").append(title)
    page_dom("body").append(transcript)
    page_dom("h3").attr("align", "center")
    return page_dom
def SendToKindle():
    (title, transcript) = CurrentPageGeter(CurrentUrlParser(url))
    eb=EmailBox()
    eb.add_attachment(title.text(),str(DomGenerator(title, transcript)))
    eb.send_email()
if __name__=="__main__":
    (title, transcript) = CurrentPageGeter(CurrentUrlParser(url))
    print(str(DomGenerator(title, transcript)))