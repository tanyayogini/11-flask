from flask import Flask, render_template
from utils import *

file_candidates_data = 'candidates.json'

app = Flask(__name__)
candidates = load_candidates_from_json(file_candidates_data)

# Представление главной страницы
@app.route('/')
def page_list():
    return render_template('list.html', candidates=candidates)


# Представление страницы отдельного кандидата
@app.route('/candidate/<int:candidate_id>/')
def page_candidate(candidate_id):
    candidate_info = get_candidate(candidates, candidate_id)
    return render_template('single.html', **candidate_info)


# Представление страницы с результатами поиска по имени кандидата
@app.route('/search/<candidate_name>/')
def page_search_by_name(candidate_name):
    candidates_by_name = get_candidates_by_name(candidates, candidate_name)
    number_candidates = len(candidates_by_name)
    return render_template('search.html', number_candidates=number_candidates, candidates_by_name=candidates_by_name)


# Представление страницы с результатами поиска кандидатов с конкретным навыком
@app.route('/skill/<skill_name>/')
def page_skill(skill_name):
    candidates_by_skill = get_candidates_by_skill(candidates, skill_name)
    number_candidates = len(candidates_by_skill)
    return render_template('skill.html', skill_name=skill_name, number_candidates=number_candidates, candidates_by_skill=candidates_by_skill)

app.run()