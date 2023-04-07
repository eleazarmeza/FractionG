from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('statistics', views.statistics, name="statistics"),
    path('success', views.success, name="success"),
    path('add_question_form', views.add_question_form, name="add_question_form"),
    path('add_student_form', views.add_student_form, name="add_student_form"),
    path('add_student_func', views.add_student_func, name="add_student_func"),
    path('add_student_func2/<str:group>/<int:list_number>/<int:student_id>/', views.add_student_func2, name='add_student_func2'),
    path('add_question_func2/<str:question>/<int:answer1a>/<int:answer1b>/<int:answer2a>/<int:answer2b>/<int:answer3a>/<int:answer3b>/<int:answer4a>/<int:answer4b>/<int:correctAnswerA>/<int:correctAnswerB>/<int:responseTime>/<int:level>/<int:difficulty>/<int:student_id>/', views.add_question_func2, name='add_question_func2'),
    path('login', views.login, name="login"),
    path('view_students', views.view_students, name="view_students"),
   
]
