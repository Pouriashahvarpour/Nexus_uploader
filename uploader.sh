#!/bin/bash

# Nexus PyPI Package Uploader Script
# This script installs dependencies and uploads packages to Nexus repository

set -e  # Exit on error

echo "🚀 Starting Nexus Package Uploader..."
echo ""

# Change to data directory
cd /data

echo "📦 Installing dependencies..."
pip install -q  requests

echo "⬇️  Downloading packages from requirements.txt..."
pip download -r requirements.txt -d dist/

echo "📤 Uploading packages to Nexus..."
python3 uploader.py

echo ""
echo "✅ Done!"