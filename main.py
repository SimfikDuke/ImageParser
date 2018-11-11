from urllib.request import urlopen
import bs4
import re
import os

brands = ['volkswagen', 'mercedes-benz', 'toyota', 'kia', 'vaz_lada', 'bmw', 'skoda', 'ford']
page_limit: int = 20


def parse_auto(brand: str, limit: int):
    images = list()
    try:
        for page in range(1, page_limit+1):
            page = urlopen('https://www.avito.ru/rossiya/avtomobili/' + brand + '?user=1&i=1&p='+str(page))
            soup = bs4.BeautifulSoup(page, features="html.parser")
            image_div_list = soup.find_all('div', 'item-slider-image large-picture')
            for image_use in image_div_list:
                images.append(re.findall(r'(?<=url\(\/\/).*\.jpg', str(image_use))[0])
    except:
        print("Error while parsing")
    name_iterator = 1
    path = os.getcwd()
    try:
        os.mkdir(path + '\\data')
        os.mkdir(path + '\\data\\' + brand)
    except:
        print('This directory is already exist')

    for url in images:
        try:
            img = urlopen('https://' + url).read()
            out = open(path + '\\data\\' + brand + '\\' + str(name_iterator) + '.jpg', 'wb')
            out.write(img)
            out.close()
            print('/data/'+brand+"/"+str(name_iterator)+'.jpg was saved successfully')
            name_iterator += 1
        except:
            print('Error when saving file')


for car in brands:
    parse_auto(car, page_limit)
