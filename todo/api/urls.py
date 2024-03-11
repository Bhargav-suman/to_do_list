from django.urls import path
from api import views

urlpatterns = [
    path('',views.apiOverview,name="api-overview"),
    path('task-list/',views.taskList,name="task-list"),
    path('task-detail/<int:pk>/',views.taskDetail,name="task-detail"),
    path('task-create/',views.taskCreate,name="task-create"),
    path('task-update/<int:p>/',views.taskUpdate,name="task-update"),
    path('task-delete/<int:p>/',views.taskDelete,name="task-delete"),
    
    
]