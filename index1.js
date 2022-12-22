const request = require('request');


// Get the data from GraphQL server
const req = {
  url: 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql',
  method: 'POST',
  headers: { "Content-Type": "application/graphql" },
  body: `{

    stop(id: "HSL:1201602") {
              gtfsId
                name
                stoptimesWithoutPatterns {
    realtimeArrival
    arrivalDelay
    realtimeDeparture
    departureDelay
    headsign
  }
                desc
                url
                vehicleMode


        }
    }`
};


// Turning GraphQL objects into JSON objects
request(req, function (error, response, body) {
  if (!error && response.statusCode == 200) {      // If there are no errors then print the data
    console.log(JSON.stringify(JSON.parse(body), null, 4));
  }
});
