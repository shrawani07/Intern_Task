# review_generator.py
from transformers import pipeline
import requests
from bs4 import BeautifulSoup

class ReviewGenerator:
    def __init__(self):
        self.generator = pipeline("text-generation", model="gpt-3.5-turbo")

    def scrape_product_info(self, url: str) -> str:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find("h1").text
        description = soup.find("meta", {"name": "description"}).get("content", "")
        return f"Product: {title}. {description}"

    def generate_review(self, product_info: str) -> str:
        review_prompt = f"Write a review for this product:\n{product_info}\nReview:"
        review = self.generator(review_prompt, max_length=150)
        return review[0]['generated_text']
