from django.urls import path
from .views import indexPageView
from .views import createPageView
from .views import showSingleRecipePageView
from .views import readPageView
from .views import updatePageView
from .views import addRecipePageView
from .views import showSingleIngPageView
from .views import updateIngPageView
from .views import addIngPageView
from .views import updateRecipeIngredient

urlpatterns = [
    path("", indexPageView, name="index"),
    path("create", createPageView, name="create"),
    path("read", readPageView, name="read"),
    path('showRecipe/<int:rec_id>/', showSingleRecipePageView, name='update'),
    path('updateRecipe/', updatePageView, name='updateRec'),
    path('addRecipe/', addRecipePageView, name='addRecipe'),
    path("showIng/", showSingleIngPageView, name="showIng"),
    path("updateIng/", updateIngPageView, name="updateIng"),
    path("addIng/", addIngPageView, name="addIng"), 
    path('updateRecIng/<int:rec_id>/', updateRecipeIngredient, name = 'updateRecIng'),

]

