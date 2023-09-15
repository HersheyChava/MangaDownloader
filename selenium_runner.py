from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

path_to_adblock = r'/Users/hershey/Documents/python/5.3.3_0'

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('load-extension=' + path_to_adblock)
driver = webdriver.Chrome(options=chrome_options)
driver.create_options()
driver.get("https://kissmanga.org")

def search_manga(manga):

    searchBox = driver.find_element(By.CSS_SELECTOR, '[name="q"]')

    searchBox.send_keys(manga)

    searchButton = driver.find_element(By.XPATH, '//*[text()="SEARCH"]')

    searchButton.click()

    fullList = driver.find_element(By.CSS_SELECTOR, '[class="listing full"]').find_elements(By.CSS_SELECTOR, '[class="item_movies_link"]')


    if len(fullList) < 5:
        rangeLength = len(fullList)
    else:
        rangeLength = 5

    firstFive =[[],[]]

    for x in range(rangeLength):
        firstFive[0].append(fullList[x])
        firstFive[1].append(fullList[x].text)
        
    return firstFive


def get_sources(firstFive, selected):

    print(selected[0])
    print(firstFive)

    firstFive[0][selected[0]].click()

    driver.implicitly_wait(20)

    allChaptersDrivers = driver.find_element(By.CSS_SELECTOR, '[class="barContent episodeList full"]').find_elements(By.TAG_NAME, 'a')

    imageSources = []

    
    for i in range(len(allChaptersDrivers)):

        allChaptersDrivers = driver.find_element(By.CSS_SELECTOR, '[class="barContent episodeList full"]').find_elements(By.TAG_NAME, 'a')

        allChaptersDrivers.reverse()

        allChaptersDrivers[i].click()

        print('chapter ' + str(i+1) + ' being downloaded')

        allImages = driver.find_element(By.ID, 'centerDivVideo').find_elements(By.TAG_NAME, 'img')

        for images in allImages:
            imageSources.append(images.get_attribute("src"))

        driver.back()
        driver.back()

        driver.implicitly_wait(20)


    driver.quit()
    return imageSources