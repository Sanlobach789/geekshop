from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('users/', adminapp.UsersListView.as_view(), name='admin_users'),
    path('users/create/', adminapp.UsersCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', adminapp.UsersUpdateView.as_view(), name='admin_users_update'),
    path('users/remove/<int:pk>/', adminapp.UserDeleteView.as_view(), name='admin_users_remove'),
    path('categories/', adminapp.admin_categories, name='admin_categories'),
    path('categories/create/', adminapp.admin_categories_create, name='admin_categories_create'),
    path('categories/update/<int:category_id>/', adminapp.admin_categories_update, name='admin_categories_update'),
    path('categories/remove/<int:category_id>/', adminapp.admin_categories_remove, name='admin_categories_remove'),
    path('products/', adminapp.admin_products, name='admin_products'),
    path('products/create/', adminapp.admin_products_create, name='admin_products_create'),
    path('products/update/<int:product_id>/', adminapp.admin_products_update, name='admin_products_update'),
    path('products/remove/<int:product_id>/', adminapp.admin_products_remove, name='admin_products_remove'),
]