const CACHE = "jerga-de-obra-v6";
const ASSETS = [
  "./",
  "./index.html",
  "./phrases.js",
  "./manifest.json",
  "./icon.png",
  "./icon-512.png",
  "./icon-maskable.png",
  "./apple-touch-icon.png",
  "./sw.js",
  "./images/ac-unit.webp",
  "./images/air-filter.webp",
  "./images/breaker.webp",
  "./images/brick.webp",
  "./images/bulldozer.webp",
  "./images/cable.webp",
  "./images/caster.webp",
  "./images/cement.webp",
  "./images/circular-saw.webp",
  "./images/concrete.webp",
  "./images/condenser.webp",
  "./images/copper.webp",
  "./images/crane.webp",
  "./images/drain.webp",
  "./images/drill.webp",
  "./images/drywall.webp",
  "./images/duct.webp",
  "./images/dump-truck.webp",
  "./images/electrical-tape.webp",
  "./images/electrode.webp",
  "./images/evaporator.webp",
  "./images/excavator.webp",
  "./images/extension-cord.webp",
  "./images/forklift.webp",
  "./images/formwork.webp",
  "./images/gas-cylinder.webp",
  "./images/gravel.webp",
  "./images/grinder.webp",
  "./images/guardrail.webp",
  "./images/hammer.webp",
  "./images/hard-hat.webp",
  "./images/harness.webp",
  "./images/ladder.webp",
  "./images/level.webp",
  "./images/load.webp",
  "./images/loader.webp",
  "./images/lockout.webp",
  "./images/lumber.webp",
  "./images/machine.webp",
  "./images/mig-welder.webp",
  "./images/multimeter.webp",
  "./images/pipe.webp",
  "./images/plank.webp",
  "./images/pliers.webp",
  "./images/plywood.webp",
  "./images/ppe.webp",
  "./images/pvc.webp",
  "./images/rebar.webp",
  "./images/refrigerant.webp",
  "./images/safety-glasses.webp",
  "./images/sand.webp",
  "./images/scaffold.webp",
  "./images/screwdriver.webp",
  "./images/shovel.webp",
  "./images/shutoff.webp",
  "./images/slab.webp",
  "./images/slag.webp",
  "./images/steel.webp",
  "./images/stick-welder.webp",
  "./images/tape-measure.webp",
  "./images/thermostat.webp",
  "./images/tig-welder.webp",
  "./images/toolbox.webp",
  "./images/torch.webp",
  "./images/water-heater.webp",
  "./images/water.webp",
  "./images/welding-gloves.webp",
  "./images/welding-helmet.webp",
  "./images/welding-wire.webp",
  "./images/wheelbarrow.webp",
  "./images/wrench.webp",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) => cache.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  event.respondWith(
    caches.match(req).then((cached) => {
      const network = fetch(req).then((res) => {
        const copy = res.clone();
        if (res.ok && new URL(req.url).origin === self.location.origin) {
          caches.open(CACHE).then((cache) => cache.put(req, copy));
        }
        return res;
      }).catch(() => cached);
      return cached || network;
    })
  );
});
