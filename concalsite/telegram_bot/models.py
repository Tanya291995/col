from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    head = models.CharField(max_length=100)

    def __str__(self):
        text = str(self.id) + ") " + self.name + ", " + self.head + "\n"
        return text

class QuestionSession(models.Model):
	id_question = models.ForeignKey(State)
	id_session = models.IntegerField()
	user_answer = models.CharField(max_length=10)
	confidence = models.IntegerField()

	def __str__(self):
		text = str(self.id) + ") " + ", id_q = " + str(self.id_question.id) + ", id_session = " + str(self.id_session) + ", user_answer = " + self.user_answer + ", conf = " + str(self.confidence) + "\n"
		return text
