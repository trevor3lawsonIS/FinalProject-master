from django.urls import path
from .views import indexPageView
from .views import createPageView
from .views import showSingleRecipePageView
from .views import readPageView
from .views import updateRecipePageView
from .views import saveNewRecipePageView
from .views import showSingleIngPageView
from .views import updateIngPageView
from .views import saveNewIngredientPageView
from .views import addIngredientPageView
from .views import viewRecipesPageView
from .views import viewIngredientsPageView
from .views import addRecipePageView
from .views import deleteIngredientPageView
from .views import deleteRecipePageView
from .views import chooseIngredients
from .views import addRecipeIngredientsPageView
from .views import saveNewRecipeIngredientPageView
urlpatterns = [
    path("", indexPageView, name="index"),
    path("create", createPageView, name="create"),
    path("read", readPageView, name="read"),
    path('showRecipe/<int:recID>/', showSingleRecipePageView, name='showRecipe'),
    path('updateRecipe/', updateRecipePageView, name='updateRec'),
    path('saveNewRecipe/', saveNewRecipePageView, name='saveNewRecipe'),
    path("showIngredient/<int:ingID>", showSingleIngPageView, name="showIngredient"),
    path("updateIng/", updateIngPageView, name="updateIng"),
    path("saveNewIngredient/", saveNewIngredientPageView, name="saveNewIngredient"), 
    path('recipes/', viewRecipesPageView, name='viewRecipes'),
    path('ingredients/', viewIngredientsPageView, name='viewIngredients'),
    path('addIngredient/', addIngredientPageView, name='addIngredient'),
    path('addRecipe/', addRecipePageView, name = 'addRecipe'),
    path('deleteIngredient/<int:ingID>', deleteIngredientPageView,name='deleteIngredient'),
    path('deleteRecipe/<int:recID>', deleteRecipePageView, name='deleteRecipe'),
    path('chooseIngredients/', chooseIngredients, name='chooseIngredients'),
    path('addRecipeIngredient/', addRecipeIngredientsPageView, name='addRecipeIngredient'),
    path('saveRecipeIngredients/', saveNewRecipeIngredientPageView, name = 'saveRecipeIngredient')


]

