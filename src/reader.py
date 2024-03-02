import json


class Reader():
    """
    Class for receiving question/answer fields

    Attributes
    ----------
    file_name : str
        The name of the file containing the questions and answers.
    """

    def __init__(self, file_name: str) -> None:
        """
        Parameters
        ----------
        file_name : str
            The name of the file containing the questions and answers.
        """

        self.file_name = file_name

    def questions(self):
        """ Returns the question.

        Yields
        ------
        str
            The next line with a question that was contained in the file.
        """

        with open(self.file_name, 'r') as f:
            tmp: dict = json.load(f)
            questions = tmp.get('questions', None)
            if questions:
                for i in range(len(questions)):
                    yield questions[i]

    def answers(self):
        """ Returns the answers.

        Yields
        ------
        list
            Another list with the answers contained in the file.
        """

        with open(self.file_name, 'r') as f:
            tmp: dict = json.load(f)
            answers = tmp.get('answers', None)
            if answers:
                for i in range(len(answers)):
                    yield answers[i]
