from marshmallow import Schema, fields

class GithubRepoSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str()
    language = fields.Str()
    description = fields.Str()
    html_url = fields.URL()

class KudoSchema(GithubRepoSchema):
    user_id = fields.Email(required=True)
