from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCategoryEditForm, ProductEditForm
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')


# Следующие контроллеры демонстрируют принцип CRUD
class UsersListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UsersCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    form_class = UserAdminRegisterForm


class UsersUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    form_class = UserAdminProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование пользователя'
        return context


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# Admin-categories___________________________________________________________________________________________________
@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):
    # C - Create
    if request.method == 'POST':
        form = ProductCategoryEditForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_categories'))
        else:
            print(form.errors)
    else:
        form = ProductCategoryEditForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-categories-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    # R - Read
    context = {
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'adminapp/admin-categories-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_update(request, category_id):
    # U - Update
    category = ProductCategory.objects.get(id=category_id)
    if request.method == 'POST':
        form = ProductCategoryEditForm(data=request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_categories'))
    else:
        form = ProductCategoryEditForm(instance=category)

    context = {'form': form, 'category': category}
    return render(request, 'adminapp/admin-categories-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_remove(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    # category.delete()
    category.is_active = False
    category.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_categories'))

# Admin-products___________________________________________________________________________________________________
@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    # C - Create
    if request.method == 'POST':
        form = ProductEditForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products'))
        else:
            print(form.errors)
    else:
        form = ProductEditForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    # R - Read
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'adminapp/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, product_id):
    # U - Update
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductEditForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products'))
    else:
        form = ProductEditForm(instance=product)

    context = {'form': form, 'product': product}
    return render(request, 'adminapp/admin-products-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_remove(request, product_id):
    product = ProductCategory.objects.get(id=product_id)
    # category.delete()
    product.is_active = False
    product.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_products'))
