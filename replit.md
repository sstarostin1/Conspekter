# Conspekter - Intelligent Lecture Transcription System

## Overview
Conspekter is an intelligent system for automatic lecture transcription with conversion to structured LaTeX documents. The project is focused on physics and mathematics disciplines and works in real-time.

**Current State**: This is an initial implementation imported from GitHub. The repository originally contained only documentation (README and LICENSE), so a basic web interface has been created to demonstrate the project concept.

## Recent Changes
- **November 2, 2025**: STT Module Implementation
  - ✅ Implemented full STT (Speech-to-Text) module with OpenVINO Whisper
  - ✅ Added support for NPU/GPU/CPU hardware acceleration with automatic device selection
  - ✅ Created web interface for STT testing (/stt)
  - ✅ Implemented audio preprocessing (resampling, normalization)
  - ✅ Added model preparation script for Whisper quantization
  - ✅ Created REST API for transcription
  - ✅ Added configuration management system
  
- **November 2, 2025**: Initial Replit setup
  - Created basic Flask web application
  - Set up project structure with templates and static files
  - Configured workflow to run on port 5000
  - Added Python dependencies (Flask, Werkzeug)

## Project Structure
```
.
├── main.py                          # Flask application entry point
├── requirements.txt                 # Python dependencies
├── config.yaml                      # Configuration file
├── STT_SETUP.md                     # STT setup guide
├── conspecter/                      # Main package
│   ├── core/
│   │   └── config_manager.py        # Configuration management
│   ├── stt/
│   │   ├── audio_processor.py       # Audio preprocessing
│   │   ├── stt_service.py          # Main STT service
│   │   └── engines/
│   │       └── whisper_openvino.py  # Whisper engine with OpenVINO
│   └── interfaces/
│       └── api/                     # API interfaces
├── scripts/
│   └── prepare_whisper_model.py    # Model preparation script
├── templates/
│   ├── index.html                  # Main web interface
│   └── stt.html                    # STT testing page
├── static/
│   ├── css/
│   │   └── style.css               # Styling
│   └── js/
│       └── app.js                  # Client-side JavaScript
├── README.md                       # Original project documentation (Russian)
└── LICENSE                         # MIT License
```

## Architecture
The system is built on modular architecture:
- **core/** - ✅ System core (config manager)
- **stt/** - ✅ Speech recognition module (IMPLEMENTED)
  - Audio processor with librosa
  - Whisper OpenVINO engine
  - STT service with device management
- **nlp/** - 🔜 Natural language processing (planned)
- **latex/** - 🔜 LaTeX document generation (planned)
- **interfaces/** - ✅ Web and API interfaces

## Key Features
1. **Speech Recognition (STT)** ✅ IMPLEMENTED
   - ✅ Whisper model with OpenVINO optimization
   - ✅ INT4/INT8/FP16 quantization support
   - ✅ NPU/GPU/CPU hardware acceleration
   - ✅ Automatic device selection
   - ✅ Audio preprocessing (resampling to 16kHz, normalization)
   - ✅ Support for multiple languages (Russian, English, etc.)

2. **Intelligent Processing**
   - Semantic structuring
   - Mathematical parsing
   - Contextual correction
   - Key concept extraction

3. **LaTeX Generation**
   - Automatic formatting
   - Dynamic environments
   - Optimized output
   - Custom style support

## Technology Stack
- **Backend**: Python 3.11, Flask 3.0
- **AI/ML**: OpenVINO 2025.0+, OpenVINO GenAI, Whisper
- **Audio Processing**: librosa, soundfile
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Replit (development server on port 5000)

## Running the Project
The web interface runs automatically via the configured workflow:
- **Development**: `python main.py` (runs on 0.0.0.0:5000)
- **Access**: The web preview is available in Replit's webview

## API Endpoints
- `GET /` - Main web interface
- `GET /stt` - STT testing page
- `GET /api/status` - System status check
- `GET /api/stt/status` - STT service status
- `GET /api/stt/devices` - Available OpenVINO devices
- `POST /api/stt/initialize` - Initialize STT service and load model
- `POST /api/transcribe` - Transcribe audio file

## User Preferences
None recorded yet.

## Getting Started with STT

### Quick Start
1. Install model preparation dependencies:
   ```bash
   pip install optimum-intel
   ```

2. Prepare Whisper model:
   ```bash
   python scripts/prepare_whisper_model.py --model base --output models/whisper-base-int8
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Navigate to http://localhost:5000/stt to test STT

See `STT_SETUP.md` for detailed instructions.

### Hardware Optimization (Intel Ultra 7 255H)

Your system supports:
- **NPU**: Intel AI Boost (13 TOPS) - Best for real-time transcription
- **GPU**: Intel Arc 140T - Good for balanced performance/quality
- **CPU**: 96GB RAM - Supports large models

The system automatically selects the best available device.

## Notes
- ✅ STT module is fully implemented and ready to use
- The original GitHub repository contained only documentation
- NLP and LaTeX features are planned for future development
- The project documentation is primarily in Russian
