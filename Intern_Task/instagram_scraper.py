# instagram_scraper.py
import instaloader
import os
from moviepy.editor import VideoFileClip
from typing import List, Dict

class InstagramScraper:
    def __init__(self):
        self.loader = instaloader.Instaloader()
        self.temp_dir = "temp_downloads"
        os.makedirs(self.temp_dir, exist_ok=True)

    def authenticate(self, username: str, password: str) -> bool:
        try:
            self.loader.login(username, password)
            return True
        except Exception as e:
            print(f"Authentication failed: {e}")
            return False

    def fetch_creator_content(self, username: str, max_posts: int = 10) -> Dict:
        profile = instaloader.Profile.from_username(self.loader.context, username)
        posts = profile.get_posts()
        videos = []
        captions = []

        for i, post in enumerate(posts):
            if i >= max_posts:
                break
            if post.is_video:
                video_data = self._process_video(post)
                videos.append(video_data)
                captions.append(post.caption or "")

        return {'videos': videos, 'captions': captions}

    def _process_video(self, post) -> Dict:
        video_path = f"{self.temp_dir}/{post.shortcode}.mp4"
        self.loader.download_post(post, target=self.temp_dir)
        with VideoFileClip(video_path) as video:
            audio_path = self._extract_audio(video, post.shortcode)
            return {'video_path': video_path, 'audio_path': audio_path}

    def _extract_audio(self, video: VideoFileClip, shortcode: str) -> str:
        audio_path = f"{self.temp_dir}/audio_{shortcode}.mp3"
        video.audio.write_audiofile(audio_path)
        return audio_path
