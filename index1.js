const request = require('request');



var req = {
    url: 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql',
  method: 'POST',
  headers: { "Content-Type": "application/graphql" },
  body: `{

    stop(id: "HSL:1201602") {
              gtfsId
                name
                stoptimesWithoutPatterns {
    scheduledArrival
    realtimeArrival
    arrivalDelay
    scheduledDeparture
    realtimeDeparture
    departureDelay
    realtime
    realtimeState
    serviceDay
    headsign
  }
                desc
                url
                vehicleMode


        }
    }`
};


request(req, function (error, response, body) {
  if (!error && response.statusCode == 200) {
    console.log(JSON.stringify(JSON.parse(body), null, 4));
  }
});
