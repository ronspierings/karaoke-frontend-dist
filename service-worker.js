// General service worker properties
const CACHE_NAME = 'karaoke-cache-v1';
var urlsToCache = [
  '/',
  '/songlist.json',
  'https://localhost:4173/videos/Sister%20Sledge%20-%20We%20are%20family.mp4',
  'https://localhost:4173/videos/2-unlimited-nono.mp4'
  // Add other assets you want to cache here
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    // Fetch the songList JSON
    fetch("/songlist.json").then(function (res) {
      return res.json();
    })
    .then(function (songData) {
      // Loop through every song 
      for(let song of songData)
      {
        let songFilename = "/videos/" + song.songFilename;

        // Add this song to the Cache
        caches.open(CACHE_NAME).then((cache) => {
          console.info("Cache file:" + songFilename);
          return cache.add(songFilename)
        });
      }

      // Add all other files
      caches.open(CACHE_NAME).then((cache) => {
        return cache.addAll(urlsToCache);
      });
    })
  );  
});

self.addEventListener("fetch", (event) => {
  console.info("Fetch event", event.request);
  event.respondWith(
    caches.match(event.request).then((response) => {
      // caches.match() always resolves
      // but in case of success response will have value
      if (response !== undefined) {
        return response;
      } else {
        return fetch(event.request)
          .then((response) => {
            // response may be used only once
            // we need to save clone to put one copy in cache
            // and serve second one
            let responseClone = response.clone();

            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, responseClone);
            });
            return response;
          })
          .catch(() => caches.match("/gallery/myLittleVader.jpg"));
      }
    }),
  );
});


/*

self.addEventListener('install', (event) => {  

  // Cache all files in urlsToCache array
  event.waitUntil(

    // Fetch the songList JSON
    fetch("/songlist.json").then(function (res) {
      return res.json();
    })
    .then(function (songData) {
      debugger;
      // Loop through every song 
      for(let song of songData)
      {
        let songFilename = "/videos/" + song.songFilename;

        // Add this song to the Cache
        caches.open(CACHE_NAME).then((cache) => {
          console.info("Cache file:" + songFilename);
          return cache.add(songFilename)
        });
      }

      // Add all other files
      caches.open(CACHE_NAME).then((cache) => {
        return cache.addAll(urlsToCache);
      });
    })
  );
});

self.addEventListener('fetch', (event) => {

  event.respondWith(
    // Does the requested exist in the cache?
    caches.match(event.request).
    then((response) => {
      // debugger;
      if(response)
      {
        // Fetching from cache 
        console.info("Fetching from cache:", response.request)
        return response
      }

      console.info("Download - ", event.request)

      // Downloading from cache
      return fetch(event.request);
    })
  );
});

*/