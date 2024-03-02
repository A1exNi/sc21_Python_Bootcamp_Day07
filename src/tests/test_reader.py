from reader import Reader
import json


def test_reader_questions():
    file_name = 'questions.json'
    with open(file_name, 'r') as f:
        dict_from_json = json.load(f)
    questions_from_json = dict_from_json.get('questions')
    reader = Reader(file_name)
    for question_from_reader, question_from_json in zip(
        reader.questions(),
        questions_from_json
    ):
        assert question_from_reader == question_from_json


def test_reader_answers():
    file_name = 'questions.json'
    with open(file_name, 'r') as f:
        dict_from_json = json.load(f)
    questions_from_json = dict_from_json.get('answers')
    reader = Reader(file_name)
    for question_from_reader, question_from_json in zip(
        reader.answers(),
        questions_from_json
    ):
        assert question_from_reader == question_from_json
