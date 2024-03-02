from enum import Enum


class VoightKampffTest():
    """
    Voight-Kampff Test`s.

    Attributes
    ----------
    respiration : list
        List of respiration value.
    heart_rate : list
        List of heart rate value.
    blushing_level : list
        List of blushing level value.
    pupillary_dilation : list
        List of pupillary dilation value.
    """

    class Blushing(Enum):
        """The enumeration class is used to identify blushing."""

        NO_BLUSHING = 0
        SLIGHT_BLUSHING = 1
        ABOVE_SLIGHT_BLUSHING = 2
        MEDIUM_BLUSHING = 3
        ABOVE_MEDIUM_BLUSHING = 4
        HIGH_BLUSHING = 5

    def __init__(self) -> None:
        self.respiration = list()
        self.heart_rate = list()
        self.blushing_level = list()
        self.pupillary_dilation = list()

    def add_respiration(self, respiration: float) -> None:
        """Adds a respiration value to the list.

        Parameters
        ----------
        respiration : str
            The value of respiration.
        """

        self.respiration.append(respiration)

    def add_heart_rate(self, heart_rate: int) -> None:
        """Adds a heart rate value to the list.

        Parameters
        ----------
        heart_rate : str
            The value of heart rate.
        """

        self.heart_rate.append(heart_rate)

    def add_blushing_level(self, blushing_level: Blushing) -> None:
        """Adds a blushing level value to the list.

        Parameters
        ----------
        blushing_level : str
            The value of blushing level.
        """

        self.blushing_level.append(blushing_level)

    def add_pupillary_dilation(self, pupillary_dilation: int) -> None:
        """Adds a pupillary dilation value to the list.

        Parameters
        ----------
        pupillary_dilation : str
            The value of pupillary dilation.
        """

        self.pupillary_dilation.append(pupillary_dilation)

    def get_result(self) -> str:
        """Defines and returns the test result.

        Returns
        -------
        str
            Returns the message "human" or "replicant"
        """

        answers = []
        for respiration, heart_rate, blushing_level, pupillary_dilation in zip(
            self.respiration,
            self.heart_rate,
            self.blushing_level,
            self.pupillary_dilation
        ):
            answer = self.is_human_value(
                respiration,
                heart_rate,
                blushing_level,
                pupillary_dilation
            )
            for val in answer:
                answers.append(val)
        number_answers = len(answers)
        sum_answers = sum(answers)
        coefficient: float = sum_answers/number_answers
        print(number_answers)
        if coefficient >= 0.9:
            return 'human'
        else:
            return 'replicant'

    def is_human_value(
        self,
        respiration: float,
        heart_rate: int,
        blushing_level: Blushing,
        pupillary_dilation: int
    ):
        """Determines whether the transmitted readings are acceptable for
        a person.

        Parameters
        ----------
        respiration : float
            The value of respiration.
        heart_rate: int
            The value of heart rate.
        blushing_level: Blushing
            The value of blushing level.
        pupillary_dilation: int
            The value of pupillary dilation.
        """

        resp_is_normal = False
        if respiration >= 12.0 and respiration <= 16.0:
            resp_is_normal = True
        heart_is_normal = False
        if heart_rate >= 60 and heart_rate <= 100:
            heart_is_normal = True
        blushing_is_normal = False
        if blushing_level >= 2 and blushing_level <= 4:
            blushing_is_normal = True
        pupillary_is_normal = False
        if pupillary_dilation >= 2 and pupillary_dilation <= 8:
            pupillary_is_normal = True
        return (
            resp_is_normal,
            heart_is_normal,
            blushing_is_normal,
            pupillary_is_normal
        )
