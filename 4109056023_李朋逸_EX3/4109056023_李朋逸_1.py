import requests
from bs4 import BeautifulSoup

url = 'https://s5.sir.sportradar.com/taiwansportslottery/zht/2/season/94573'
response = requests.get(url)
content = response.text

# 打印 HTML 內容，檢查是否能夠獲取到網頁內容
print(content)

sportSoup = BeautifulSoup(content, 'html.parser')
table = sportSoup.select_one('.panel-body .table')

if table:
    headings = [th.text.strip() for th in table.select('thead tr th')]
    rows = [[td.text.strip() for td in tr.find_all('td')] for tr in table.select('tbody tr')]

    # cut the team name in half
    for row in rows:
        if len(row) > 1:  # 確保 row[1] 存在
            row[1] = row[1][:len(row[1])//2]

    with open('data_1.txt', 'w', encoding='utf-8') as file:
        file.write(sportSoup.prettify())

    with open('table.txt', 'w', encoding='utf-8') as file:
        file.write(' '.join(headings) + ' \n')
        for row in rows:
            file.write(' '.join(row) + ' \n')

else:
    print("未能找到表格。請檢查選擇器是否正確。")
