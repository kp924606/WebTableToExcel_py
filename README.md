![](https://img.shields.io/badge/Creater-TCT-FFFF00) ![](https://img.shields.io/badge/development-python-006400) ![](https://img.shields.io/badge/Version-3.10.6-blue) ![](https://img.shields.io/badge/Tool-VSCode-222222)

# WebTableToExcel_py
網頁表格轉Excel

![image](https://github.com/user-attachments/assets/f9d4bf8a-8313-4391-b3d1-7aa5c3a80b79)

![image](https://github.com/user-attachments/assets/1dbade46-c96b-4692-bfc7-4679eaf5c931)

-------

# 1. Package Introduce

## 1-1. requests
從網頁「下載 HTML 原始碼」的工具
- 功能：對網站發送 HTTP 請求，取得網頁內容。

```bash
取得網頁內容再進行分析。
requests.get(url)
```

## 1-2. pandas
資料處理與分析工具，核心是 DataFrame 表格物件
- 功能：讀取、操作、儲存各種表格資料（如 Excel、CSV、HTML 表格等）。

```bash
解析 HTML 表格
pd.read_html()

輸出成 Excel
df.to_excel()
```

## 1-3. beautifulsoup4
解析 HTML 或 XML 的利器，快速找出標籤內容
- 功能：讀取 HTML 結構，找到指定標籤（如 <table>、<div>、id=xxx）。

```bash
找出所有有 id 的表格。
soup.find_all('table', id=True)
```

## 1-4. lxml
超快速的 HTML / XML 解析器（BeautifulSoup 的加速引擎）
- 功能：加快 BeautifulSoup 或 pandas.read_html() 解析 HTML 的速度與穩定性。

```bash
背後會呼叫它來加速解析。
pandas.read_html()
```

## 1-5. openpyxl
處理 Excel（.xlsx）的套件
- 功能：讀寫 .xlsx 格式的 Excel 檔案。
  
```bash
輸出 Excel
pd.ExcelWriter(..., engine='openpyxl')
```

## 1-6 PKG Install：
```bash
pip install
pip requests
pip pandas
pip beautifulsoup4
pip lxml
pip openpyxl
```

## 套件互動關係圖：
```bash
[ requests ] → 下載 HTML
       ↓
[ BeautifulSoup ] → 找出 <table id="xxx">
       ↓
[ pandas.read_html ] + [ lxml ] → 解析成 DataFrame
       ↓
[ openpyxl ] ← pandas.to_excel → 寫入 Excel 檔
```

-------

# 2. py
## 2-1. 03_GetWebAllTableToExcelByUrl.py
輸入要解析的網頁並將表格提取儲存至Excel。

-------

# 3. exe
## 3-1. WebTableToExcel_py\dist\03_GetWebAllTableToExcelByUrl.exe
打包成執行檔，開啟即可使用。

```bash
#打包成 exe 套件
pip install pyinstaller

#--onefile	打包成單一檔案（所有模組都打進去）
#--noconsole	不開啟黑色命令列（適合 GUI 程式）
#pyinstaller --onefile --noconsole webtable_to_excel.py
pyinstaller --onefile 03_GetWebAllTableToExcelByUrl.py
```

![image](https://github.com/user-attachments/assets/a7dac395-eebc-438d-8cb1-29bfeed81298)

![image](https://github.com/user-attachments/assets/7cb0e808-9994-438f-9fec-204435e30ee5)

![image](https://github.com/user-attachments/assets/faadf299-bab6-4a0f-9765-5aa9766b7429)

![image](https://github.com/user-attachments/assets/64c9ee45-4924-4139-ae0d-be7a70fe29c8)

------

## About Me
Thanks & Best Regards !

蔡承廷

​Senior Engineer of Semiconductor Product/Testing & ​Automation

Email: ​​kp924606@gmail.com

LinkedIn:https://www.linkedin.comin/tsai-cheng-ting/
