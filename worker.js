/* Local Memory Interception Protocol */

const memoryStorageName = 'visual-asset-archive-version-one';
const visualExtensions = ['.jpg', '.jpeg', '.png', '.webp', '.svg'];

// Execute immediate installation
self.addEventListener('install', (event) => {
    self.skipWaiting();
});

// Intercept outgoing network requests
self.addEventListener('fetch', (event) => {
    const requestAddress = event.request.url;
    
    // Mathematically verify if the target file is a visual asset
    const isVisualAsset = visualExtensions.some(extension => requestAddress.toLowerCase().endsWith(extension));

    if (isVisualAsset) {
        event.respondWith(
            caches.match(event.request).then((cachedResponse) => {
                // Return the asset instantaneously from local memory if it exists
                if (cachedResponse) {
                    return cachedResponse; 
                }
                
                // If it does not exist, retrieve it from the network and securely store a duplicate
                return fetch(event.request).then((networkResponse) => {
                    return caches.open(memoryStorageName).then((storage) => {
                        storage.put(event.request, networkResponse.clone());
                        return networkResponse;
                    });
                });
            })
        );
    }
});