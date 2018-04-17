import pytest
import time
from selenium import webdriver

driver = webdriver.Chrome()


def test_open_url():
    url = "https://www.youtube.com/"
    song_name = "Rawayana High"
    search_button_id = "search-icon-legacy"
    song_text = "Rawayana - High feat. Apache (Video Oficial)"
    tittle_container = '//*[@id="container"]/h1/yt-formatted-string'

    driver.get(url)
    driver.find_element_by_id("search").send_keys(song_name)
    driver.find_element_by_id(search_button_id).click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[contains(text(), '" + song_text + "')]").click()
    time.sleep(9)
    assert song_text == driver.find_element_by_xpath(tittle_container).text


def test_close_driver():
    driver.close()
    driver.quit()
