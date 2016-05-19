from selenium import webdriver
import random
import tweepy

#twitter stuff
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

# opens webclinet
driver = webdriver.Firefox()
driver.get('http://sebpearce.com/bullshit/')

# clicks ionize button
ionize = driver.find_element_by_xpath('//div[@class="topbar"]/button[@class]')
ionize.click()

#gets new age bullshit
phrases = []
phrases.append(driver.find_element_by_xpath('//div[@class="master"]/h1[@id="main-heading"]').text)
phrases.append(driver.find_element_by_xpath('//div[@class="master"]/h2[@id="sub-heading"]').text)
phrases.append(driver.find_element_by_xpath('//div[@class="master"]/h3[@id="third-heading"]').text)
phrases.append(driver.find_element_by_xpath('//div[@class="master"]/p[1]').text)
phrases.append(driver.find_element_by_xpath('//div[@class="master"]/p[2]').text)
phrases.append(driver.find_element_by_xpath('//div[@class="master"]/p[3]').text)
phrases.append(driver.find_element_by_xpath('//div[@class="master"]/p[4]').text)
phrases.append(driver.find_element_by_xpath('//div[@class="master"]/blockquote[@id="quote"]').text)

#closes driver
driver.close()

#removes phrases greater than 140
for p in phrases:
	if len(p) > 140:
		phrases.remove(p)


# accesses twitter
cfg = { 
"consumer_key"        : "",
"consumer_secret"     : "",
"access_token"        : "",
"access_token_secret" : "" 
}

api = get_api(cfg)

#writes tweet
tweet = phrases[random.randint(0, len(phrases) - 1)]
status = api.update_status(status=tweet) 