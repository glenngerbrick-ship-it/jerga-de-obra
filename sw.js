const CACHE = "jerga-de-obra-v4";
const ASSETS = [
  "./",
  "./index.html",
  "./phrases.js",
  "./manifest.json",
  "./icon.png",
  "./sw.js",
  "./images/ac-unit.svg",
  "./images/air-filter.svg",
  "./images/breaker.svg",
  "./images/brick.svg",
  "./images/bulldozer.svg",
  "./images/cable.svg",
  "./images/caster.svg",
  "./images/cement.svg",
  "./images/circular-saw.svg",
  "./images/concrete.svg",
  "./images/condenser.svg",
  "./images/copper.svg",
  "./images/crane.svg",
  "./images/drain.svg",
  "./images/drill.svg",
  "./images/drywall.svg",
  "./images/duct.svg",
  "./images/dump-truck.svg",
  "./images/electrical-tape.svg",
  "./images/electrode.svg",
  "./images/evaporator.svg",
  "./images/excavator.svg",
  "./images/extension-cord.svg",
  "./images/forklift.svg",
  "./images/formwork.svg",
  "./images/gas-cylinder.svg",
  "./images/gravel.svg",
  "./images/grinder.svg",
  "./images/guardrail.svg",
  "./images/hammer.svg",
  "./images/hard-hat.svg",
  "./images/harness.svg",
  "./images/ladder.svg",
  "./images/level.svg",
  "./images/load.svg",
  "./images/loader.svg",
  "./images/lockout.svg",
  "./images/lumber.svg",
  "./images/machine.svg",
  "./images/mig-welder.svg",
  "./images/multimeter.svg",
  "./images/pipe.svg",
  "./images/plank.svg",
  "./images/pliers.svg",
  "./images/plywood.svg",
  "./images/ppe.svg",
  "./images/pvc.svg",
  "./images/rebar.svg",
  "./images/refrigerant.svg",
  "./images/safety-glasses.svg",
  "./images/sand.svg",
  "./images/scaffold.svg",
  "./images/screwdriver.svg",
  "./images/shovel.svg",
  "./images/shutoff.svg",
  "./images/slab.svg",
  "./images/slag.svg",
  "./images/steel.svg",
  "./images/stick-welder.svg",
  "./images/tape-measure.svg",
  "./images/thermostat.svg",
  "./images/tig-welder.svg",
  "./images/toolbox.svg",
  "./images/torch.svg",
  "./images/water-heater.svg",
  "./images/water.svg",
  "./images/welding-gloves.svg",
  "./images/welding-helmet.svg",
  "./images/welding-wire.svg",
  "./images/wheelbarrow.svg",
  "./images/wrench.svg",
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
