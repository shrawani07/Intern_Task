# script_generator.py
from style_analyzer import StyleAnalyzer  # Adjust the path if necessary

class ScriptGenerator:
    def __init__(self, style_analyzer: StyleAnalyzer):
        self.style_analyzer = style_analyzer

    def generate_script(self, product_review: str, style_data: dict) -> str:
        phrases = style_data['common_phrases']
        script = f"{phrases[0]}, here's a review for you: {product_review}"
        return script
