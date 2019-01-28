from django.core.management.base import BaseCommand, CommandError
from basketball.models import Team, Tournament, Bracket, Season_stats, Participant

class Person:

    def __init__(self,name):
        self.name = name
        self.first = 0
        self.second = 0
        self.third = 0
        self.correct_champions = 0
        self.average_predicted_upsets = 0
        self.average_correct_upsets = 0

    def __str__(self):
        return self.name

    def set_correct_champions(self):
        true_brackets = Bracket.objects.filter(name="TRUTH").all()
        self_brackets = Bracket.objects.filter(name=self.name).all()
        for i in range(len(true_brackets)):
            if true_brackets[i].championship == self_brackets[i].championship:
                self.correct_champions += 1

    def set_average_predicted_upsets(self):
        self_brackets = Bracket.objects.filter(name=self.name).all()
        total = 0
        for b in self_brackets:
            total += b.num_upsets()
        self.average_predicted_upsets = total/len(self_brackets)

    def set_average_predicted_upsets(self):
        self_brackets = Bracket.objects.filter(name=self.name).all()
        total = 0
        for b in self_brackets:
            total += b.num_upsets()
        self.average_predicted_upsets = total/len(self_brackets)

    def set_average_correct_upsets(self):
        self_brackets = Bracket.objects.filter(name=self.name).all()
        total = 0
        for b in self_brackets:
            total += b.num_correct_upsets()
        self.average_correct_upsets = total/len(self_brackets)

class Command(BaseCommand):

    def handle(self, *args, **options):

        finishes = self.determine_finishes()
        for (p,_) in Participant.PARTICIPANT_NAMES:
            person = Person(p)
            self.stdout.write("{}".format(person))
            person.first = finishes[p][0]
            person.second = finishes[p][1]
            person.third = finishes[p][2]
            person.set_correct_champions()
            person.set_average_predicted_upsets()
            person.set_average_correct_upsets()
            #self.stdout.write("Firsts: {}".format(person.first))
            #self.stdout.write("Seconds: {}".format(person.second))
            #self.stdout.write("Thirds: {}".format(person.third))
            #self.stdout.write("Correct Champions: {}".format(person.correct_champions))
            #self.stdout.write("Average Predicted Upsets: {}".format(person.average_predicted_upsets))
            #self.stdout.write("Average Correct Upsets: {}".format(person.average_correct_upsets))
            Participant.objects.create(name=person.name, first_place=person.first,
                    second_place=person.second, third_place=person.third,
                    correct_champions=person.correct_champions,
                    average_predicted_upsets=person.average_predicted_upsets,
                    average_correct_upsets=person.average_correct_upsets)
            self.stdout.write("Created Pariticpant {}".format(person.name))


    def determine_finishes(self):
        all_brackets = Bracket.objects.exclude(name__in=["TRUTH","ROOMMATE","BROTHER","DAD"]).order_by('-year','-score')

        if all_brackets:
            finish = {"MOM":[0, 0, 0], "AUNT":[0, 0, 0], "ME":[0, 0, 0]}
            place = 1
            last_year = None
            for b in all_brackets:
                if last_year != b.year:
                    last_year = b.year
                    place = 1
                else:
                    place += 1
                finish[b.name][place - 1] += 1
            return finish
