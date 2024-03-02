import pytest
from voightkampfftest import VoightKampffTest


@pytest.mark.parametrize(
    'respiration, heart_rate, blushing_level, pupillary_dilation, result', [
        (
            [15, 14, 16, 12, 13, 14, 15, 14, 11, 14],
            [79, 90, 85, 30, 70, 70, 70, 70, 70, 70],
            [5, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 9],
            'human'
        ), (
            [15, 14, 16, 12, 13, 14, 15, 14, 11, 14],
            [79, 90, 85, 30, 70, 70, 70, 70, 70, 70],
            [5, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [4, 1, 1, 4, 4, 4, 4, 4, 4, 9],
            'replicant'
        )
    ]
)
def test_testvoightkampff_get_result(
    respiration,
    heart_rate,
    blushing_level,
    pupillary_dilation,
    result
):
    test = VoightKampffTest()
    for resp, heart, blush, pup in zip(
        respiration,
        heart_rate,
        blushing_level,
        pupillary_dilation
    ):
        test.add_respiration(resp)
        test.add_heart_rate(heart)
        test.add_blushing_level(blush)
        test.add_pupillary_dilation(pup)
    answer = test.get_result()
    assert answer == result
