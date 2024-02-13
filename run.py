bind = "0.0.0.0:8080"  # Replace with your desired port
workers = 2  # Adjust the number of worker processes

# Optional: Logging configuration
loglevel = "info"
accesslog = "-"

# ... other configuration options

def app(environ, start_response):
    # Import your Flask app here
    from app import app

    return app(environ, start_response)
