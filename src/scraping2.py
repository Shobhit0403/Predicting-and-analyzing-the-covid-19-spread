# -*- coding: utf-8 -*-
"""Scraping2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yByaoZkPFokW6KdAPg-2dsEcxblcpI7I
"""

pip install html-table-parser-python3

import urllib.request
from html_table_parser import HTMLTableParser
import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np

from bs4 import BeautifulSoup
import requests

import csv

url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2020&Month=2#"
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]
for i in range(29):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(29):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)

df_temp=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df_temp['date'] = pd.date_range(start='2/1/2020', periods=len(df_temp), freq='D')

print(df_temp)

#March2020
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2020&Month=3"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]
for i in range(31):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(31):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)

df=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df['date'] = pd.date_range(start='3/1/2020', periods=len(df), freq='D')
df_temp=df_temp.append(df)

#April 2020"
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2020&Month=4"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]

for i in range(30):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(30):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)



df=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df['date'] = pd.date_range(start='4/1/2020', periods=len(df), freq='D')


df_temp=df_temp.append(df)

#May2020
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2020&Month=5"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]
for i in range(31):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(31):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)

df=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df['date'] = pd.date_range(start='5/1/2020', periods=len(df), freq='D')
df_temp=df_temp.append(df)

#June 2020
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2020&Month=6"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]

for i in range(30):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(30):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)


df=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df['date'] = pd.date_range(start='6/1/2020', periods=len(df), freq='D')
df_temp=df_temp.append(df)

#July2020
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2020&Month=7"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]
for i in range(31):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(31):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)

df=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df['date'] = pd.date_range(start='7/1/2020', periods=len(df), freq='D')
df_temp=df_temp.append(df)

#AUG2020
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2020&Month=8"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]
for i in range(31):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(31):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)

df=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df['date'] = pd.date_range(start='8/1/2020', periods=len(df), freq='D')
df_temp=df_temp.append(df)

df_temp

#Sept 2020
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2020&Month=9"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]

for i in range(30):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(30):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)


df=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df['date'] = pd.date_range(start='9/1/2020', periods=len(df), freq='D')
df_temp=df_temp.append(df)

#Oct2020
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2020&Month=10"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]
for i in range(31):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(31):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)

df=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df['date'] = pd.date_range(start='10/1/2020', periods=len(df), freq='D')
df_temp=df_temp.append(df)

#Nov 2020
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2020&Month=11"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]

for i in range(30):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(30):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)


df=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df['date'] = pd.date_range(start='11/1/2020', periods=len(df), freq='D')
df_temp=df_temp.append(df)

#Dec2020
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2020&Month=12"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]
for i in range(31):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(31):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)

df=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df['date'] = pd.date_range(start='12/1/2020', periods=len(df), freq='D')
df_temp=df_temp.append(df)

#JAN2021
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2021&Month=1#"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]
for i in range(31):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(31):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)

df=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df['date'] = pd.date_range(start='1/1/2021', periods=len(df), freq='D')
df_temp=df_temp.append(df)

#FEB2021
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2021&Month=2"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]
for i in range(28):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(28):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)

df=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df['date'] = pd.date_range(start='1/2/2021', periods=len(df), freq='D')
df_temp=df_temp.append(df)

#March2021
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2021&Month=3"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]
for i in range(31):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(31):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)

df=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df['date'] = pd.date_range(start='3/1/2021', periods=len(df), freq='D')
df_temp=df_temp.append(df)

#April2021
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2013-02-13%7C2021-04-22&dlyRange=2013-02-14%7C2021-04-21&mlyRange=%7C&StationID=51157&Prov=QC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2020&EndYear=2021&selRowPerPage=100&Line=131&lstProvince=QC&timeframe=2&Day=22&Year=2021&Month=4"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-striped table-hover align-cells-right data-table"})
gdp_table_data = gdp_table.tbody.find_all("tr") 

mean_temp=[]
r=[]
for i in range(21):
  s=gdp_table_data[i].find_all("td")
  r.append(s[2])

for i in range(21):
  k=str(r[i])
  s=''
  for i in range(len(k)):
    if(k[i]=='>'):
      i=i+1
      while(k[i]!='<'):
        s=s+k[i]
        i=i+1
      break
  mean_temp.append(s)

df=pd.DataFrame(mean_temp, columns =['Mean Temp'])
df['date'] = pd.date_range(start='4/1/2021', periods=len(df), freq='D')
df_temp=df_temp.append(df)

df_temp

df_temp.to_csv(r'temp_Quebec.csv')

