from bs4 import BeautifulSoup

json = {}

with open('New Lead .html', 'r') as fin:
    text = fin.read()
    soup = BeautifulSoup(text, 'html.parser')
    
    name = soup.find_all('strong')[1].get_text()
    email = soup.find_all('a')[4].get_text()
    phone = soup.find_all('a')[3].get_text()
    beds = soup.find_all('strong')[5].get_text()
    baths = soup.find_all('strong')[6].get_text()
    address = soup.find_all('strong')[3].get_text()
    
json['name'] = name
json['email'] = email
json['phone'] = phone
json['beds'] = int(beds)
json['baths'] = int(baths)
json['address'] = address.replace(',', '~')

json_text = str(json).replace(',', ',\n').replace('\'', '\"').replace('~', ',').replace('{', '{\n').replace('\n', '\n\t').replace('}', '\n}')

with open('output.json', 'w') as fout:
    fout.write(json_text)

