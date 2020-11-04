from ..repository import Repository
from ..repository.mongo import MongoRepository
from .schema import KudoSchema

class Service(object):
  def __init__(self, user_id, repo_client=Repository(adapter=MongoRepository)):
    self.repo_client = repo_client
    self.user_id = user_id

    if not user_id:
      raise Exception("user id not provided")

  def find_all_kudos(self):
    kudos  = self.repo_client.find_all({'user_id': self.user_id})
    return [self.dump(kudo) for kudo in kudos]

  def find_kudo(self, repo_id):
    kudo = self.repo_client.find({'user_id': self.user_id, 'repo_id': repo_id})
    return self.dump(kudo)

  def create_kudo_for(self, githubRepo):
    self.repo_client.create(self.prepare_kudo(githubRepo))
    return self.dump(githubRepo.data)

  def update_kudo_with(self, repo_id, githubRepo):
    records_affected = self.repo_client.update({'user_id': self.user_id, 'repo_id': repo_id}, self.prepare_kudo(githubRepo))
    return records_affected > 0

  def delete_kudo_for(self, repo_id):
    records_affected = self.repo_client.delete({'user_id': self.user_id, 'repo_id': repo_id})
    return records_affected > 0

  def dump(self, data):
    return KudoSchema(exclude=['_id']).dump(data).data

  def prepare_kudo(self, githubRepo):
    data = githubRepo.data
    data['user_id'] = self.user_id
    return data
