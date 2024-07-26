import requests
from bs4 import BeautifulSoup
import time

def get_articles(url, target_date):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = []

        for div in soup.find_all('div', class_='r-ent'):
            date = div.find('div', class_='date').text.strip()
            
            if date == target_date:
                try:
                    a_tag = div.find('div', class_='title').find('a')
                    title = a_tag.text.strip()
                    link = 'https://www.ptt.cc' + a_tag['href']
                    articles.append({'title': title, 'link': link})
                except AttributeError:
                    articles.append({'title': '已被刪除', 'link': ''})

        # 找到 "上頁" 按鈕的鏈接
        prev_page_link = soup.find('div', class_='btn-group-paging').find_all('a')[1]['href']
        
        return articles, 'https://www.ptt.cc' + prev_page_link
    except requests.RequestException as e:
        print(f"爬取 {url} 時發生錯誤: {e}")
        return [], None

def scrape_nba_board(target_date, max_pages=200):
    url = 'https://www.ptt.cc/bbs/NBA/index.html'
    all_articles = []
    page_count = 0
    found_target_date = False

    while page_count < max_pages:
        print(f"正在爬取頁面：{url}")
        articles, next_url = get_articles(url, target_date)
        all_articles.extend(articles)
        
        print(f"在頁面 {page_count + 1} 找到 {len(articles)} 篇 {target_date} 的文章")
        
        if articles:
            found_target_date = True
        elif found_target_date:
            # 如果已經找到目標日期的文章，且當前頁面沒有文章，則停止爬取
            print(f"沒有找到更多 {target_date} 的文章，停止爬取")
            break
        
        if not next_url:
            print("沒有更多頁面，停止爬取")
            break
        
        url = next_url
        page_count += 1
        

    return all_articles

# 使用函數
target_date = '5/20'  # 設置目標日期
articles = scrape_nba_board(target_date)

# 將結果寫入文件
with open('nba_articles_flexible.txt', 'w', encoding='utf-8') as file:
    for article in articles:
        file.write(f"{article['title']}\n{article['link']}\n\n")

print(f"共找到 {len(articles)} 篇 {target_date} 的文章，已保存到 nba_articles_flexible.txt")