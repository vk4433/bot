# Talk & Translate 🗣️🔁

## Overview
**Talk & Translate** is a speech-to-text translation app that lets users speak in one language, generate content, translate it into another language, and hear the translated audio.

![alt text](<Screenshot 2025-01-31 231012.png>)
## Features 🚀
- 🎙️ **Real-time Speech Recognition**: Capture and convert spoken words into text.
- 🌍 **Multi-Language Support**: Detect and translate speech into various languages.
- 📝 **AI-Powered Content Generation**: Generate explanations and translations using Google Gemini AI.
- 🔄 **Text & Audio Translation**: Convert translated text into speech for better understanding.
- 🎧 **Listen to Translations**: Hear translations in your chosen language.

## How It Works 🔥
1. **Select Languages**: Choose the source and target languages.
2. **Start Recording**: Click the mic button and begin speaking.
3. **Translate & Generate**: The app detects the language, translates it, and generates content if needed.
4. **Listen to the Output**: Hear the translated speech in the target language.

## Installation 🛠️
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/talk-translate.git
   cd talk-translate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your **Google API Key**:
   - Create a `.env` file and add your Google API key:
     ```
     google_api=YOUR_GOOGLE_API_KEY
     ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Supported Languages 🌎
- English 🇬🇧
- Hindi 🇮🇳
- Telugu 🇮🇳
- Kannada 🇮🇳
- Tamil 🇮🇳
- Malayalam 🇮🇳
- Bengali 🇮🇳
- German 🇩🇪
- Chinese 🇨🇳
- Japanese 🇯🇵
- Arabic 🇸🇦
- Italian 🇮🇹
- Korean 🇰🇷

## Dependencies 📦
- `streamlit`
- `speech_recognition`
- `deep_translator`
- `langdetect`
- `gtts`
- `google-generativeai`
- `python-dotenv`

## Contributing 🤝
Pull requests are welcome! Feel free to open an issue if you have suggestions or bug reports.

## License 📜
This project is licensed under the MIT License.




