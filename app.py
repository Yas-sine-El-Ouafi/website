from flask import Flask, render_template,send_file
import json
import os

import requests, jsonify

# create flask app
app = Flask(__name__)
GITHUB_USERNAME = 'Yas-sine-El-Ouafi'

def get_projects():
    file_path = os.path.join('api','static', 'assets', 'projects.json')
    with open(file_path, 'r') as file:
            projects = json.load(file)
    return projects['projects']


@app.errorhandler(Exception)
def handle_exception(message):
    return render_template('error.html', message="Bad Request"), 400


@app.errorhandler(404)
def err_404(message):
    return render_template('error.html', message='404 Page Not Found'), 404


@app.route('/')
def main_page():
    return render_template('index.html', title='Yassine El Ouafi - Portfolio')


@app.route('/home')
def home():
    return render_template('base.html', title='Base')

@app.route('/about')
def about_page():
    return render_template('about.html', title="About")

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    return render_template('contact.html', title='Contact Page')

@app.route('/contact2', methods=['GET', 'POST'])
def contact_page2():
    return render_template('contact2.html', title='Contact Page')

@app.route('/projects', methods=['GET', 'POST'])
def projects_page():
    github_url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    headers = {
        'Authorization': f'token {env.GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    try:
        # Fetch GitHub repos
        response = requests.get(github_url, headers=headers)

        # Check if API call was successful
        if response.status_code == 200:
            repos = response.json()
            print(f"Fetched {len(repos)} repositories")  # Debugging: Check number of repos
            return render_template('projects.html', repos=repos)
        else:
            error_info = response.json()
            return jsonify({
                'error': 'Failed to fetch repositories',
                'status_code': response.status_code,
                'message': error_info.get('message', 'Unknown error'),
                'documentation_url': error_info.get('documentation_url')
            }), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'API request failed', 'message': str(e)}), 500

@app.route('/resume')
def resume():
    return send_file("static/assets/xx.pdf", as_attachment=False)

if __name__=='__main__':
    app.run()