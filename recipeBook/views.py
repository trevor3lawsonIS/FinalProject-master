from django.shortcuts import render
from recipeBook.models import Recipe, Ingredient, Recipe_Ingredient

# Create your views here.

#take them back to homepage
def indexPageView(request) :
    return render(request, 'recipeBook/index.html') 
    
#takes them to the create page
def createPageView(request) :
    return render(request, 'recipeBook/create.html')

#shows them the recipies
def readPageView(request) :
    return render(request, 'recipeBook/read.html') 

#shows a single reciepie to the user
def showSingleRecipePageView(request, recID) :
    if request.method == 'POST':
        recipeIngredients = Recipe_Ingredient.objects.filter(RecipeID=recID)
        recipe = Recipe.objects.get(id=recID)

        context = {
            'rI': recipeIngredients,
            'rcp': recipe
        }
    else:
        recipeIngredients = Recipe_Ingredient.objects.filter(RecipeID=recID)
        recipe = Recipe.objects.get(id=recID)

        context = {
            'rI': recipeIngredients,
            'rcp': recipe
        }

    return render(request, 'recipeBook/showSingleRecipe.html', context)

#allows the user to change the recipies
def updateRecipePageView(request):
    if request.method == 'POST':
        rec_id = request.POST['rcpID']
        recipe = Recipe.objects.get(id = rec_id)
        recipe.RecipeTitle = request.POST['title']
        recipe.Preparation = request.POST['preparation']
        recipe.Notes = request.POST['notes']
        recipe.save()

        amountList = request.POST.getlist('recIng')
        recipeIngredients = request.POST.getlist('recIngID')
        for i in range(0, len(recipeIngredients)):
            recipeIngredient = Recipe_Ingredient.objects.get(id = recipeIngredients[i])
            recipeIngredient.Amount = amountList[i]
            recipeIngredient.save()

    return showSingleRecipePageView(request, rec_id)

#save your recipies
def saveNewRecipePageView(request):
    if request.method == 'POST':
        recipe = Recipe()
        recipe.RecipeTitle = request.POST['title']
        recipe.Preparation = request.POST['preparation']
        recipe.Notes = request.POST['notes']
        
        recipe.save()
        recID = recipe.id
    return chooseIngredients(request, recID)

#shows a certin ingredient chosen
def showSingleIngPageView(request, ingID):
    if request.method == 'POST':
        ingredient = Ingredient.objects.get(id=ingID)
    else:
        ingredient = Ingredient.objects.get(id=ingID)
    context = {
    'ing' : ingredient
    }
    return render(request, 'recipeBook/showSingleIngredient.html', context)

#updates the ingredint information
def updateIngPageView(request) :
    if request.method == 'POST':
        ing_id = request.POST['ingID']
        ingredient = Ingredient.objects.get(id = ing_id)
        ingredient.IngredientName = request.POST['name']
        ingredient.save()
    return viewIngredientsPageView(request)

#Saves a new ingredient
def saveNewIngredientPageView(request) :
    if request.method == 'POST':
        ingredient = Ingredient()
        ingredient.IngredientName= request.POST['name']
        ingredient.save()
        
    return viewIngredientsPageView(request)

#takes you to the add ingredient page
def addIngredientPageView(request):
    return render(request, 'recipeBook/addIngredient.html')

#Takes you to the add recipie page
def addRecipePageView(request):
    return render(request, 'recipeBook/addRecipe.html')

#Allows you to update a recipie ingredient and then takes you to the update recipe ingredint page
def updateRecipeIngredient(request, rec_id):
    recipe = Recipe.objects.get(id=rec_id)
    recIngredients = Recipe_Ingredient.objects.filter(RecipeID_id = rec_id)
    ingredients = Ingredient.objects.all()
    
    context = {
        'rec': recipe,
        'recIng': recIngredients,
        'ing': ingredients,
        
    }

    return render(request, 'recipeBook/updateRecipeIngredients.html', context)

#displays recipies
def viewRecipesPageView(request):
    recipes = Recipe.objects.all()
    context = {
        'rcp' : recipes
    }
    return render(request, 'recipeBook/showRecipes.html', context)

#displays ingredients
def viewIngredientsPageView(request):
    ingredients = Ingredient.objects.all()
    
    context = {
        'ing' : ingredients
    }
    return render(request, 'recipeBook/showIngredients.html', context)

#deletes ingredients
def deleteIngredientPageView(request, ingID):
    ing = Ingredient.objects.get(id=ingID)
    ing.delete()
    
    return viewIngredientsPageView(request)

#deletes a recipie
def deleteRecipePageView(request, recID):
    rec = Recipe.objects.get(id=recID)
    rec.delete()

    return viewRecipesPageView(request)

def deleteRecipeIngredientPageView(request, recIngID):
    recipeIngredient = Recipe_Ingredient.objects.get(id=recIngID)
    recID = recipeIngredient.RecipeID_id
    recipeIngredient.delete()

    return showSingleRecipePageView(request, recID)

#allows you to choose an ingredint 
def chooseIngredients(request, recID):
    ingredients = Ingredient.objects.all()
    context = {
        'ingredients' : ingredients,
        'recID' : recID
    }
    return render(request, 'recipeBook/chooseIngredients.html', context)

#creates a recpie ingredient
def addRecipeIngredientsPageView(request):
    if request.method == 'POST':
        recID = request.POST['recID']
        ingredientList = request.POST.getlist('array')
        ingredients = Ingredient.objects.filter(id__in = ingredientList)

        context =  {
            'recID' : recID,
            'ingredients': ingredients
        }

    return render(request, 'recipeBook/addRecipeIngredient.html', context)

#saves the new recipie ingredient
def saveNewRecipeIngredientPageView(request):
    if request.method == 'POST':
        recID = request.POST['recID']
        ingredientList = request.POST.getlist('ingID')
        amountList = request.POST.getlist('recIng')
        for i in range(0, len(ingredientList)):
            recipeIngredient = Recipe_Ingredient()
            recipeIngredient.RecipeID_id = recID
            recipeIngredient.IngredientID_id = ingredientList[i]
            recipeIngredient.Amount = amountList[i]
            recipeIngredient.save()
    return showSingleRecipePageView(request, recID)








