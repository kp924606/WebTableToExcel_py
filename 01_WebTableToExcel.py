
# Please install PKG as below.
# pip install requests pandas beautifulsoup4 lxml
# pip install openpyxl
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 網頁 URL
url = 'https://histock.tw/stock/gift.aspx'

# 發送請求取得 HTML
response = requests.get(url)
response.encoding = 'utf-8'  # 或視網頁編碼調整（如 big5、utf-8）

# 用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 抓指定 id 的 table
table = soup.find('table', {'id': 'CPHB1_gv'})

#CPHB1_gv
#CPHB1_gvOld

# 轉成 pandas DataFrame（注意這裡 str(table)）
df = pd.read_html(str(table))[0]

# 另存成 Excel 檔
df.to_excel('table_output.xlsx', index=False)

print("已完成轉換為 Excel！")
