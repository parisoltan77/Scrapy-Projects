#programmer : Parinaz Soltanzadeh
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
#import os

def Search():
    search = input("Search for:")
    params = {"q": search}
    """
    #agar bekhaim be surat joda directory besazim va be esm chizi ke search krdim bashe az in dasturat estefadeh mikonim.
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):#agar directory ba in esm vojud nadashte bashe uno misazeh
        os.makedirs(dir_name)
    #agar az in dasturat estefadeh krdim khat 31 bejaye "scraped_image az dir_name estefadeh shavad
    """
    r = requests.get("http://www.bing.com/images/search", params=params) #example : https://www.bing.com/images/search?q=pizza

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])#link address
            print("Link address: ", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1] #esm ax dar title mirize
            try:
                img = Image.open(BytesIO(img_obj.content))#mohtavaye object ke azx hast ra dar img mirizeh
                img.save("./scraped_images/" + title, img.format) # save kardan ax dar sirectory mored nazar be hamrah esm va format
            except:
                print("Could not save image!!!")
        except:
            print("Could not request image!!!")

    Search()

Search()