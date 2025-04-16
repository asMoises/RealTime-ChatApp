from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    displayname = models.CharField(max_length=20, null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user)
      
    #Aqui eu disponibilizo o nome no displayname, caso não tenha, o username
    # do user é utilizado.
    @property
    def name(self):
        if self.displayname:
          name = self.displayname
        else:
          name = self.user.username  
        return name
      
    #Mesma situação da anterior. Eu tento disponibilizar a imagem do usuário, caso não tenha,
    # eu disponibilizo uma imagem padrão que está na pasta static/images/avatar.svg
    # Essa imagem padrão é a mesma que o Django disponibiliza quando não tem imagem do usuário.
    # O método static é utilizado para pegar o caminho correto da imagem, independente do sistema operacional.  
    @property  
    def avatar(self):
      try:
        avatar = self.image.url
      except:
        avatar = static('images/avatar.svg')
      return avatar 