/**
 * Copyright 2018, Google LLC
 * Licensed under the Apache License, Version 2.0 (the `License`);
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an `AS IS` BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
 
// [START gae_python38_log]
// [START gae_python3_log]

// TODO: Set up a leaflet map here, centred on somewhere in the top-of-the-south
var map = L.map('map').setView([-41, 174], 5);
var currentMarkers = [];

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map)

// We have a selection box on the main page which allows you to pick which 'dogsAllowed' value
// you want to get tracks for (e.g. Dogs on a leash only)        
const sb = document.querySelector('#dogsel')

// This sets up an event for when the selection box changes
sb.onchange = (event) => {
            event.preventDefault();
            // The value chosen is added to the dogValue variable
            var dogValue = sb[sb.selectedIndex].value;
            // The dogValue variable goes into the payload for the internal API
            var payload = {
              'key': 'dogsAllowed',
              'value': dogValue
            };
            // This fetch queries the internal API to find tracks using the payload above
            // to see how this works, go to main.py and look for the track_filter route
            fetch('/track_filter', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify(payload)
          })
          .then((response) => response.json())
          .then((data) => {
              console.log(data);
              
              var disp = document.getElementById('display');
              var strout = [];
              data.sort((a,b) => b.lat - a.lat)
              if (typeof currentMarkers !== "undefined") {
                console.log("Removing markers from map");
                currentMarkers.forEach(marker => {
                  marker.removeFrom(map);
                });
              }

              for (track of data) {
                
                // TODO: This line could be removed and replaced with a colour scheme or some other way of identifying which tracks are bikeable
                if (track.permittedActivities.includes('Mountain biking')) {
                  // TODO: This loop returns lat and lon for each track - set up leaflet markers for each point and add them to our map
                  strout.push(`${track['name']} ${track['lat']},${track['lon']} ${track.region}`);
                  var marker = L.marker([track.lat, track.lon]).addTo(map);
                  currentMarkers.push(marker);
                }
              }
              disp.innerHTML = `<pre>${strout.join("\r\n")}</pre>`;
              
          })
        };

  

        
       
// [END gae_python3_log]
// [END gae_python38_log]
