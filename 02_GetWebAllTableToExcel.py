
# Please install PKG as below.
# pip install requests pandas beautifulsoup4 lxml
# pip install openpyxl

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

# 建立 data 資料夾（如果還不存在）
os.makedirs("data", exist_ok=True)

# 產生時間戳記
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# 建立完整路徑的檔名
filename = fr"data/{timestamp}.xlsx"

# 目標網址
url = "https://histock.tw/stock/gift.aspx"

# 擷取網頁 HTML
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# 擷取所有有 id 的 table
tables_with_id = soup.find_all('table', id=True)

# 寫入 Excel，每個 table 一個工作表
with pd.ExcelWriter(filename, engine='openpyxl') as writer:
    for table in tables_with_id:
        table_id = table['id']
        try:
            df = pd.read_html(str(table))[0]
            sheet_name = table_id[:31]
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"✅ 已寫入工作表：{sheet_name}")
        except Exception as e:
            print(f"⚠️ 無法解析 table（id={table_id}）：{e}")

print(f"🎉 完成！Excel 已儲存至：{filename}")
