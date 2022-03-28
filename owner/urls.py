from django.urls import path
from owner import views
# # owner/book/100
urlpatterns=[
    path('books/add',views.AddBookView.as_view(),name='addbook'),
    path('books/all',views.BookListView.as_view(),name='listbook'),
    path('books/<int:id>',views.BookDetailView.as_view(),name='bookdetail'),
    path('books/change/<int:id>',views.BookEditView.as_view(),name='bookedit'),
    path('books/remove/<int:id>',views.BookDeleteView.as_view(),name='bookremove')
#     path("home",views.owner_home),
#     path("books/add",views.add_book),
#     path("books/all",views.list_book),
#     path("book/<int:id>",views.book_detail),
#
]
