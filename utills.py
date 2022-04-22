import  json

def get_candidates(path):
    with open(path, 'r', encoding='utf-8') as candidates:
        return json.load(candidates)

def format_candidates(candidates_list):
    result = '<pre>'
    for candidate in candidates_list:
        result += (
            f'Имя кандидата - {candidate["name"]}\n'
            f'Позиция кандидата - {candidate["position"]}\n'
            f'Навыки кандидата - {candidate["skills"]}\n\n'
        )
    result = '<pre>'
    return result

def get_candidate_by_id(candidates_list, candidate_id):
    candidate_id = int(candidate_id)
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate

def get_candidates_by_skill(candidates_list, candidate_sill):
    result = []
    for candidate in candidates_list:
        candidate_sills = candidate['skills'].lower().split(', ')
        if candidate_sill.lower() in candidate['skill']:
            result.append(candidate)
    return result
