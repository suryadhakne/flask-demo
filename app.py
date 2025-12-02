"""Flask demo application with healthz endpoint."""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/healthz')
def healthz():
    """Health check endpoint.
    
    Returns:
        JSON response with health status and HTTP 200 status code.
    """
    return jsonify({
        'status': 'healthy',
        'message': 'Service is running'
    }), 200


@app.route('/')
def index():
    """Root endpoint.
    
    Returns:
        JSON response with welcome message.
    """
    return jsonify({
        'message': 'Welcome to Flask Demo API'
    }), 200


if __name__ == '__main__':
    # Note: This is for development only. 
    # Use a production WSGI server (e.g., gunicorn) in production.
    import os
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(host=host, port=port, debug=debug)
