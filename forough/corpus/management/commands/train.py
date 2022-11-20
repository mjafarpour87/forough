from django.core.management.base import BaseCommand

from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer


class Command(BaseCommand):
    """
    A Django management command for calling a
    chat bot's training method.
    """

    help = "Trains the database used by the chat bot"
    can_import_settings = True

    def handle(self, *args, **options):
        chatterbot = ChatBot(**settings.CHATTERBOT)
        trainer = ChatterBotCorpusTrainer(chatterbot)
        trainer.train(*settings.CHATTERBOT["training_data"])

        self.stdout.write(self.style.SUCCESS("Starting training..."))
        self.stdout.write(
            self.style.SUCCESS(
                f'ChatterBot trained using "{trainer.__class__.__name__}"'
            )
        )
