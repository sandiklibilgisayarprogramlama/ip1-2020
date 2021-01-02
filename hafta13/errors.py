from app import app

@app.errorhandler(404)
def error_404(e):
    """404 için genel tema sayfası

    Args:
        e ([type]): [description]

    Returns:
        [type]: [description]
    """
    return render_template("404.html"),404