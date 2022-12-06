import wikipedia
query=wikipedia.page(input('search:'))
print(query.summary)