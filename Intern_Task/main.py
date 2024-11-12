# main.py
from instagram_scraper import InstagramScraper
from style_analyzer import StyleAnalyzer
from review_generator import ReviewGenerator
from script_generator import ScriptGenerator
from voice_synthesizer import VoiceSynthesizer
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

def main():
    # Step 1: Scrape content
    scraper = InstagramScraper()
    content = scraper.fetch_creator_content(username="abhishekkuntare")

    # Step 2: Analyze style
    style_analyzer = StyleAnalyzer()
    style_data = style_analyzer.analyze_text_style(content['captions'])

    # Step 3: Generate product review   
    review_gen = ReviewGenerator()
    product_info = review_gen.scrape_product_info("https://ecommerce-url.com/product")
    product_review = review_gen.generate_review(product_info)

    # Step 4: Generate script
    script_gen = ScriptGenerator(style_analyzer)
    script = script_gen.generate_script(product_review, style_data)

    # Step 5: Synthesize voice
    voice_synth = VoiceSynthesizer()
    voice_synth.synthesize_voice(script, "output_voice.mp3")
    print("Voice synthesis complete.")

if __name__ == "__main__":
    main()
