#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the first command-line argument
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a GET request to the Star Wars API to fetch the movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body to JSON
  const movieData = JSON.parse(body);

  // Get the list of character URLs from the movie data
  const characters = movieData.characters;

  // For each character URL, make a request to fetch the character's name
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      // Parse the character data and print the name
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
