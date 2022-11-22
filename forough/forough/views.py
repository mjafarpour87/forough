import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings

from .extend_settings import LOGGING
import logging
logging.config.dictConfig(LOGGING)
logger = logging.getLogger('app')

class page_chat(TemplateView):
    template_name = 'page_chat.html'


class ChatterBotAppView(TemplateView):
    template_name = 'app.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)
        logger.debug(type(response))
        logger.debug(response.search_text)
        logger.debug(response.persona)
        logger.debug(response.tags)
        logger.debug(response.in_response_to)
        logger.debug(response.search_in_response_to)
        logger.debug(response.confidence)


        response_data = response.serialize()
        logger.debug(response_data)
        if response.confidence < 0.5 :
            response_data['text'] = 'در این حد بلد نیستم'


        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })
