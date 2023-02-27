from celery import shared_task
from .models import Userlog

# @shared_task
# def file_to_db(csv_file,filename):
#     try:
#         storage = FileSystemStorage()
#         conn = psycopg2.connect(host="localhost", port="5432", dbname="user", user="postgres", password="root")

#         # Open a cursor to perform database operations
#         cur = conn.cursor()
#         with open(csv_file, 'r') as f:
#             cur.copy_from(f, 'user', sep=',')
#         conn.commit()
#     except Exception as e:
#         storage.delete(filename)  
#         return 'failed'
#     storage.delete(filename)   
#     return 'success'

@shared_task
def insert_to_db(data_arr):
    try:
        bulk = []
        for row in data_arr:
            userlog = Userlog(
            id=row['id'],
            name=row['name'],
            ip =row['ip'],
            timestamp =row['timestamp'],
            )
            bulk.append(userlog)
        Userlog.objects.bulk_create(bulk)
    
    except Exception as e:
        return 'failed'
    return 'success'

    