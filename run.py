# from app import create_app

# app = create_app()


# if __name__ == '__main__':
#     app.run(debug=True)

from app import create_app

app = create_app()

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Render assigns a dynamic port
    app.run(host='0.0.0.0', port=port)
