from checkdata import CheckData
from reader import Reader
from voightkampfftest import VoightKampffTest


class Viewer():
    """Console user interaction class.

    Attributes
    ----------
    file_name : str
        File name containing the question/answers.
    check_data : CheckData
        An object of the CheckData class that validates user input.
    test: VoightKampffTest
        An object of the class VoightKampffTest which produces the test result.
    reader : Reader
        An object of the class Reader that reads questions and answers
        from a file.
    """

    def __init__(self) -> None:
        self.file_name: str = None
        self.check_data = CheckData()
        self.test = VoightKampffTest()
        self.reader = Reader(self.file_name)

    def ask_file_name(self) -> str:
        """Asks the user for the name of the question and answer file."""

        file_name = self.repeatable_message(
            (
                'Enter the name of the questions and answers file '
                '(to exit, enter "exit"): '
            ),
            self.check_data.check_file
        )
        if self.check_data.error == CheckData.ErrorCheckData.NO_ERROR:
            self.file_name = file_name

    def test_begin(self) -> None:
        """Prints a message indicating the start of the test."""

        print((
            '========================'
            'Test has begun'
            '========================'
        ))

    def testing(self) -> None:
        """Displays a list of questions and answers and receives an answer
        option from the user.
        """

        self.reader = Reader(self.file_name)
        for question, answers in zip(
            self.reader.questions(),
            self.reader.answers()
        ):
            print(f'Question: {question}')
            print('\tAnswers:')
            for num, answer in enumerate(answers):
                print(f'\t\t{num+1}. {answer}')
            answer = self.repeatable_message(
                '\tEnter response number(to exit, enter "exit"): ',
                self.check_data.check_answer
            )
            if self.check_data.error == CheckData.ErrorCheckData.EXIT:
                break
            self.input_data_for_test()
            if self.check_data.error == CheckData.ErrorCheckData.EXIT:
                break

    def input_data_for_test(self):
        """Receives data on breathing, heart rate, redness and pupil dilation
        from the user.
        """

        respiration = self.repeatable_message(
            "Enter the subject's breathing readings(to exit, enter 'exit'): ",
            self.check_data.check_respiration
        )
        if self.check_data.error != CheckData.ErrorCheckData.EXIT:
            heart_rate = self.repeatable_message(
                (
                    "Enter the subject's heart rate readings"
                    "(to exit, enter 'exit'): "
                ),
                self.check_data.check_heart_rate
            )
        if self.check_data.error != CheckData.ErrorCheckData.EXIT:
            blushing_level = self.repeatable_message(
                (
                    "Enter the test subject's redness level(from 0 to 5) "
                    "reading(to exit, enter 'exit'): "
                ),
                self.check_data.check_blushing_level
            )
        if self.check_data.error != CheckData.ErrorCheckData.EXIT:
            pupillary_dilation = self.repeatable_message(
                (
                    "Enter the subject's pupil dilation reading(to exit, "
                    "enter 'exit'): "
                ),
                self.check_data.check_pupillary_dilation
            )
        if self.check_data.error != CheckData.ErrorCheckData.EXIT:
            self.test.add_respiration(float(respiration))
            self.test.add_heart_rate(int(heart_rate))
            self.test.add_blushing_level(int(blushing_level))
            self.test.add_pupillary_dilation(int(pupillary_dilation))

    def repeatable_message(self, message: str, check) -> str:
        """Repeatable message. Prompts the user for some data and verifies it.
        When you enter the word "exit", a stop occurs.

        Parameters
        ----------
        message : str
            Message displayed on the screen.
        check
            Function to check the entered value.

        Returns
        -------
        str
            The value entered by the user.

        """
        exit = False
        while not exit:
            answer = input(message)
            check(answer)
            if (
                self.check_data.error == CheckData.ErrorCheckData.NO_ERROR or
                self.check_data.error == CheckData.ErrorCheckData.EXIT
            ):
                exit = True
            else:
                self.print_error()
        return answer

    def print_error(self):
        """Displays a description of the error."""

        if self.check_data.error ==\
                CheckData.ErrorCheckData.FILE_DOES_NOT_EXIST:
            print('File does not exist. Try again.')
        elif self.check_data.error == CheckData.ErrorCheckData.INVALID_FILE:
            print('Invalid file format specified or empty file. Try again.')
        elif self.check_data.error == CheckData.ErrorCheckData.INVALID_INPUT:
            print('\tInvalid input. Try again.')
        elif self.check_data.error ==\
                CheckData.ErrorCheckData.INVALID_RESPIRATION:
            print((
                '\tIncorrect breathing readings. The value must be '
                'a positive floating point number not greater than 120. '
                'Try again.'
            ))
        elif self.check_data.error ==\
                CheckData.ErrorCheckData.INVALID_HEART_RATE:
            print((
                '\tIncorrect heartbeat readings. The value must be a positive '
                'number between 30 and 200. Try again.'
            ))
        elif self.check_data.error ==\
                CheckData.ErrorCheckData.INVALID_BLUSHING_LEVEL:
            print((
                '\tIncorrect redness readings. The value must be between '
                '0 and 5. Try again.'
            ))
        elif self.check_data.error ==\
                CheckData.ErrorCheckData.INVALID_PUPILLARY_DILATION:
            print((
                '\tIncorrect pupil readings. The value must be integer between'
                ' 1 and 15. Try again.'
            ))
        else:
            print('UNKNOWN ERROR')

    def test_end(self) -> None:
        """Prints a message indicating the completed of the test."""

        print((
            '========================'
            'Test completed'
            '========================'
        ))

    def print_result_test(self) -> None:
        """Displays the test result."""

        if self.check_data.error == CheckData.ErrorCheckData.NO_ERROR:
            test_subjects = self.test.get_result()
            print(f"test subject's is {test_subjects}".upper())
