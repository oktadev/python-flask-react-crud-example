function getJSONRepos(query) {
  return fetch('https://api.github.com/search/repositories?q=' + query).then(response => response.json());
}

export default getJSONRepos;
