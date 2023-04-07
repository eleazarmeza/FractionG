from django.shortcuts import render
from frontend.models import Student, Questions
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    return render(request, "frontend/index.html")

def aboutus(request):
    return render(request, "frontend/aboutus.html")

def statistics(request):
    return render(request, "frontend/statistics.html")

def success(request):
    return render(request, "frontend/success.html")




# login con json
def login(request):
    # Retrieve the request parameters
    group = request.POST.get('group')
    list_number = request.POST.get('listNumber')
    student_id = request.POST.get('studentId')

    # Perform login logic and retrieve the relevant data
    # (e.g. group, list_number, etc.) from your data source
    # You can replace this with your actual login logic
    player_data = {'group': group, 'list_number': list_number, 'student_id': student_id}

    # Return the player data as a JSON response
    return JsonResponse(player_data)





#puedo hacer una forma y de ahi mandar los datos
def add_student_form(request):
    return render(request, "frontend/add_student_form.html")

def add_question_form(request):
    return render(request, "frontend/add_question_form.html")


#puedo mandar los datos en directo
# http://127.0.0.1:8000/add_student_func/group/42/1234/
def add_student_func2(request, group, list_number, student_id):
    # Create a new student with the provided values
    student = Student(group=group, list_number=list_number, student_id=student_id)
    student.save()
    return render(request, 'frontend/success.html')



# http://127.0.0.1:8000/add_question_func/my_question/1/2/3/4/5/6/7/8/correctA/correctB/10/1/easy/1234/
def add_question_func2(request, question, answer1a, answer1b, answer2a, answer2b, answer3a, answer3b, answer4a, answer4b, 
                 correctAnswerA, correctAnswerB, responseTime, level, difficulty, student_id):
    # Create a new question with the provided values
    question = Questions(question=question, answer1a=answer1a, answer1b=answer1b, answer2a=answer2a, answer2b=answer2b, 
                        answer3a=answer3a, answer3b=answer3b, answer4a=answer4a, answer4b=answer4b, correctAnswerA=correctAnswerA, 
                        correctAnswerB=correctAnswerB, responseTime=responseTime, level=level, difficulty=difficulty, student_id=student_id)
    question.save()
    return render(request, 'frontend/success.html')




# RECIBIR DATOS PARA GUARDAR por medio de json
#falta agregar LEVEL y DIFFICULTY
@method_decorator(csrf_exempt)
def add_student_func(request):
    if request.method == 'POST':
        try:
            # Load the JSON data from the request body
            data = json.loads(request.body)

            # Extract the values from the JSON data
            group = data['group']
            list_number = data['list_number']
            student_id = data['student_id']

            # Create a new student with the extracted values
            student = Student(group=group, list_number=list_number, student_id=student_id)
            student.save()

            return HttpResponse('Student created successfully')
        except json.JSONDecodeError:
            return HttpResponse('Invalid JSON data', status=400)
    else:
        return HttpResponse('Invalid request method', status=400)



# MOSTRAR DATOS por medio de json
#falta agregar LEVEL y DIFFICULTY
@csrf_exempt
def view_students(request):
    if request.method == 'GET':
        # Retrieve all students from the database
        students = Student.objects.all()

        # Create a list to hold the student data
        student_data = []
        for student in students:
            # Create a dictionary to store the student data
            student_dict = {
                'group': student.group,
                'list_number': student.list_number,
                'student_id': student.student_id
            }
            student_data.append(student_dict)

        # Return the student data as JSON response
        return JsonResponse(student_data, safe=False)
    else:
        return HttpResponse('Invalid request method', status=400)



"""
# http://127.0.0.1:8000/add_question_func/my_question/1/2/3/4/5/6/7/8/correctA/correctB/10/1/easy/1234/
def add_question_func(request, question, answer1a, answer1b, answer2a, answer2b, answer3a, answer3b, answer4a, answer4b, 
                 correctAnswerA, correctAnswerB, responseTime, level, difficulty, student_id):
    # Convert string inputs to their respective types
    answer1a = int(answer1a)
    answer1b = int(answer1b)
    answer2a = int(answer2a)
    answer2b = int(answer2b)
    answer3a = int(answer3a)
    answer3b = int(answer3b)
    answer4a = int(answer4a)
    answer4b = int(answer4b)
    responseTime = int(responseTime)
    level = int(level)
    student_id = int(student_id)

    # Create a new question with the provided values
    question = Questions(question=question, answer1a=answer1a, answer1b=answer1b, answer2a=answer2a, answer2b=answer2b, 
                        answer3a=answer3a, answer3b=answer3b, answer4a=answer4a, answer4b=answer4b, correctAnswerA=correctAnswerA, 
                        correctAnswerB=correctAnswerB, responseTime=responseTime, level=level, difficulty=difficulty, student_id=student_id)
    question.save()
    return render(request, 'frontend/success.html')

"""
