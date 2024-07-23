from urllib.parse import urlparse, parse_qs, unquote 
# 從 urllib.parse 模組中導入了三個函數 
def output_search_query(url):
    # 解析 URL
    parsed_url = urlparse(url) 
        #urlparse 是可以把url拆解出來的 以https://www.youtube.com/results?search_query=LiSA-ADAMAS為例子
        # 會將 URL 分解為：協議（scheme）：https /
        # 網域（netloc）：www.youtube.com 
        # 路徑（path）：/results 
        # 查詢（query）：search_query=LiSA-ADAMAS
    
    # 解析查詢參數
    query_params = parse_qs(parsed_url.query)
        # 由於拆解出來的字串是沒有意義的，parse_qs這個動作是進行字典建立
        # 也就是從分解出來的上面那一大串中，挑選出query中建立: {'search_query': ['LiSA-ADAMAS']} 

    # 獲取 'search_query' 參數的值
    search_query = query_params.get('search_query', [None])[0]
        # 從已經建立好的字典 query_params 中詢問 search_query的第一個[0]value是什麼
        # query_params 是一個字典：它的鍵是查詢參數名，值是包含所有對應值的列表，所以需要指定是列表中的[0]
        # [None]作為默認值的作用是確保 search_query 在查詢參數不存在時，仍然是一個包含 [None] 的列表。
        ## 注意 ## None 跟 [None] 在列表內所代表的意思不同
        # 這使得 search_query 始終是列表（即使是空列表），可以安全地使用 [0] 來獲取第一個值，避免在處理空列表時出現錯誤。
        # dic.get("key",default)[第幾個值]
    if search_query: #if 上面那個查出是有效值
        # 解碼 URL 編碼的字符 
         search_query = unquote(search_query.replace('+', ' '))
        #unquote 函數可將其他可能的編碼字符（例如 %20）轉換回原始字符
        # replace + 變成空格
    return search_query

print(output_search_query("https://www.youtube.com/results?search_query=python"))  