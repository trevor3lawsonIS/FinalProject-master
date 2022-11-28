from django.shortcuts import render
from recipeBook.models import Recipe, Ingredient, Recipe_Ingredient

# Create your views here.
def indexPageView(request) :
    return render(request, 'recipeBook/index.html') 

def createPageView(request) :
    return render(request, 'recipeBook/create.html')


def readPageView(request) :
    return render(request, 'recipeBook/read.html') 

def showSingleRecipePageView(request, rec_id) :
    recipe = Recipe.objects.get(id=rec_id)

    context = {
        'rcp': recipe
    }
    return render(request, 'recipeBook/updateRecipe.html', context)

def updatePageView(request):
    if request.method == 'POST':
        rec_id = request.POST['rec_id']

        recipe = Recipe.objects.get(id = rec_id)

        recipe.RecipeTitle = request.POST['title']
        recipe.Preparation = request.POST['preparation']
        recipe.Notes = request.POST['notes']

        recipe.save()
    return showSingleRecipePageView(request)

def addRecipePageView(request):
    if request.method == 'POST':
        recipe = Recipe()
        recipe.RecipeTitle = request.POST['title']
        recipe.Preparation = request.POST['preparation']
        recipe.Notes = request.POST['notes']

        recipe.save()
    return showSingleRecipePageView(request)

def showSingleIngPageView(request):
    ingredient = Ingredient.objects.all()
    context = {
        'ing' : ingredient
    }
    return render(request, 'recipeBook/updateIngredients.html', context)

def updateIngPageView(request) :
    if request.method == 'POST':
        ing_id = request.POST['ing_id']
        ingredient = Ingredient.objects.get(id = ing_id)
        ingredient.IngredientName= request.POST['name']
        ingredient.save()
    return showSingleIngPageView(request) 

def addIngPageView(request) :
    if request.method == 'POST':
        ingredient = Ingredient()
        ingredient.IngredientName= request.POST['name']
        ingredient.save()
    return showSingleIngPageView(request)

def updateRecipeIngredient(request, rec_id):
    recipe = Recipe.objects.get(id=rec_id)
    recIngredients = Recipe_Ingredient.objects.filter(RecipeID_id = rec_id)
    ingredients = Ingredient.objects.all()
    context = {
        'rec': recipe,
        'recIng': recIngredients,
        'ing': ingredients
    }

    return render(request, 'recipeBook/updateRecipeIngredients.html', context)
def addRecipeIngredient(request):
    if request.method == 'POST':
        rec_id = request.POST['rec_id']
        recipeIngredient = Recipe_Ingredient()
        recipeIngredient. = request.POST['name']
        ingredient.save()

    return updateRecipeIngredient(request)







