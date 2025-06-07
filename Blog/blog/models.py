from django.db import models

# Create your models here.
class Blog(models.Model):
    """A topic the user is posting about"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


#Creating an Entry Model that can be nested under a Topic
class Blog_Post(models.Model):
    """Something specific enter about a topic"""
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)


    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        if len(self.text) > 50: 
            return f"{self.text[:50]}..."
        
        #The ellipsis (...) is to remind the UI that we're not presenting the entire entry. Well. It shows anyway even if you have less than 50 characters so woops oh well.

        else:
            return f"{self.text}"