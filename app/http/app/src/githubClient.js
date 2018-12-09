export default {
  getJSONRepos(query) {
    return fetch('https://api.github.com/search/repositories?q=' + query).then(response => response.json());
  },
  getJSONRepo(id) {
    return fetch('https://api.github.com/repositories/' + id).then(response => response.json())
  }
}