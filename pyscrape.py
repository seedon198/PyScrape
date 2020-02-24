from bs4 import BeautifulSoup
import requests
import os

url = "https://www.adafruit.com/product/"
sku = 2010

while True:
    sku += 1
    pdid = input("code: ")
    response = requests.get(url + pdid)
    soup = BeautifulSoup(response.content, "html.parser")
    name = soup.find('h1', attrs={'class': 'product-name-large'}).text.strip()
    print("Product Name: " + name + "\n")
    price = soup.find('meta', attrs={'itemprop': 'priceCurrency'}).text.strip()
    print("Product Price: $ " + price + "\n")
    ddata = soup.find('div', attrs={'id': 'description'}).text.strip()
    iprice = price.replace("$", "")
    rprice = (float(iprice) * 75) * 1.3
    print("Sales Price: INR " + str(rprice) + "\n")
    techdetails = soup.find('div', attrs={'id': 'technical-details'}).text.strip()
    procdat = techdetails.split("Weight: ")
    weight = procdat[1].split("g")
    dimension = procdat[0].replace(" x ", "").split("mm")
    print("Dimensions : " + dimension[0] + "mm x " + dimension[1] + "mm x " + dimension[2] + "mm x " + "\n")
    print("Weight : " + weight[0] + "\n")

    # Make Product Directory
    cwd = os.getcwd()
    dir = os.path.join(cwd, "images", pdid)
    if not os.path.exists(dir):
        os.mkdir(dir)
        print("Created Image Directory : " + pdid + "\n")
    os.chdir(dir)

    for i in range(0, 9):
        iurl = "https://cdn-shop.adafruit.com/1200x900/" + pdid + "-0" + str(i) + ".jpg"
        iresponse = requests.get(iurl, stream=True)
        with open(pdid + "-0" + str(i) + ".jpg", 'wb') as file:
            file.write(iresponse.content)
        print("Downloaded file: " + pdid + "-0" + str(i) + ".jpg\n")

    os.chdir(cwd)

    delim = ","
    csvdata = name + delim + name.lower().replace(" ", "_") + delim + "publish" + delim + str(sku) + delim + "no" + \
              delim + "no" + delim + "visible" + delim + "10" + delim + "instock" + delim +"yes" + delim + "yes" + \
              delim + str(rprice) + delim + delim + weight[0] + delim + dimension[0] + delim + dimension[1] + delim + \
              dimension[2] + delim + "taxable" + delim + "standard" + delim + delim + delim + delim + delim + \
              delim + delim + delim + "\n"


    with open('file.csv', 'a') as fd:
        fd.write(csvdata)
    print("Appended " + pdid + " Data to csv file... \n Processing Complete!\n\n")
