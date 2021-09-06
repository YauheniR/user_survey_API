from enum import Enum


class QuestionTypeEnum(Enum):
    TEXT_RESPONSE = "TR"
    ONE_CHOICE = "OC"
    SEVERAL_CHOICE = "SC"

    QUESTION_TYPE_CHOICES = (
        (TEXT_RESPONSE, 'Answer with a text'),
        (ONE_CHOICE, 'Choice of one options'),
        (SEVERAL_CHOICE, 'Answer with a choice of several options'),
    )
