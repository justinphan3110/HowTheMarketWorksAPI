# HowTheMarketWorksAPI

The API for the Stock Simulator Game https://HowTheMarketworks.com. My attempt to analyze and doing some basic trading algorithm through this API and stock data crawl by Python Scrapy

There will be 2 main section for this project: [Scrapy](#Scrapy) and [Main API](#API)

## Scrapy
This is the document to set up the Scrapy Spider to crawl stock data from [Yahoo Finance](https://finance.yahoo.com/). 
There will be 2 set up environment Step: Set up the [database](#Install and set up InfluxDB) and [Python Scrapy](#Install and Set up Scrapy).

### Install and set up InfluxDB
In this project, I will use [InfluxDB](https://www.influxdata.com/), an open source time series database

Add InfluxData repository
    
    wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
    source /etc/lsb-release
    echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee               /etc/apt/sources.list.d/influxdb.list
    sudo apt-get update && sudo apt-get install influxdb
    sudo service influxdb start
    
Calling influx to check

![image](https://user-images.githubusercontent.com/44376091/62831159-e5c1eb80-bc44-11e9-9720-1aae70912d33.png)

    


### Install and Set up Scrapy
    pip install scrapy 
    scrapy startproject stock

After these two command, the folder will look something like this

![image](https://user-images.githubusercontent.com/44376091/62830812-2d457900-bc3f-11e9-9194-798dbb0f7890.png)

The main file where will working with is stocks_spider.py.

![image](https://user-images.githubusercontent.com/44376091/62830828-73024180-bc3f-11e9-86ce-2b4a4c54ff7a.png)
   #### :fast_forward:sef.companyList: The list of company we will get stock data from, you can change this with an import        from csv file
  #### :fast_forward:sef.name: Name of the spider
  #### :fast_forward:sef.start_url: The link our spider will start with and link with every company's page for each crawl
  #### :fast_forward:sef.parse(): The main function will be call


With this spider, we will get the price and growth value of the stock from the HTML tags from [Yahoo Finance](https://finance.yahoo.com/). This is an example with [GOOGL](https://finance.yahoo.com/quote/GOOGL/). 

  ![image](https://user-images.githubusercontent.com/44376091/62830873-223f1880-bc40-11e9-88d8-609f706387b3.png)

the XPATH of the growth and price value should be 
      
   ![image](https://user-images.githubusercontent.com/44376091/62830884-7649fd00-bc40-11e9-8658-601f97866039.png)
   
You can easily get the value of these XPATH through some Chrome extension like [XPATH Helper](https://chrome.google.com/webstore/detail/xpath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl?hl=en)

After getting the data of each companies succesfully, we can easily write it in the databases we want, in this example I used InfluxDB

![image](https://user-images.githubusercontent.com/44376091/62830902-de98de80-bc40-11e9-80ef-b1ad686600e3.png)

### Run Scrapy with Crontab
Now you can easily run scrapy with 
      
      scrapy crawl stock
      
The result can be clearly seen, our spiders will run through our companyList and extract stock price from the given XPATH

![image](https://user-images.githubusercontent.com/44376091/62830935-5830cc80-bc41-11e9-9374-e84a908afb5d.png)
      
The data will be written in my InfluxDB

![image](https://user-images.githubusercontent.com/44376091/62830978-08063a00-bc42-11e9-94bc-208639976d00.png)

#### Using Crontab
Now we can employ Crontab to get our scrapy spider run every 1 minute, which close to the time Yahoo Finance updates the stock value

    crontab -e
and insert a line like the picture below with your own file path

![image](https://user-images.githubusercontent.com/44376091/62830994-7ba84700-bc42-11e9-8b11-cced89a4da97.png)

Now the stock values will be update every 1min, after a while you can check the database again

![image](https://user-images.githubusercontent.com/44376091/62831016-c1fda600-bc42-11e9-8e4b-31f54fb76aa3.png)






## API
