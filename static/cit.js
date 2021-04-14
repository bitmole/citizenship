const QUESTIONS_URL = '/random-test.json';

async function init() {
  console.log('caching questions');
  const cache = await caches.open('cit-cache');
  return cache.add(QUESTIONS_URL);
}

async function next() {
  // grab next question from cache
  let cache = await caches.open('cit-cache');
  let response = await cache.match(QUESTIONS_URL);
  let questions = await response.json();
  let next = questions.shift();
  console.log(`next: ${next}`);

  if (!next) return; // we're done, no more questions

  // replace cache with rest of questions
  const options = {
    headers: {
      'Content-Type': 'application/json'
    }
  }
  cache = await caches.open('cit-cache');
  cache.put(QUESTIONS_URL, new Response(JSON.stringify(questions), options));
  
  return `/questions/${next}/`;
}

function create_next_link(url, container_id, text) {
  let a = document.createElement('a');
  if (url) {
      a.href = url;
      a.textContent = text || 'Next Question';
  } else {
      a.href = '/finish/';
      a.textContent = 'Done! View Your Results.';
  }
  
  let container = document.getElementById(container_id);
  container.appendChild(a);
}

export { init, next, create_next_link }
