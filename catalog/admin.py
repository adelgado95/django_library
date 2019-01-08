from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

admin.site.register(Language)
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
class BooksInLine(admin.TabularInline):
    model = Book
    extra = 0
    readonly_fields = ['summary','title','isbn','summary','genre','language',]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','date_of_birth','date_of_death')
    fields = ['first_name','last_name', ('date_of_birth','date_of_death')]
    inlines = [BooksInLine]
admin.site.register(Author, AuthorAdmin)

##hace lo mismo que admin.site.register()

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]



@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','status','borrower','due_back','book')
    list_filter = ('status','due_back')
    fieldsets = (
        (None,{
                'fields':('book','imprint','id')
        }),
        ('Availability',{
            'fields':('status','due_back','borrower')
        })
    )
