from .models import Category

def category_list(request):
    cat_menu_list = Category.objects.all()
    return {'cat_menu_list': cat_menu_list}
