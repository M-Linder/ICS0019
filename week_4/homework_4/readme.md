# How to activate the Spiders:

## BeautifulSoup Spider
The BeautifulSoup Spider can either be activated through the Pycharm IDE 
by pressing the green arrow in the top right. 
Or otherwise with the following CMD command in the file's directory:

````shell
python .\BeautifulSoupSpider.py
````


## Scrapy Spider
The Scrapy Spider cannot be activated through the IDE. It can only be activated
by running the following CMD command in the file's directory:


````shell
scrapy runspider -O .\output\scrapy.json ScrapySpider.py
````