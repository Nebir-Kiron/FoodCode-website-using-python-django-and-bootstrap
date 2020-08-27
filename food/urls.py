from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("item/", views.item, name="item"),
    path("<int:pk>/", views.Details.as_view(), name="itemDetails"),
    
    # add items
    path("add/", views.Create_item.as_view(), name="createItems"),
    
    #update
    path("update/<int:id>/", views.update_item, name="updateItems"),
    
    #delete
    path("delete/<int:id>/", views.delete_item, name="deleteItems"),

]