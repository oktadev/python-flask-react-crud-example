from ..repository import Repository
from ..repository.mongo import MongoRepository
from .schema import KudoSchema

class Service(object):
  def __init__(self, user_id, repo=Repository(adapter=MongoRepository)):
    self.repo = repo
    self.user_id = user_id

    if not user_id:
      raise Exception("user id not provided")

  def find_all_kudos(self):
    kudos  = self.repo.find_all({'user_id': self.user_id})
    return [self.dump(kudo) for kudo in kudos]

  def find_kudo(self, repo_id):
    kudo = self.repo.find({'user_id': self.user_id, 'id': repo_id})
    return self.dump(kudo)

  def create_kudo_for(self, githubRepo):
    self.repo.create(self.prepare_kudo(githubRepo))
    return self.dump(githubRepo.data)

  def update_kudo_with(self, repo_id, githubRepo):
    updated_kudos = self.repo.update({'user_id': self.user_id, 'id': repo_id}, self.prepare_kudo(githubRepo))
    return updated_kudos > 0

  def delete_kudo_for(self, repo_id):
    deleted_kudos = self.repo.delete({'user_id': self.user_id, 'id': repo_id})
    return deleted_kudos > 0

  def dump(self, data):
    return KudoSchema(exclude=['_id']).dump(data).data

  def prepare_kudo(self, githubRepo):
    data = githubRepo.data
    data['user_id'] = self.user_id
    return data