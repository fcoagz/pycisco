from g4f import ChatCompletion
from g4f.Provider import (
    Aichat, DeepAi, GetGpt, H2o, opchatgpts
    )
from g4f.models import (
    falcon_7b, falcon_40b, gpt_35_turbo, llama_13b
)

from nltk.sentiment.vader import SentimentIntensityAnalyzer

ai = ['Aichat', 'DeepAi', 'GetGpt', 'H2o', 'opchatgpts']
models = [falcon_7b, falcon_40b, llama_13b, gpt_35_turbo]

class Api(object):
    @classmethod
    def get_message(self, Ai: str, model: str, message: str):
        
        while True:
            try:
                sentiment_message = self.receiver_comprehension(message)
                break
            except LookupError:
                import nltk
                nltk.download('vader_lexicon')
        
        provider = Aichat if Ai == 'Aichat' else DeepAi if Ai == 'DeepAi' else GetGpt if Ai == 'GetGpt' else H2o if Ai == 'H2o' else opchatgpts
        response = ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": f"Spanish. {sentiment_message}. {message}"}],
            provider=provider
        )
        return response
    
    @classmethod
    def receiver_comprehension(self, message: str):
        context = SentimentIntensityAnalyzer()

        received_context = context.polarity_scores(message)
        if received_context['compound'] > 0.05:
            return "Responderás positivamente"
        elif received_context['compound'] < -0.05:
            return "Responderás negativamente"
        else:
            return "Responderás neutral"