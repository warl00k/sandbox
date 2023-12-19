from django.urls import path
from person.views import PersonView, PersonDetailView

urlpatterns = [
    path('', PersonView.as_view()),
    path('<int:id>/', PersonDetailView.as_view()),
]
