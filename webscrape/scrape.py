import requests
from bs4 import BeautifulSoup
import json
import re
import os

# List of URLs to scrape
urls = [
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%201&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%202&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%203&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%204&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%205&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%206&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%207&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%208&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%209&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2010&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2011&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2012&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2013&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2014&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2015&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2016&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2017&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2018&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2019&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2020&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2021&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2022&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2023&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2024&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2025&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2026&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2027&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2028&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2029&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2030&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2031&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2032&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2033&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2034&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2035&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2036&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2037&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2038&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2039&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2040&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2041&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2042&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2043&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2044&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2045&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2046&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2047&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2048&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2049&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2050&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2051&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2052&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2053&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2054&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2055&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2056&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2057&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2058&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2059&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2060&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2061&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2062&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2063&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2064&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2065&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2066&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2067&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2068&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2069&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2070&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2071&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2072&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2073&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2074&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2075&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2076&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2077&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2078&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2079&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2080&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2081&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2082&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2083&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2084&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2085&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2086&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2087&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2088&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2089&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2090&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2091&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2092&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2093&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2094&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2095&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2096&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2097&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2098&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%2099&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20100&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20101&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20102&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20103&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20104&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20105&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20106&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20107&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20108&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20109&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20110&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20111&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20112&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20113&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20114&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20115&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20116&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20117&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20118&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20119&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20120&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20121&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20122&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20123&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20124&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20125&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20126&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20127&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20128&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20129&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20130&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20131&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20132&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20133&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20134&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20135&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20136&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20137&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20138&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20139&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20140&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20141&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20142&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20143&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20144&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20145&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20146&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20147&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20148&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20149&version=NRT",
    "https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20150&version=NRT"
    # Add more URLs as needed
]

def parse_verses(verses, chapter_number):
    chapter_data = []
    current_verse = 1
    text_buffer = ""

    for verse in verses:
        numbers = list(map(int, re.findall(r'\d+', verse)))
        if numbers:
            if text_buffer:
                chapter_data.append({
                    "chapter": chapter_number,
                    "verse": current_verse,
                    "text": text_buffer.strip(),
                    "translation_id": "NRT",
                    "book_id": "Ps",
                    "book_name": "Psalms"
                })
                current_verse += 1
            text_buffer = verse.split(str(numbers[0]), 1)[-1].strip()
        else:
            text_buffer += " " + verse

    if text_buffer:
        chapter_data.append({
            "chapter": chapter_number,
            "verse": current_verse,
            "text": text_buffer.strip(),
            "translation_id": "NRT",
            "book_id": "Ps",
            "book_name": "Psalms"
        })

    return chapter_data

def scrape_text_from_url(url):
    verses = []
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        poetry_div = soup.find('div', class_='passage-text')
        if poetry_div:
            spans = poetry_div.find_all('span', class_='text')
            for span in spans:
                text = span.text.strip()
                if text:
                    verses.append(text)
    except Exception as e:
        print(f"Error scraping {url}: {e}")
    
    return verses

# Create 'psalms' directory if it doesn't exist
os.makedirs('psalms', exist_ok=True)

for url in urls:
    # Extract chapter number from the URL using regex
    match = re.search(r'%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20(\d+)', url)
    chapter_number = int(match.group(1)) if match else None
    
    if chapter_number is not None:
        verses = scrape_text_from_url(url)
        chapter_data = parse_verses(verses, chapter_number)
        if chapter_data:
            for entry in chapter_data:
                entry["chapter"] = chapter_number
            with open(f'psalms/Ps-{chapter_number}.json', 'w', encoding='utf-8') as f:
                json.dump(chapter_data, f, ensure_ascii=False, indent=4)
