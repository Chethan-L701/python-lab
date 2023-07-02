import requests
from bs4 import BeautifulSoup
import os


def webscr(url):
    print("Fetching data from " + url)
    r = requests.get(url)
    if r.status_code == 200:
        print("Success!!")
        soup = BeautifulSoup(r.content, 'lxml')
        return soup
    else:
        print("Failed to fetch data : {}".format(r.status_code))
        return None


def download(soup):
    img_url = "https:" + soup.find('div', {'id': 'comic'}).find('img')['src']
    print("Trying to download {}...".format(img_url))
    os.makedirs("./webscr", exist_ok=True)
    filename = "./webscr/" + img_url.split("/")[-1]
    with open(filename, 'wb') as f:
        f.write(requests.get(img_url).content)
    print("Downloaded into {}".format(filename))


url = "https://www.xkcd.com/"
print("Enter your choice : \n1.Specific Comic\n2.Range of Comic")
choice = int(input())
if choice == 1:
    id = int(input("Enter Comic ID : "))
    soup = webscr(url + str(id))
    if soup is not None:
        download(soup)
elif choice == 2:
    start = int(input("Enter Start ID : "))
    end = int(input("Enter End ID : "))
    for i in range(start, end + 1):
        soup = webscr(url + str(i))
        if soup is not None:
            download(soup)
