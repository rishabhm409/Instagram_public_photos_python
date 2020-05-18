from selenium import webdriver
import  time
import urllib.request
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver")
driver.get("url of the public account")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/div[1]/div/button").click()
lst_height=driver.execute_script("document.body.scrollHeight")
i=0
while(i<1):
    i+=1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
posts=[]
links=driver.find_elements_by_tag_name('a')
#print(links)
for link in links:
    post=link.get_attribute("href")
    if ('/p/') in post:
        posts.append(post)
print(posts)
download_url=''
k=0
for post in posts:
    driver.get(post)
    shortcode=driver.current_url.split('/')[-2]
    #print(shortcode)
    type=driver.find_element_by_xpath("//meta[@property='og:type']").get_attribute("content")
    if type=='video':
        download_url=driver.find_element_by_xpath("//meta[@property='og:video']").get_attribute("content")
        #urllib.request.urlretrive(download_url,"{}.mp4".format(shortcode))
    else:
        k+=1
        download_url = driver.find_element_by_xpath("//meta[@property='og:image']").get_attribute("content")
        urllib.request.urlretrieve(download_url, "E:\picss\{}.jpg".format(k))
    #print(download_url)
