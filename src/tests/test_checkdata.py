import pytest
from checkdata import CheckData


@pytest.mark.parametrize('args, result', [
    ('questions1.json', CheckData.ErrorCheckData.FILE_DOES_NOT_EXIST),
    ('tests', CheckData.ErrorCheckData.FILE_DOES_NOT_EXIST),
    ('exit', CheckData.ErrorCheckData.EXIT),
    ('questions.json', CheckData.ErrorCheckData.NO_ERROR),
    ('requirement.txt', CheckData.ErrorCheckData.INVALID_FILE),
    ('questionstest.json', CheckData.ErrorCheckData.INVALID_FILE),
    ('questionstest2.json', CheckData.ErrorCheckData.INVALID_FILE),
    ('questionstest3.json', CheckData.ErrorCheckData.INVALID_FILE)
])
def test_check_data_check_file(args, result):
    check = CheckData()
    check.check_file(args)
    assert check.error == result


@pytest.mark.parametrize('args, result', [
    ('1', CheckData.ErrorCheckData.NO_ERROR),
    ('2', CheckData.ErrorCheckData.NO_ERROR),
    ('3', CheckData.ErrorCheckData.NO_ERROR),
    ('4', CheckData.ErrorCheckData.NO_ERROR),
    ('asdf', CheckData.ErrorCheckData.INVALID_INPUT),
    ('0', CheckData.ErrorCheckData.INVALID_INPUT),
    ('5', CheckData.ErrorCheckData.INVALID_INPUT),
    ('exit', CheckData.ErrorCheckData.EXIT),
])
def test_check_data_check_answer(args, result):
    check = CheckData()
    check.check_answer(args)
    assert check.error == result


@pytest.mark.parametrize('args, result', [
    ('asdf', CheckData.ErrorCheckData.INVALID_RESPIRATION),
    ('0', CheckData.ErrorCheckData.NO_ERROR),
    ('120', CheckData.ErrorCheckData.NO_ERROR),
    ('10.123', CheckData.ErrorCheckData.NO_ERROR),
    ('-10.02', CheckData.ErrorCheckData.INVALID_RESPIRATION),
    ('exit', CheckData.ErrorCheckData.EXIT)
])
def test_check_data_check_respiration(args, result):
    check = CheckData()
    check.check_respiration(args)
    assert check.error == result


@pytest.mark.parametrize('args, result', [
    ('asdf', CheckData.ErrorCheckData.INVALID_HEART_RATE),
    ('0', CheckData.ErrorCheckData.INVALID_HEART_RATE),
    ('-60', CheckData.ErrorCheckData.INVALID_HEART_RATE),
    ('300', CheckData.ErrorCheckData.INVALID_HEART_RATE),
    ('120', CheckData.ErrorCheckData.NO_ERROR),
    ('10.123', CheckData.ErrorCheckData.INVALID_HEART_RATE),
    ('-10.02', CheckData.ErrorCheckData.INVALID_HEART_RATE),
    ('exit', CheckData.ErrorCheckData.EXIT)
])
def test_check_data_check_heart_rate(args, result):
    check = CheckData()
    check.check_heart_rate(args)
    assert check.error == result


@pytest.mark.parametrize('args, result', [
    ('asdf', CheckData.ErrorCheckData.INVALID_BLUSHING_LEVEL),
    ('0', CheckData.ErrorCheckData.NO_ERROR),
    ('-60', CheckData.ErrorCheckData.INVALID_BLUSHING_LEVEL),
    ('5', CheckData.ErrorCheckData.NO_ERROR),
    ('120', CheckData.ErrorCheckData.INVALID_BLUSHING_LEVEL),
    ('10.123', CheckData.ErrorCheckData.INVALID_BLUSHING_LEVEL),
    ('-10.02', CheckData.ErrorCheckData.INVALID_BLUSHING_LEVEL),
    ('exit', CheckData.ErrorCheckData.EXIT)
])
def test_check_data_check_blushing_level(args, result):
    check = CheckData()
    check.check_blushing_level(args)
    assert check.error == result


@pytest.mark.parametrize('args, result', [
    ('asdf', CheckData.ErrorCheckData.INVALID_PUPILLARY_DILATION),
    ('0', CheckData.ErrorCheckData.INVALID_PUPILLARY_DILATION),
    ('-60', CheckData.ErrorCheckData.INVALID_PUPILLARY_DILATION),
    ('5', CheckData.ErrorCheckData.NO_ERROR),
    ('1.2', CheckData.ErrorCheckData.INVALID_PUPILLARY_DILATION),
    ('15', CheckData.ErrorCheckData.NO_ERROR),
    ('10.123', CheckData.ErrorCheckData.INVALID_PUPILLARY_DILATION),
    ('-10.02', CheckData.ErrorCheckData.INVALID_PUPILLARY_DILATION),
    ('exit', CheckData.ErrorCheckData.EXIT)
])
def test_check_data_check_pupillary_dilation(args, result):
    check = CheckData()
    check.check_pupillary_dilation(args)
    assert check.error == result
