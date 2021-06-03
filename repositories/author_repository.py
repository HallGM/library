from db.run_sql import run_sql 
from models.author import Author


def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES(%s, %s) RETURNING * "
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id

def select_all():
    authors = []
    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['first_name'], row['last_name'], row['id'])
        authors.append(author)

    return authors
    
def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)

    if len(results) > 0 :
        result = results[0]
        first_name = result['first_name']
        last_name = result['last_name']
        id = result['id']  
        author = Author(first_name,last_name,id)
        
    return author   
    


def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)
