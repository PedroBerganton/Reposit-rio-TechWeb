def extract_route (string):
    cont = 0
    resp = ""
    for l in string:
        if l == '/' and cont == 0:
            cont += 1
        elif cont > 0 and l != " ":
            resp = resp + l
        elif  cont > 0 and l == ' ':
            break
    return  resp.strip()

from pathlib import Path

def read_file(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
    return content

import json
import os

def load_data(file_name):
    file_path = os.path.join("data", file_name)

    with open(file_path, "r") as file:
        data = json.load(file)
    return data
      
def load_template(template_name):
    template_path = os.path.join("templates", template_name)
    with open(template_path, "r", encoding="utf-8") as file:
        template_content = file.read()
    return template_content

def save_data(lista):
    with open('data/notes.json', 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)


def add_annotation_to_notes(nova_anotacao):
    notes_data = load_data('notes.json')

    notes_data.append(nova_anotacao)
    save_data(notes_data)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers:
        response = f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'
    else:
        response = f'HTTP/1.1 {code} {reason}\n\n{body}'
    return response.encode()