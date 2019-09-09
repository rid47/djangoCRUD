from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [

    path('contacts/', views.contacts, name='all_contacts'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('edit_contact/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete_contact/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('profile_info/<int:pk>/', views.profile_info, name='profile_info')


]