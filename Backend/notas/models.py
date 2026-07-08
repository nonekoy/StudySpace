from django.db import models

# Create your models here.
class Nota (models.Model):
    created_by= models.ForeignKey ()
    created_at= models.DateTimeField (auto_now_add=True)
    deleted= models.BooleanField (default=False)
    conteudo= models.TextField ()
    updated_at= models.DateTimeField (auto_now=True)
    updated_by= models.ForeignKey ()
    
    class Meta: 
        verbose_name= 'Nota'
        verbose_name_plural= 'Notas'

    def delete (self):
        if self.pk is None: 
            return
        if self.deleted: 
            return
        self.deleted= True
        update_fields= ['deleted']
        self.save (update_fields=update_fields)

    