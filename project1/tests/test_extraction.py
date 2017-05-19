import urllib.request


urls=['http://thelatinlibrary.com/avianus.html','http://www.thelatinlibrary.com/greg.html','http://www.thelatinlibrary.com/minucius.html',
        'http://www.thelatinlibrary.com/williamapulia.html','http://www.thelatinlibrary.com/poggio.html','http://www.thelatinlibrary.com/priapea.html',
        'http://www.thelatinlibrary.com/arnulf.html'] 


 
def get_url_info(url):
    d = urllib.request.urlopen(url)
    meta=d.info()
    return int(meta.get_all("Content-Length")[0])
    

    
def Length_text(url):
    d =urllib.request.urlopen(url)
    text=d.read()
    return len(text)
    
    
   
    

def test_extraction():
    info_lenght=[]
    returned_length=[]

    for url in urls:
        info_lenght.append(get_url_info(url))
        
    for url in urls:
        returned_length.append(Length_text(url)) 
    
    assert info_lenght==returned_length


    