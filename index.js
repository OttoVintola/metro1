const request = require('request');



var req = {
    url: 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql',
  method: 'POST',
  headers: { "Content-Type": "application/graphql" },
  body: `{
          routes(name: "", transportModes: SUBWAY) {
              gtfsId
              patterns {
                  directionId
                  name
                  headsign
        }
              shortName
              longName
              mode

      }
    }`
};


request(req, function (error, response, body) {
  if (!error && response.statusCode == 200) {
    console.log(JSON.stringify(JSON.parse(body), null, 4));
  }
});
