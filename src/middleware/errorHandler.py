```python
from flask import jsonify

def handle_error(error):
    response = {
        "error": {
            "type": type(error).__name__,
            "message": str(error)
        }
    }
    return jsonify(response), 500

def init_app(app):
    app.register_error_handler(Exception, handle_error)
```