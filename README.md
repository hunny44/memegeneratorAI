# AI Meme Generator

A full-stack web application that uses AI to generate custom memes. Powered by Google's Gemini 1.5 Pro for text generation and advanced image generation APIs.

## Features

### Core Functionality
- 🤖 AI-powered meme text generation using Gemini 1.5 Pro
- 🎨 High-quality image generation
- 💾 Local storage for meme history with deletion capabilities
- ⬇️ Direct meme download functionality
- 👤 User authentication system
- 📱 Responsive design for all devices

### User Interface
- 🎭 Interactive meme generation interface
- 📝 Simple prompt-based creation
- 📚 Sidebar with meme history management
  - Individual meme deletion
  - Bulk history clearing
  - Date-based organization
- 💫 One-click meme downloads
- 🌈 Animated background elements
- 🎨 Modern, dark theme design

### User Management
- ✨ User registration and login
- 👤 Personal profile pages
- 🔐 Secure authentication
- 📊 User activity tracking

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Flask
- Google Generative AI package
- Other dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-meme-generator.git
cd ai-meme-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API keys:
Create a file named `api_keys.ini` in the root directory with the following structure:
```ini
[Keys]
Gemini = your_gemini_api_key
ClipDrop = your_clipdrop_api_key
StabilityAI = your_stabilityai_api_key
```

4. Run the application:
```bash
python app.py
```

## Usage

1. **Registration/Login**
   - Create an account or log in to access the meme generator
   - Secure authentication system protects your memes

2. **Creating Memes**
   - Click "New Meme" or use the main input area
   - Enter your meme concept/prompt
   - Click "Generate Meme" to create
   - View your generated meme instantly
   - Download your meme with one click
   - Automatic filename generation based on prompt

3. **History & Management**
   - View your meme history in the sidebar
   - Organized by today and previous 7 days
   - Click any history item to reload past memes
   - Delete individual memes with the trash icon
   - Clear all history with one click
   - Local storage ensures your history persists
   - Hover interactions for easy management

4. **Profile & Settings**
   - Access your profile page
   - View your meme creation history
   - Manage your account settings

## Technical Details

### Frontend
- HTML5, CSS3 (Tailwind CSS)
- JavaScript (Vanilla JS)
- Dynamic animations and transitions
- Responsive layout design
- Local storage for meme history

### Backend
- Flask web framework
- Google Generative AI (Gemini 1.5 Pro)
- Image generation APIs
- User authentication system
- Session management

### Security
- Secure password handling
- Protected API endpoints
- Session-based authentication
- Input validation and sanitization

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Generative AI for Gemini 1.5 Pro
- ClipDrop API for image generation
- Stability AI for additional image processing
- The Flask team for the awesome framework
- Tailwind CSS for the styling utilities
