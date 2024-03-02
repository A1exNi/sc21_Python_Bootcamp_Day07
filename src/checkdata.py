import json
from enum import Enum


class CheckData():
    """
    The class is used to validate input data.

    Attributes
    ----------
    error : ErrorCheckData
        Stores the error type or absence thereof
    """

    class ErrorCheckData(Enum):
        """
        The enumeration class is used to identify possible errors.

        Attributes
        ----------
        NO_ERROR
            Indicates no error.
        EXIT
            Indicates that it has been entered 'exit'.
        INAVLID_FILE
            Indicates that an unsuitable, empty file or a file not
            containing the required fields was selected.
        FILE_DOES_NOT_EXIST
            Indicates that the file does not exist.
        INVALID_INPUT
            Indicates that the file contains an answer option that
            is in the wrong format or is outside the expected answer
            options.
        INVALID_RESPIRATION
            Indicates that incorrect respiration values have been entered.
        INVALID_HEART_RATE
            Indicates that incorrect heart rate values have been entered.
        INVALID_BLUSHING_LEVEL
            Indicates that incorrect blushing level values have been
            entered.
        INVALID_PUPILLARY_DILATION
            Indicates that incorrect pupillary dilation values have been
            entered.
        INVALID_INT_VALUE
            Indicates that the check for an integer failed.
        INVALID_FLOAT_VALUE
            Indicates that the check for a floating point number failed.
        """

        NO_ERROR = -1
        EXIT = 0
        INVALID_FILE = 1
        FILE_DOES_NOT_EXIST = 2
        INVALID_INPUT = 3
        INVALID_RESPIRATION = 4
        INVALID_HEART_RATE = 5
        INVALID_BLUSHING_LEVEL = 6
        INVALID_PUPILLARY_DILATION = 7
        INVALID_INT_VALUE = 8
        INVALID_FLOAT_VALUE = 9

    def __init__(self) -> None:
        self.error = self.ErrorCheckData.NO_ERROR

    def check_file(self, file_name: str) -> None:
        """ Checks whether the file exists, is in the required format
            and contains the required fields.

        Parameters
        ----------
        file_name : str
            The name of the file being checked.
        """

        if file_name == 'exit':
            self.error = self.ErrorCheckData.EXIT
        else:
            try:
                f = open(file_name, 'r')
                if (
                    self.allowed_file(file_name) and
                    not self.empty_file(f)
                ):
                    self.error = self.ErrorCheckData.NO_ERROR
                else:
                    self.error = self.ErrorCheckData.INVALID_FILE
                f.close()
            except (FileNotFoundError, IsADirectoryError):
                self.error = self.ErrorCheckData.FILE_DOES_NOT_EXIST

    def empty_file(self, file) -> bool:
        """Checks whether the file can be processed and whether it
        contains the required fields.

        Parameters
        ----------
        file : file object
            File to check.

        Returns
        -------
        bool
            Returns True if the file is empty or does not contain the
            required fields. False - otherwise.
        """

        answer = False
        try:
            tmp: dict = json.load(file)
            questions = tmp.get('questions', None)
            answers = tmp.get('answers', None)
            if not questions and not answers:
                answer = True
        except json.decoder.JSONDecodeError:
            answer = True
        return answer

    def allowed_file(self, file_name: str) -> bool:
        """Checks that the file is in json format.

        Parameters
        ----------
        file_name : str
            The name of the file being checked.

        Returns
        -------
        bool
            Returns True if the file is in json format. False - otherwise.
        """

        allowed = set(['json'])
        return '.' in file_name and \
            file_name.rsplit('.', 1)[1].lower() in allowed

    def check_answer(self, answer: str) -> None:
        """Checks the response value.

        Parameters
        ----------
        answer : str
            Checks that the entered answer is an integer from 1 to 4.
        """

        self.check_int_value(answer, 1, 4)
        if self.error == self.ErrorCheckData.INVALID_INT_VALUE:
            self.error = self.ErrorCheckData.INVALID_INPUT

    def check_respiration(self, respiration: str) -> None:
        """Checks the respiration value.

        Parameters
        ----------
        respiration: str
            Checks that the entered answer is an float from 0.0 to 120.0.
        """

        self.check_float_value(respiration, 0.0, 120.0)
        if self.error == self.ErrorCheckData.INVALID_FLOAT_VALUE:
            self.error = self.ErrorCheckData.INVALID_RESPIRATION

    def check_heart_rate(self, heart_rate: str) -> None:
        """Checks the heart rate value.

        Parameters
        ----------
        heart_rate : str
            Checks that the entered answer is an integer from 30 to 200.
        """

        self.check_int_value(heart_rate, 30, 200)
        if self.error == self.ErrorCheckData.INVALID_INT_VALUE:
            self.error = self.ErrorCheckData.INVALID_HEART_RATE

    def check_blushing_level(self, blushing_level: str) -> None:
        """Checks the blushing level value.

        Parameters
        ----------
        blushing_level : str
            Checks that the entered answer is an integer from 0 to 5.
        """

        self.check_int_value(blushing_level, 0, 5)
        if self.error == self.ErrorCheckData.INVALID_INT_VALUE:
            self.error = self.ErrorCheckData.INVALID_BLUSHING_LEVEL

    def check_pupillary_dilation(self, pupillary_dilation: str) -> None:
        """Checks the pupillary dilation value.

        Parameters
        ----------
        pupillary_dilation : str
            Checks that the entered answer is an integer from 1 to 15.
        """

        self.check_int_value(pupillary_dilation, 1, 15)
        if self.error == self.ErrorCheckData.INVALID_INT_VALUE:
            self.error = self.ErrorCheckData.INVALID_PUPILLARY_DILATION

    def check_int_value(
        self,
        value: str,
        min_value: int,
        max_value: int
    ) -> None:
        """Checks that the value is an integer and is in the range from
        min_value to max_value.

        Parameters
        ----------
        value : str
            Check value.
        min_value : int
            Minimum allowed value.
        max_value : int
            Maximum allowed value.
        """

        if value == 'exit':
            self.error = self.ErrorCheckData.EXIT
        else:
            try:
                if int(value) < min_value or int(value) > max_value:
                    self.error = self.ErrorCheckData.INVALID_INT_VALUE
                else:
                    self.error = self.ErrorCheckData.NO_ERROR
            except ValueError:
                self.error = self.ErrorCheckData.INVALID_INT_VALUE

    def check_float_value(
        self,
        value: str,
        min_value: float,
        max_value: float
    ) -> None:
        """Checks that the value is an floating point and is in the range from
        min_value to max_value.

        Parameters
        ----------
        value : str
            Check value.
        min_value : float
            Minimum allowed value.
        max_value : float
            Maximum allowed value.
        """

        if value == 'exit':
            self.error = self.ErrorCheckData.EXIT
        else:
            try:
                if float(value) < min_value or float(value) > max_value:
                    self.error = self.ErrorCheckData.INVALID_FLOAT_VALUE
                else:
                    self.error = self.ErrorCheckData.NO_ERROR
            except ValueError:
                self.error = self.ErrorCheckData.INVALID_FLOAT_VALUE
