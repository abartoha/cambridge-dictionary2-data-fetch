from bs4 import BeautifulSoup
from requests import get

#headers : for specifying a user agent so it doesn't seem as suspicious to the servers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

#list of letters
letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

#url : to be for-looped
url ="https://dictionary.cambridge.org/browse/learner-english/"+letters[0]+"/"

#request
req = get(url, headers=headers)
soup = BeautifulSoup(req.content,'html.parser')

#all the possible paginations
pagination_1 = [i['href'] for i in soup.find_all("a", attrs={"class":"dil tcbd"})]

#request
req = get(pagination_1[0], headers=headers)
soup = BeautifulSoup(req.content,'html.parser')

#all the entries
tc_bd = [i for i in soup.find_all("a", attrs={'class':'tc-bd'}) if i.text != "index"]
neo_list = []
for i in tc_bd:
    idiom = i.find('span', attrs={'class':'pos'})
    if idiom != None:
        neo_list.append(i['href'])


neo_url = "https://dictionary.cambridge.org"+neo_list[0]

req = get(neo_url)
soup = BeautifulSoup(req.content,'html.parser')

meanings = [] #(meaning,pos)
dictionary = {} #word, meanings_list

#entry-body
entry_body = soup.find("div", attrs={'class':'entry-body'})

#word
word = soup.find('span', attrs={'class':'hw dhw'})
print(word)

