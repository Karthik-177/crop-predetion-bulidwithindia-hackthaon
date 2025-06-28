from app import app

# Vercel expects a WSGI callable named "app"
# The Flask app instance is imported from app.py
# No need to call app.run() here, Vercel handles the server

if __name__ == "__main__":
    app.run()
