from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),  # Add this line
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
     

    path('students/', views.student, name='student'),
    path('students_list/', views.student_list, name='student_list'),
   

]  
 