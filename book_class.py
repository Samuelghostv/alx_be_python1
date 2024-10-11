class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self): 
        
        """
        Destructor will be called when the instance is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):

        """
        String representation of the users or the instance of the class Book"""
        return f"{self.title} by {self.author} published in {self.year}"
    
    def __repr__(self):

        """
        Restring representation of the users or the instance of the class that can recreate the users
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
    

    