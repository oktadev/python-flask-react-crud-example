from flask_oidc import OpenIDConnect
from flask import Flask, json, g, request
from app.kudo.service import Service as Kudo
from app.kudo.schema import GithubRepoSchema
from flask_cors import CORS

app = Flask(__name__)
app.config.update({
  'OIDC_CLIENT_SECRETS': './client_secrets.json',
  'OIDC_RESOURCE_SERVER_ONLY': True
})
oidc = OpenIDConnect(app)
CORS(app)

@app.route("/kudos", methods=["GET"])
@oidc.accept_token(True)
def index():
  return json_response(Kudo(g.oidc_token_info['sub']).find_all_kudos())


@app.route("/kudos", methods=["POST"])
@oidc.accept_token(True)
def create():
  github_repo = GithubRepoSchema().load(json.loads(request.data))

  if github_repo.errors:
    return json_response({'error': github_repo.errors}, 422)

  kudo = Kudo(g.oidc_token_info['sub']).create_kudo_for(github_repo)
  return json_response(kudo)


@app.route("/kudo/<int:repo_id>", methods=["GET"])
@oidc.accept_token(True)
def show(repo_id):
  kudo = Kudo(g.oidc_token_info['sub']).find_kudo(repo_id)

  if kudo:
    return json_response(kudo)
  else:
    return json_response({'error': 'kudo not found'}, 404)


@app.route("/kudo/<int:repo_id>", methods=["PUT"])
@oidc.accept_token(True)
def update(repo_id):
  github_repo = GithubRepoSchema().load(json.loads(request.data))

  if github_repo.errors:
    return json_response({'error': github_repo.errors}, 422)

  kudo_service = Kudo(g.oidc_token_info['sub'])
  if kudo_service.update_kudo_with(repo_id, github_repo):
    return json_response(github_repo.data)
  else:
    return json_response({'error': 'kudo not found'}, 404)


@app.route("/kudo/<int:repo_id>", methods=["DELETE"])
@oidc.accept_token(True)
def delete(repo_id):
  kudo_service = Kudo(g.oidc_token_info['sub'])
  if kudo_service.delete_kudo_for(repo_id):
    return json_response({})
  else:
    return json_response({'error': 'kudo not found'}, 404)


def json_response(payload, status=200):
  return (json.dumps(payload), status, {'content-type': 'application/json'})
