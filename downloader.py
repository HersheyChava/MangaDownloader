from PIL import Image
import requests

def exists(path):
   return requests.head(path).status_code == requests.codes.ok

def download_it(filenames):

   allSources = filenames

   pages = []
   counter = 1
   for source in allSources:
      if(exists(source)):
         pages.append(Image.open(requests.get(source, stream = True).raw))
         print(str(counter) + "/" + str(len(allSources)) + " images completed")
         counter+=1
      else:
         print(source + ' is down')

   pages[0].save('output.pdf', "PDF" ,resolution=100.0, save_all=True, append_images=pages[1:])

