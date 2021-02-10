import bs4
import requests

url = 'http://www.jadwalsholat.pkpu.or.id/?id=145'
contents = requests.get(url)

# Mengolah data melalui bs4
response = bs4.BeautifulSoup(contents.text, "html.parser")

data = response.find_all('tr', 'table_highlight')
# var data akan di bungkus(wrap) dgn tipe data array/list,
# jadi untuk mengurangi masalah kedepannya kita mengambil element nya dan membuat tipe data baru
data = data[0]

sholat = {}
i = 0
for d in data:
    if i == 1:
        sholat['subuh'] = d.get_text()
    elif i == 2:
        sholat['duhur'] = d.get_text()
    elif i == 3:
        sholat['asar'] = d.get_text()
    elif i == 4:
        sholat['magrib'] = d.get_text()
    elif i == 5:
        sholat['isya'] = d.get_text()
    i += 1

print(sholat)
print(f"\nSholat Magrib : {sholat['magrib']}")
