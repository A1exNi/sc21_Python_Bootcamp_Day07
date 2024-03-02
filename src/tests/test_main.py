import pytest
from main import main


def gen_str(inputs):
    for input in inputs:
        yield input


@pytest.mark.parametrize('inputs, result', [
    ([
        'questions.json',
        '1', '15', '79', '5', '4',
        '1', '14', '90', '2', '4',
        '1', '16', '85', '2', '4',
        '1', '12', '30', '2', '4',
        '1', '13', '70', '2', '4',
        '1', '14', '70', '2', '4',
        '1', '14', '70', '2', '4',
        '1', '15', '70', '2', '4',
        '1', '14', '70', '2', '4',
        '1', '14', '70', '2', '9'
    ], 'human'), ([
        'questions.json',
        '1', '15', '79', '5', '4',
        '1', '14', '90', '2', '1',
        '1', '16', '85', '2', '4',
        '1', '12', '30', '2', '4',
        '1', '13', '70', '2', '4',
        '1', '14', '70', '2', '4',
        '1', '14', '70', '2', '4',
        '1', '15', '70', '2', '4',
        '1', '11', '70', '2', '4',
        '1', '14', '70', '2', '9'
    ], 'replicant')
])
def test_main(monkeypatch, inputs, result, capsys):
    gen = gen_str(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(gen))
    main()
    captured = capsys.readouterr()
    assert captured.out.rsplit('\n', 2)[1] ==\
        f"test subject's is {result}".upper()


@pytest.mark.parametrize('inputs, result', [
    (['questions.json', 'asdf', 'exit'], '\tInvalid input. Try again.'),
    (['questions.json', '1', 'asdf', 'exit'], (
        '\tIncorrect breathing readings. The value must be '
        'a positive floating point number not greater than 120. '
        'Try again.'
    )),
    (['questions.json', '1', '1', '1', 'exit'], (
        '\tIncorrect heartbeat readings. The value must be a positive '
        'number between 30 and 200. Try again.'
    )),
    (['questions.json', '1', '1', '30', '6', 'exit'], (
        '\tIncorrect redness readings. The value must be between '
        '0 and 5. Try again.'
    )),
    (['questions.json', '1', '1', '30', '5', '16', 'exit'], (
        '\tIncorrect pupil readings. The value must be integer between '
        '1 and 15. Try again.'
    ))
])
def test_main_viewer_print_error(monkeypatch, inputs, result, capsys):
    gen = gen_str(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(gen))
    main()
    captured = capsys.readouterr()
    assert captured.out.rsplit('\n', 3)[1] == result


@pytest.mark.parametrize('inputs, result', [
    (
        ['reader.py', 'exit'],
        'Invalid file format specified or empty file. Try again.\n'
    ),
    (['asdf', 'exit'], 'File does not exist. Try again.\n')
])
def test_main_viewer_print_error_2(monkeypatch, inputs, result, capsys):
    gen = gen_str(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(gen))
    main()
    captured = capsys.readouterr()
    assert captured.out == result
