from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
    path("", views.index, name="index"),
    path("item/", views.item, name="item"),
    path("<int:id>/", views.details, name="itemDetails"),
    
    # add items
    path("add/", views.create_item, name="createItems"),
    
    #update
    path("update/<int:id>/", views.update_item, name="updateItems"),
    
    #delete
    path("delete/<int:id>/", views.delete_item, name="deleteItems"),

]