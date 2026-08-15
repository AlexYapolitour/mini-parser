import requests
import fake_useragent
from bs4 import BeautifulSoup

user = fake_useragent.UserAgent().random
header = {'User-Agent': user}



link = 'https://browser-info.ru/'
reponce = requests.get(link, headers=header).text
soup = BeautifulSoup(reponce, 'lxml')
block = soup.find('div', id='tool_padding')

check_js = block.find('div', id='javascript_check')
status_js = check_js.find_all('span')[1].text
result_js = f'javascript: {status_js}'

check_flesh = block.find('div', id='flash_version')
status_flash = check_flesh.find_all('span')[1].text
result_flash = f'flash: {status_flash}'

check_agent = block.find('div', id='user_agent').text

print(result_js)
print(result_flash)
print(check_agent)