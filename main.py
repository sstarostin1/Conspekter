from flask import Flask, render_template, request, jsonify
import os
import logging

from conspecter.stt.stt_service import STTService

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

stt_service = None

@app.before_request
def initialize_services():
    global stt_service
    if stt_service is None:
        stt_service = STTService.get_instance()
        try:
            logger.info("Попытка инициализации STT сервиса...")
        except Exception as e:
            logger.warning(f"STT сервис не может быть инициализирован: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stt')
def stt_page():
    return render_template('stt.html')

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'running',
        'project': 'Conspekter - Intelligent Lecture Transcription System',
        'version': '0.2.0'
    })

@app.route('/api/stt/status', methods=['GET'])
def stt_status():
    if stt_service:
        return jsonify(stt_service.get_status())
    return jsonify({
        'initialized': False,
        'ready': False,
        'error': 'STT service not initialized'
    })

@app.route('/api/stt/devices', methods=['GET'])
def stt_devices():
    if stt_service:
        devices = stt_service.get_available_devices()
        return jsonify({
            'success': True,
            'devices': devices
        })
    return jsonify({
        'success': False,
        'devices': [],
        'error': 'STT service not initialized'
    })

@app.route('/api/stt/initialize', methods=['POST'])
def stt_initialize():
    global stt_service
    try:
        if stt_service is None:
            stt_service = STTService.get_instance()
        
        stt_service.initialize()
        
        return jsonify({
            'success': True,
            'message': 'STT сервис успешно инициализирован',
            'status': stt_service.get_status()
        })
    except FileNotFoundError as e:
        logger.warning(f"Модель не найдена: {e}")
        return jsonify({
            'success': False,
            'error': str(e),
            'remediation': 'Запустите: python scripts/prepare_whisper_model.py --model base --output models/whisper-base-int8'
        }), 404
    except Exception as e:
        logger.error(f"Ошибка инициализации STT: {e}", exc_info=True)
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    if not stt_service or not stt_service.is_ready():
        return jsonify({
            'success': False,
            'error': 'STT сервис не инициализирован. Пожалуйста, сначала инициализируйте сервис.'
        }), 400
    
    if 'audio' not in request.files:
        return jsonify({
            'success': False,
            'error': 'Аудиофайл не найден в запросе'
        }), 400
    
    audio_file = request.files['audio']
    
    if audio_file.filename == '':
        return jsonify({
            'success': False,
            'error': 'Имя файла пустое'
        }), 400
    
    try:
        language = request.form.get('language', 'ru')
        device = request.form.get('device')
        
        audio_bytes = audio_file.read()
        
        result = stt_service.transcribe_file(
            audio_bytes,
            language=language,
            device=device
        )
        
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Ошибка транскрибации: {e}", exc_info=True)
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
