# style_analyzer.py
from transformers import pipeline
import spacy
from collections import Counter

class StyleAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        self.speech_recognizer = pipeline("automatic-speech-recognition")

    def analyze_text_style(self, captions: list[str]) -> dict:
        sentiments = [self.sentiment_analyzer(text)[0] for text in captions]
        common_phrases = self._extract_common_phrases(captions)

        return {
            'average_sentiment': sum([s['score'] for s in sentiments]) / len(sentiments),
            'common_phrases': common_phrases
        }

    def _extract_common_phrases(self, texts: list[str]) ->list[str]:
        phrases = []
        for text in texts:
            doc = self.nlp(text)
            phrases.extend([chunk.text for chunk in doc.noun_chunks])
        phrase_counts = Counter(phrases)
        return [phrase for phrase, count in phrase_counts.most_common(5)]
