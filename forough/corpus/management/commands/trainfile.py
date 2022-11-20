from django.core.management.base import BaseCommand

from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import json
from pathlib import Path
class Command(BaseCommand):
    """
    A Django management command for calling a
    chat bot's training method.
    """

    help = "Trains the database used by the chat bot"
    can_import_settings = True

    def handle(self, *args, **options):
        DIR = Path(__file__).resolve().parent / 'karshenasi.json'
        print(DIR)
        # Opening JSON file
        f = open(DIR, encoding='utf-8')
        
        # returns JSON object as 
        # a dictionary
        data = json.load(f)

        # Closing file
        f.close()

        chatterbot = ChatBot(**settings.CHATTERBOT)

        trainer = ListTrainer(chatterbot)
        # trainer = ChatterBotCorpusTrainer(chatterbot)
        # trainer.train(*settings.CHATTERBOT["training_data"])

        # Iterating through the json
        # list
        for i in data['conversations']:
            # print(i[0])
            # print("")
            # print(i[1])
            trainer.train([
                i[0],
                i[1],
            ])

        self.stdout.write(self.style.SUCCESS("Starting training..."))
        self.stdout.write(
            self.style.SUCCESS(
                f'ChatterBot trained using "{trainer.__class__.__name__}"'
            )
        )
