'''
chrome class
read information from website 
'''
from bs4 import BeautifulSoup
def chrome(driver):
    if driver == 0:
        print(1)
    else:

        html = driver.page_source
        soup = BeautifulSoup(html,"html.parser")
        info_list = []
        info_list2=[]

        for g in soup.find_all('div',class_='d2l-textblock'):
            info_list.append(g.string)
    
        index = info_list.index("The number of calendars exceeds the maximum. To see more, remove calendars from My Calendars.")
        info_list = info_list[index+1:-1]
        for item in info_list:
            if (item is not None):
                info_list2.append(item)
        driver.quit()
        return info_list2