

# cada modelo é representado por uma classe derivada da classe django.db.models.Model

# O nome de cada instância Field (por exemplo question_text ou pub_date) é o nome 
# do campo, em formato amigável para a máquina. Você irá usar este valor no seu 
# código Python, e seu banco de dados irá usá-lo como nome de coluna.

# É importante adicionar métodos __str__() aos seus modelos, não apenas para sua 
# própria conveniência quando estiver lidando com o prompt interativo, mas também 
# porque representações de objetos são usadas por todo interface administrativa 
# gerada automaticamente pelo Django.
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.question_text
    

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

        
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


    




