import json


def load_candidates_from_json(filename):
    """Принимает имя файла json, возвращает данные файла в формате списка"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def get_candidate(candidates, candidate_id):
    """Принимает данные о кандидатах в формате списка словарей и id кандидата в формате int,
    возвращает словарь с информацией про кандидата с этим id"""

    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidates, candidate_name):
    """Принимает данные о кандидатах в формате списка словарей и имя кандидата в формате str,
    возвращает список с информацией о кандидатах с таким именем"""

    candidates_by_name = []
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            candidates_by_name.append(candidate)

    return candidates_by_name


def get_candidates_by_skill(candidates, skill_name):
    """Принимает информацию о кандидатах в формате списка и навык в формате str,
    возвращает информацию о кандидатах, у которых есть навык, в формате списка словарей"""

    candidates_by_skill = []
    for candidate in candidates:
        candidate_skills = candidate['skills'].lower().split(', ')
        for skill in candidate_skills:
            if skill == skill_name.lower():
                candidates_by_skill.append(candidate)
                break

    return candidates_by_skill
