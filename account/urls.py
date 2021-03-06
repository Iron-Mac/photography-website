from django.conf.urls import url
from django.contrib.auth import views
from django.urls import path
from .views import PostDelete, PostList,PostCreate, PostUpdate

app_name = 'account'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

#    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
#    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

#    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
#    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#   path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


urlpatterns+=[
    path('', PostList.as_view() , name='home'),
    path('create/', PostCreate.as_view() , name='create_post'),
    path('update/<int:pk>', PostUpdate.as_view() , name='update_post'),
    path('delete/<int:pk>', PostDelete.as_view() , name='delete_post')


]