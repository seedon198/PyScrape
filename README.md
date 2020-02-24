# PyScrape

PyScrape is a web scraper written in python3 using beautiful soup 4 library, PyScrape takes one input i.e. sku id from a known website and will start to scrape and organize data on a csv file. also it downloads product images and stores it in their respective folders. the code might be buggy as i built this for one time job and have no plans to maintain it.

#### Installation
Clone the repository:
```sh
$ git clone https://github.com/seedon198/pyscrape.git
```
install the modules :
```sh
$ pip3 install requests bs4
```
currently the source is adafruit.com modify the code to work with other sites

```sh
$ python3 pyscrape.py
```

#### Usage 
[![asciicast](https://asciinema.org/a/v0tspjZLdJiNFmiJTh2sdPSz4.svg)](https://asciinema.org/a/v0tspjZLdJiNFmiJTh2sdPSz4)

#### Licence
Feel free to use this code :)
