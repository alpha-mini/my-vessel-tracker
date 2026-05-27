name: Vessel Tracker Update

on:
  schedule:
    - cron: '0 * * * *'       # Runs every hour
  workflow_dispatch:           # Allows manual trigger

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install requests

      - name: Run Tracker
        # No API key needed for MarineTraffic!
        # If you want to use VesselAPI as backup, add VESSELAPI_KEY secret:
        # env:
        #   VESSELAPI_KEY: ${{ secrets.VESSELAPI_KEY }}
        run: python tracker.py

      - name: Commit and Push Data
        run: |
          git config --global user.name "GitHub Action"
          git config --global user.email "actions@github.com"
          git add vessels.json
          git commit -m "Update vessel data" || exit 0
          git push
