#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the first command-line argument
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Function to fetch a single character's name
const fetchCharacter = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
};

// Make a GET request to the Star Wars API to fetch the movie details
request(apiUrl, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body to JSON
  const movieData = JSON.parse(body);

  // Get the list of character URLs from the movie data
  const characters = movieData.characters;

  // Fetch and print each character name in order
  for (const characterUrl of characters) {
    try {
      const characterName = await fetchCharacter(characterUrl);
      console.log(characterName);
    } catch (err) {
      console.error(err);
    }
  }
});
