from bs4 import BeautifulSoup

def extractDateInformation(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    sectionDetail = soup.find("div", class_= "guia-detalle")
    return str(sectionDetail.prettify())
