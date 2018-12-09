import axios from 'axios';

const BASE_URI = 'http://localhost:4433';

const client = axios.create({
  baseURL: BASE_URI,
  json: true
});

class APIClient {
  
  constructor(accessToken) {
    this.accessToken = accessToken;
  }

  createKudo(repo) {
    return this.perform('post', '/kudos', repo);
  }

  deleteKudo(repo) {
    return this.perform('delete', `/kudos/${repo.id}`);
  }

  updateKudo(repo) {
    return this.perform('put', `/kudos/${repo.id}`, repo);
  }

  getKudos() {
    return this.perform('get', '/kudos');
  }

  getKudo(repo) {
    return this.perform('get', `/kudo/${repo.id}`);
  }

  async perform (method, resource, data) {
    return client({
      method,
      url: resource,
      data,
      headers: {
        Authorization: `Bearer ${this.accessToken}`
      }
    }).then(resp => {
      return resp.data ? resp.data : [];
    })
  }
}

export default APIClient;
