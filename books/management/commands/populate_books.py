from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Populate the database with sample books'
    
    def handle(self, *args, **options):
        books_data = [
            
            {'title': 'Harry Potter and the Philosopher\'s Stone', 'author': 'J.K. Rowling', 'price': 15.99, 'rating': 4.8, 'publication_year': 1997, 'genre': 'Fantasy'},
            {'title': 'Harry Potter and the Chamber of Secrets', 'author': 'J.K. Rowling', 'price': 16.99, 'rating': 4.7, 'publication_year': 1998, 'genre': 'Fantasy'},
            {'title': 'Harry Potter and the Prisoner of Azkaban', 'author': 'J.K. Rowling', 'price': 17.99, 'rating': 4.9, 'publication_year': 1999, 'genre': 'Fantasy'},
            {'title': 'Harry Potter and the Goblet of Fire', 'author': 'J.K. Rowling', 'price': 18.99, 'rating': 4.8, 'publication_year': 2000, 'genre': 'Fantasy'},
            {'title': 'The Casual Vacancy', 'author': 'J.K. Rowling', 'price': 14.99, 'rating': 3.8, 'publication_year': 2012, 'genre': 'Contemporary Fiction'},
            
            
            {'title': 'The Shining', 'author': 'Stephen King', 'price': 16.99, 'rating': 4.6, 'publication_year': 1977, 'genre': 'Horror'},
            {'title': 'It', 'author': 'Stephen King', 'price': 19.99, 'rating': 4.7, 'publication_year': 1986, 'genre': 'Horror'},
            {'title': 'Pet Sematary', 'author': 'Stephen King', 'price': 15.99, 'rating': 4.4, 'publication_year': 1983, 'genre': 'Horror'},
            {'title': 'The Stand', 'author': 'Stephen King', 'price': 22.99, 'rating': 4.5, 'publication_year': 1978, 'genre': 'Post-Apocalyptic'},
            {'title': 'Carrie', 'author': 'Stephen King', 'price': 13.99, 'rating': 4.2, 'publication_year': 1974, 'genre': 'Horror'},
            {'title': 'Salem\'s Lot', 'author': 'Stephen King', 'price': 17.99, 'rating': 4.3, 'publication_year': 1975, 'genre': 'Horror'},
            
            
            {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'price': 12.99, 'rating': 4.4, 'publication_year': 1925, 'genre': 'Classic Fiction'},
            {'title': 'Tender Is the Night', 'author': 'F. Scott Fitzgerald', 'price': 14.99, 'rating': 4.1, 'publication_year': 1934, 'genre': 'Classic Fiction'},
            {'title': 'This Side of Paradise', 'author': 'F. Scott Fitzgerald', 'price': 13.99, 'rating': 3.9, 'publication_year': 1920, 'genre': 'Classic Fiction'},
            {'title': 'The Beautiful and Damned', 'author': 'F. Scott Fitzgerald', 'price': 13.50, 'rating': 3.8, 'publication_year': 1922, 'genre': 'Classic Fiction'},
            
            
            {'title': 'Good Omens', 'author': 'Neil Gaiman', 'price': 16.99, 'rating': 4.6, 'publication_year': 1990, 'genre': 'Fantasy'},
            {'title': 'American Gods', 'author': 'Neil Gaiman', 'price': 18.99, 'rating': 4.5, 'publication_year': 2001, 'genre': 'Fantasy'},
            {'title': 'The Sandman Vol. 1', 'author': 'Neil Gaiman', 'price': 19.99, 'rating': 4.8, 'publication_year': 1989, 'genre': 'Graphic Novel'},
            {'title': 'Neverwhere', 'author': 'Neil Gaiman', 'price': 15.99, 'rating': 4.4, 'publication_year': 1996, 'genre': 'Urban Fantasy'},
            {'title': 'Coraline', 'author': 'Neil Gaiman', 'price': 12.99, 'rating': 4.3, 'publication_year': 2002, 'genre': 'Dark Fantasy'},
        ]
        
        for book_data in books_data:
            Book.objects.get_or_create(**book_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated books with your favorite authors!'))
    

        
        