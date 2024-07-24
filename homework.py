#Method1
url="https://www.youtube.com/results?search_query=happy+cat+song"
search = url.replace("https://www.youtube.com/results?search_query=","")
print(search.replace("+"," "))
#Method2
url2="https://www.youtube.com/results?search_query=happy+cat+song"
list2 = url2.partition("search_query=") #將資料list用search_query= 切三段
print(list2[2].replace("+"," ")) #取search_query 後方的資料並將+號取代成空格
#Method for Google
url3="https://www.google.com/search?q=Teams+Microsoft&sca_esv=6a16a772d5a29aa1&rlz=1C1CHBF_enUS849US849&sxsrf=ADLYWIIRGZw8d9wsyxXO_8MxfbVNHeZ85A%3A1721827924531&ei=VAKhZuyYILinvr0Ph560gAU&oq=teams+download&gs_lp=Egxnd3Mtd2l6LXNlcnAiDnRlYW1zIGRvd25sb2FkKgIIBTIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYR0joG1AAWABwAXgBkAEAmAEAoAEAqgEAuAEByAEAmAIBoAISmAMAiAYBkAYKkgcBMaAHAA&sclient=gws-wiz-serp"
list3=url3.partition("search?q=")
search3=list3[2].partition("&")
print(search3[0].replace("+"," "))


