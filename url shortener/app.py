from flask import Flask, request, redirect, render_template
from models import (
    get_all_url, 
    get_url, 
    increment_visit_click_count, 
    delete_url_by_short_code, 
    init_db)
from functions import (create_short_url)

app = Flask(__name__)
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            original_url = request.form['original_url']
            
            if not original_url or create_short_url(original_url):
                return redirect('/')
        except Exception as e:
            return render_template('error.html', message = str(e))
    elif request.method == 'GET':
        try:
            all_urls = get_all_url()
            return render_template('index.html' , request = request, urls = all_urls)
        except Exception as e:
            return render_template('error.html', message = str(e) + ' - Unable to fetch URLs')

@app.route('/<short_code>')
def on_click(short_code):
    try:
        redirect_url = get_url(short_code)
        if redirect_url is None:
            return render_template('404.html')
        increment_visit_click_count(short_code)
        return redirect(redirect_url[0])
    except Exception as e:
        return render_template('error.html', message=str(e) + ' - Invalid Short URL')

@app.route('/delete/<short_code>', methods=['POST'])
def delete_url(short_code):
    if request.method == 'POST':
        delete_url_by_short_code(short_code)
        return redirect('/')
    else:
        return render_template('404.html')
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404