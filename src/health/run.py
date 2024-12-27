
"""
Basic entry/setup point with `main` fucntion.
"""
def main():
    from .app import app
    from .callbacks import register_callbacks

    register_callbacks(app)    
    app.run_server(debug=True)

if __name__ == "__main__":
    main()
