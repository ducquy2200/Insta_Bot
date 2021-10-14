from selenium import webdriver
from time import sleep
from account import username
from account import password

class InstaBot:
    def __init__(self, username, pw):
        #open window
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        #fill in user info
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(6)
        #extra
        if(self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")):
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            sleep(2)
        if(self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")):
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            sleep(2)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/section/main/section/div[3]/div[1]/div/div/div[1]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        """sleep(2)
        sugs = self.driver.find_element_by_xpath(
            '//h4[contains(text(), Suggestions)]')
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)"""
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;""", scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()
        return names


def main():
    UN = username
    PW = password

    account = InstaBot(UN, PW)
    account.get_unfollowers()


if __name__ == "__main__":
    main()
