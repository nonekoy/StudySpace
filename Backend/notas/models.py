from django.db import models
from django.contrib.auth import get_user_model

User= get_user_model()
# Create your models here.
class Nota (models.Model):
    created_by= models.ForeignKey (
        User, 
        on_delete= models.SET_NULL, 
        null=True,
        blank=True,
        related_name= 'registros_criados'
    )
    created_at= models.DateTimeField (auto_now_add=True)
    deleted= models.BooleanField (default=False)
    conteudo= models.TextField ()
    updated_at= models.DateTimeField (auto_now=True)
    updated_by= models.ForeignKey (
        User,
        on_delete= models.SET_NULL,
        null=True,
        blank=True,
        related_name= 'registros_atualizados'
    )
    
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

    