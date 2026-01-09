import asyncio
import random
import os
import csv
from datetime import datetime
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

# The specific URL for Crescent River
URL = "https://www.marinetraffic.com/en/ais/details/ships/shipid:5178657/mmsi:563079500/imo:9800726/vessel:CRESCENT_RIVER"

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
]

async def get_vessel_data():
    # Anti-ban: Wait 1-5 mins if running on GitHub to look human
    if os.getenv("GITHUB_ACTIONS"):
        await asyncio.sleep(random.randint(60, 300))

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True
