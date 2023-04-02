# python3

class Query:
    def __init__(self, query_type, number=None, name=None):
        self.type = query_type
        self.number = number
        self.name = name
            

def read_queries():
    n = int(input())
    queries=[]
    for i in range (n):
        query=input().split()
        if query[0] == 'add':
            queries.append(Query('add',query[1],query[2]))
        elif query[0] == 'del':
            queries.append(Query('del',query[1]))
        else: 
            queries.append(Query('find',query[1]))    
    return queries

def write_responses(result):
    print(' '.join(result))

def process_queries(queries):
    result = []
    contacts={}
    for query in queries:
        if query.type == 'add':
            contacts[query.number]=query.name
        elif query.type == 'del':
            if query.number in contacts:
                del contacts[query.number]
        elif query.type == 'find':   
            if query.number in contacts:
                result.append(contacts[query.number])
            else:
                result.append('not found')    
    return result

if __name__ == '__main__':
    queries=read_queries()
    results=process_queries(queries)
    for result in results:
        print(result)

