"""Module to define the document writer interface.

This interface is intended to define a single method (write) to write two documents:
    * Questions document: document for students to solve problems and give answers.
    * Solutions document: document for teachers with the correct answers for grades.

This interface aims to separate main processes to facilitate debugging.

Typical usage example:
    from writers.writer_interface import DocumentWriterInterface

    class SubjectExampleModuleN(DocumentWriterInterface):
        def __init__(self, conf: dict) -> None:
            ... # define all the logic
"""
from abc import ABC, abstractmethod


class DocumentWriterInterface(ABC):
    @abstractmethod
    def __init__(self, conf: dict) -> None:
        """Initializes variables.

        Args:
            conf (dict): configuration from a config file.
        """
        pass

    def write(self) -> None:
        """Creates docx files for questions (students) and solutions (teacher)."""
        self.compute_questions_and_answers()
        self.create_questions_document()
        self.create_solutions_document()

    @abstractmethod
    def compute_questions_and_answers() -> None:
        """Generates questions & answers data structures to be parsed in next steps."""
        pass

    @abstractmethod
    def create_questions_document(path: str) -> None:
        """Creates question document and saves it reporting the output path."""
        pass

    @abstractmethod
    def create_solutions_document(path: str) -> None:
        """Creates solutions document and saves it reporting the output path."""
        pass
