from questions import models
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    # python manage.py createtags --help
    help = 'Check'

    def calculate_confidence(self, count_correct_answer, count_conf_interval, count_questions):
        sum = count_correct_answer + 0.5 * count_conf_interval
        confidence = (sum/count_questions) * 100
        return confidence

    def handle(self, *args, **options):
    	#count of questions
        count_questions = 10
        #numbers of correct answers
        count_correct_answer = 0
        #numbers of answers with confidence = 50%
        count_conf_interval = 0
        user_confidence = 0
        #get a list of all State`s id
        id_list_corr = models.State.objects.values_list('id', flat = True)

        #get random State`s id
        rand_id_list = random.sample(list(id_list_corr), count_questions)

        print("\nВам нужно будет определить, является ли утверждение верным или не верным. И указать вашу уверенность в процентах от 50 до 100.\n")

        for i in range(0, count_questions):
            right_answer = ""
            fact = models.State.objects.filter(id = rand_id_list[i])
            country_name = fact.values_list('name', flat = True)
            flag = random.choice([0, 1])
            if (flag == 0):
                president = fact.values_list('head', flat = True)
                right_answer = "да"
            else:
                rand = random.choice(id_list_corr)
                other_fact = models.State.objects.filter(id = rand)
                president = other_fact.values_list('head', flat = True)
                if(fact.values_list('name', flat = True)[0] == other_fact.values_list('name', flat = True)[0]):
                    right_answer = "да"
                else:
                    right_answer = "нет"

            question = str(i+1) + ") " + president[0] + " является главой государства " + country_name[0] + "?"
            print(question)
            print("Правильный ответ :", right_answer)
            user_answer = input('Введите ваш ответ:')
            user_conf = int(input('Введите вашу уверенность:'))

            user_confidence+= user_conf
            if((user_answer == right_answer) & (user_conf == 50)):
                count_conf_interval+= 1
            else:
                if(user_answer == right_answer):
                    count_correct_answer+= 1

            models.QuestionSession.objects.create(id_question = models.State.objects.get(id = rand_id_list[i]),
            	id_session = 1, user_answer = user_answer, confidence = user_confidence)


        total_confidence = user_confidence/10
        really_confidence = self.calculate_confidence(count_correct_answer, count_conf_interval, count_questions)

        print("\nВаша уверенность: " + str(total_confidence) + "%")
        print("Ваша реальная уверенность: " + str(really_confidence) + "%")

