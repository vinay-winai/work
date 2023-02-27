from django.http import JsonResponse
from . import tasks
import csv
from celery.result import AsyncResult

def upload_file(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        #file read
        data_arr=[]
        csv_reader = csv.DictReader(csv_file.read().decode('utf-8').splitlines())
        for row in csv_reader:
            data_arr.append(row)
        result = tasks.insert_to_db.delay(data_arr)
        return JsonResponse({'task' : result.id})
    return JsonResponse({'error' : "invalid method"})
    

def check_task_status(request):
    if request.method == 'POST':
        id = request.POST.get('id')   
        result = AsyncResult(id)
        if result.ready():
            # Get the result value
            result_value = result.get()
            return JsonResponse({'status' : result_value})
        else:
            return JsonResponse({'status' : "Task is not yet complete"})
    return JsonResponse({'error' : "invalid method"})
