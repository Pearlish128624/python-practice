from urllib.parse import urlparse, parse_qs, unquote 
# 從 urllib.parse 模組中導入了三個函數 
def google_search_query(url):
    # 解析 URL
    parsed_url = urlparse(url) 
    # 解析查詢參數
    query_params = parse_qs(parsed_url.query)
    # 獲取 'q' 參數的值 q parameter: Google uses q to store the search query in its URLs.
    search_query = query_params.get("q", [None])[0]
        # dic.get("key",default)[第幾個值]
    if search_query: #if 上面那個查出是有效值
        # 解碼 URL 編碼的字符 
        search_query = unquote(search_query.replace('+', ' '))
        #unquote 函數可將其他可能的編碼字符（例如 %20）轉換回原始字符
        # replace + 變成空格
    return search_query
url = input("Please input your google url ")
search_query = google_search_query(url)
print("Search query:", search_query) 
