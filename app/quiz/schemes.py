from marshmallow import Schema, fields, ValidationError


def validate_answer(answers: list):
    count_true_ans = 0
    count_ans = 0
    for answer in answers:
        if answer["is_correct"]:
            count_true_ans += 1
        if count_true_ans > 1:
            raise ValidationError("Больше одного правильного ответа.")
        count_ans += 1
    if count_true_ans == 0:
        raise ValidationError("Ни одного правильного ответа.")
    if count_ans < 2:
        raise ValidationError("У вопроса только один ответ.")


class ThemeSchema(Schema):
    id = fields.Int(required=False)
    title = fields.Str(required=True)


class QuestionSchema(Schema):
    id = fields.Int(required=False)
    title = fields.Str(required=True)
    theme_id = fields.Int(required=True)
    answers = fields.Nested("AnswerSchema", many=True, required=True, validate=validate_answer)


class AnswerSchema(Schema):
    title = fields.Str(required=True)
    is_correct = fields.Bool(required=True)


class ThemeListSchema(Schema):
    themes = fields.Nested(ThemeSchema, many=True)


class ThemeIdSchema(Schema):
    theme_id = fields.Int()


class ListQuestionSchema(Schema):
    questions = fields.Nested(QuestionSchema, many=True)
