#!/usr/bin/env python3
"""Assemble index.html from extracted CSS + enhanced app shell/JS."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS = Path("/tmp/jobsite-style.cssblock").read_text()

EXTRA_CSS = """
.badge.fav { background: var(--blaze); border-color: var(--ink); color: var(--ink); }
.badge.due { background: #fff; border-color: var(--bad); color: var(--bad); }
.icon-btn.fav.on {
  background: var(--blaze);
  border-color: var(--ink);
  color: var(--ink);
}
.quick-row {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin: 0 0 16px;
}
.quick-row .btn { flex: 1; min-width: 120px; font-size: 0.85rem; padding: 12px 10px; }
.onboard {
  position: fixed;
  inset: 0;
  z-index: 90;
  background: rgba(10,10,10,0.72);
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding: 18px;
  animation: fadeIn 0.25s ease both;
}
.onboard[hidden] { display: none !important; }
.onboard-card {
  width: min(520px, 100%);
  background: #fff;
  border: 3px solid var(--ink);
  border-radius: 20px;
  padding: 24px 20px 20px;
  box-shadow: 10px 10px 0 var(--blaze);
  animation: rise 0.4s ease both;
}
.onboard-card h2 {
  font-family: var(--font-display);
  font-size: 2.2rem;
  letter-spacing: 0.04em;
  line-height: 0.95;
  margin-bottom: 8px;
}
.onboard-card p {
  font-weight: 600;
  color: var(--ink-soft);
  margin-bottom: 16px;
}
.onboard-steps {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
}
.onboard-steps span {
  flex: 1;
  height: 6px;
  border-radius: 99px;
  background: var(--paper-2);
  border: 1px solid var(--line);
}
.onboard-steps span.on { background: var(--blaze); border-color: var(--ink); }
.audio-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.72rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border: 2px solid var(--ink);
  background: #fff;
  padding: 4px 10px;
  border-radius: 999px;
}
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

.cat-btn .pic {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  border: 2px solid var(--ink);
  background: var(--blaze);
  object-fit: cover;
  display: block;
  margin-bottom: 10px;
}
.nav-btn .glyph {
  width: 28px;
  height: 28px;
  border-radius: 8px;
  display: grid;
  place-items: center;
  border: 2px solid transparent;
  transition: all 0.15s;
}
.nav-btn .glyph svg {
  width: 18px;
  height: 18px;
  display: block;
}

/* —— Launch / splash cover —— */
.splash {
  position: fixed;
  inset: 0;
  z-index: 200;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background:
    radial-gradient(ellipse 70% 50% at 50% 42%, rgba(255, 209, 0, 0.28), transparent 60%),
    #0a0a0a;
  padding: 24px 24px calc(24px + env(safe-area-inset-bottom));
  transition: opacity 0.4s ease;
}
.splash.hide {
  opacity: 0;
  pointer-events: none;
}
.splash-mark {
  width: min(58vw, 38vh, 280px);
  height: min(58vw, 38vh, 280px);
  border-radius: 22%;
  border: 6px solid #0a0a0a;
  box-shadow: 10px 10px 0 #ffd100;
  overflow: hidden;
  background: #0a0a0a;
  margin-bottom: 6.5%;
  flex-shrink: 0;
}
.splash-mark img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.splash-title {
  font-family: var(--font-display);
  font-size: clamp(3rem, 14vw, 5.2rem);
  letter-spacing: 0.03em;
  line-height: 0.88;
  text-align: center;
  color: #ffd100;
}
.splash-title em {
  font-style: normal;
  color: #0a0a0a;
  background: #ffd100;
  padding: 0 0.12em;
  display: inline-block;
  margin-top: 0.06em;
  border-radius: 0.08em;
}
.splash-tag {
  margin-top: 0.7em;
  font-weight: 600;
  font-size: clamp(0.95rem, 3.4vw, 1.15rem);
  color: #e8e8e8;
  text-align: center;
}
.onboard-logo {
  width: 72px;
  height: 72px;
  border-radius: 14px;
  object-fit: cover;
  border: 2px solid var(--ink);
  box-shadow: 4px 4px 0 var(--blaze);
  margin-bottom: 14px;
  display: block;
}
"""

# Insert extra CSS before closing style
if CSS.strip().endswith("</style>"):
    CSS_FULL = CSS.replace("</style>", EXTRA_CSS + "\n</style>")
else:
    CSS_FULL = CSS + EXTRA_CSS

JS = r"""
const DATA = window.JERGA_DATA;
const builtInPhrases = DATA.phrases;
const categories = DATA.categories;

const QUIZ_LINES = {
  win: [
    "Foreman material. Filthy and fluent.",
    "You'd survive day one. Mouth and all.",
    "That's jerga. Not Duolingo."
  ],
  mid: [
    "Not bad. Don't freeze when someone yells ¡Aguas, cabrón!",
    "Halfway. Drill the dirty ones before the pour."
  ],
  low: [
    "Rough shift. Hit Safety — and Jerga — again.",
    "Shake it off. Real crews cuss, then they learn."
  ]
};

const ONBOARD_STEPS = [
  {
    title: "Talk like the crew",
    body: "Browse Safety, Tools, Jerga, HVAC — phrases people actually yell, including the filthy ones."
  },
  {
    title: "Hear real Mexican Spanish",
    body: "Tap SAY for Mexican Spanish clips. Flip, Drill both ways, star the keepers — vulgar allowed."
  },
  {
    title: "Review what sticks",
    body: "Mark GOT IT, Review due phrases, add your crew's worst hits. Offline once installed."
  }
];

let customPhrases = safeParse("customPhrases", []);
let knownIds = new Set(safeParse("knownIds", []));
let favoriteIds = new Set(safeParse("favoriteIds", []));
let reviewMap = safeParse("reviewMap", {}); // id -> { due, interval, ease }
let bestScore = Number(localStorage.getItem("bestScore") || 0);
let streakBest = Number(localStorage.getItem("streakBest") || 0);
let speechRate = Number(localStorage.getItem("speechRate") || 0.88);
let quizDirection = localStorage.getItem("quizDirection") || "es-en";
let onboarded = localStorage.getItem("onboarded") === "1";
let onboardStep = 0;

let currentCat = "all";
let currentView = "home";
let quizIndex = 0;
let quizScore = 0;
let quizStreak = 0;
let quizQuestions = [];
let quizMode = "mixed"; // mixed | review | favorites
let cardDeck = [];
let cardIndex = 0;
let cardFlipped = false;
let moreTab = "stats";
let activeAudio = null;

const main = document.getElementById("mainContent");
const tabs = document.getElementById("categoryTabs");
const searchEl = document.getElementById("search");
const searchWrap = document.getElementById("searchWrap");
const onboardEl = document.getElementById("onboard");

function safeParse(key, fallback) {
  try {
    const v = JSON.parse(localStorage.getItem(key) || "null");
    return v == null ? fallback : v;
  } catch {
    return fallback;
  }
}

function phraseId(p) {
  return p.id || `${p.cat}::${p.es}::${p.en}`;
}

function getAllPhrases() {
  return [
    ...builtInPhrases.map(p => ({ ...p, custom: false })),
    ...customPhrases.map((p, i) => ({
      ...p,
      id: p.id || `custom-${i}-${(p.es || "").slice(0, 12)}`,
      custom: true
    }))
  ];
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function toast(msg) {
  const el = document.getElementById("toast");
  el.textContent = msg;
  el.classList.add("show");
  clearTimeout(toast._t);
  toast._t = setTimeout(() => el.classList.remove("show"), 1800);
}

function stopAudio() {
  if (activeAudio) {
    activeAudio.pause();
    activeAudio = null;
  }
  if ("speechSynthesis" in window) speechSynthesis.cancel();
}

function speakTTS(text, lang = "es-MX") {
  if (!("speechSynthesis" in window)) {
    toast("Speech not supported on this device");
    return;
  }
  const u = new SpeechSynthesisUtterance(text);
  u.lang = lang;
  u.rate = Math.min(1.4, Math.max(0.55, speechRate || 0.88));
  speechSynthesis.cancel();
  speechSynthesis.speak(u);
}

function speak(textOrPhrase, lang = "es-MX") {
  stopAudio();
  const p = typeof textOrPhrase === "object" ? textOrPhrase : null;
  const text = p ? p.es : textOrPhrase;
  const src = p && p.audio ? p.audio : null;
  if (src && lang.startsWith("es")) {
    const audio = new Audio(src);
    audio.playbackRate = Math.min(1.35, Math.max(0.7, speechRate || 0.88));
    activeAudio = audio;
    audio.play().catch(() => speakTTS(text, lang));
    return;
  }
  speakTTS(text, lang);
}

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function persistKnown() {
  localStorage.setItem("knownIds", JSON.stringify([...knownIds]));
}
function persistFavorites() {
  localStorage.setItem("favoriteIds", JSON.stringify([...favoriteIds]));
}
function persistReview() {
  localStorage.setItem("reviewMap", JSON.stringify(reviewMap));
}

function toggleKnown(id) {
  if (knownIds.has(id)) knownIds.delete(id);
  else knownIds.add(id);
  persistKnown();
}

function toggleFavorite(id) {
  if (favoriteIds.has(id)) favoriteIds.delete(id);
  else favoriteIds.add(id);
  persistFavorites();
}

function duePhrases() {
  const now = Date.now();
  return getAllPhrases().filter(p => {
    const r = reviewMap[phraseId(p)];
    return r && r.due <= now;
  });
}

function scheduleReview(id, grade) {
  // grade: "again" | "good" | "easy"
  const now = Date.now();
  const cur = reviewMap[id] || { due: now, interval: 0, ease: 2.3 };
  let interval = cur.interval || 0;
  let ease = cur.ease || 2.3;
  if (grade === "again") {
    interval = 0;
    ease = Math.max(1.3, ease - 0.2);
    cur.due = now + 10 * 60 * 1000; // 10 min
  } else if (grade === "good") {
    interval = interval <= 0 ? 1 : Math.round(interval * ease);
    ease = Math.min(2.8, ease + 0.05);
    cur.due = now + interval * 24 * 60 * 60 * 1000;
  } else {
    interval = interval <= 0 ? 3 : Math.round(interval * ease * 1.3);
    ease = Math.min(3.0, ease + 0.1);
    cur.due = now + interval * 24 * 60 * 60 * 1000;
  }
  cur.interval = interval;
  cur.ease = ease;
  reviewMap[id] = cur;
  persistReview();
}

function renderOnboard() {
  if (onboarded) {
    onboardEl.hidden = true;
    return;
  }
  const step = ONBOARD_STEPS[onboardStep];
  onboardEl.hidden = false;
  onboardEl.innerHTML = `
    <div class="onboard-card" role="dialog" aria-modal="true" aria-label="Welcome">
      <img src="icon.png" alt="" class="onboard-logo" width="72" height="72">
      <div class="onboard-steps">${ONBOARD_STEPS.map((_, i) =>
        `<span class="${i <= onboardStep ? "on" : ""}"></span>`
      ).join("")}</div>
      <h2>${escapeHtml(step.title)}</h2>
      <p>${escapeHtml(step.body)}</p>
      <div class="btn-row">
        ${onboardStep > 0 ? `<button type="button" class="btn ghost" id="obBack">Back</button>` : `<button type="button" class="btn ghost" id="obSkip">Skip</button>`}
        <button type="button" class="btn" id="obNext">${onboardStep === ONBOARD_STEPS.length - 1 ? "Let's go" : "Next"}</button>
      </div>
    </div>
  `;
  const finish = () => {
    onboarded = true;
    localStorage.setItem("onboarded", "1");
    onboardEl.hidden = true;
  };
  const skip = document.getElementById("obSkip");
  if (skip) skip.onclick = finish;
  const back = document.getElementById("obBack");
  if (back) back.onclick = () => { onboardStep--; renderOnboard(); };
  document.getElementById("obNext").onclick = () => {
    if (onboardStep >= ONBOARD_STEPS.length - 1) finish();
    else { onboardStep++; renderOnboard(); }
  };
}

function renderTabs() {
  if (currentView !== "home") {
    tabs.style.display = "none";
    tabs.innerHTML = "";
    return;
  }
  tabs.style.display = "";
  const items = [{ id: "all", name: "All" }, ...categories];
  tabs.innerHTML = items.map(c =>
    `<button type="button" class="chip ${currentCat === c.id ? "on" : ""}" data-cat="${escapeHtml(c.id)}">${escapeHtml(c.name)}</button>`
  ).join("");
  tabs.querySelectorAll(".chip").forEach(t => {
    t.onclick = () => {
      currentCat = t.dataset.cat;
      render();
    };
  });
}

function phraseCard(p, i) {
  const id = phraseId(p);
  const known = knownIds.has(id);
  const fav = favoriteIds.has(id);
  const due = reviewMap[id] && reviewMap[id].due <= Date.now();
  const badges = [
    p.custom ? `<span class="badge mine">Mine</span>` : "",
    fav ? `<span class="badge fav">★ Fav</span>` : "",
    due ? `<span class="badge due">Due</span>` : "",
    i < 3 && currentCat === "all" ? `<span class="badge hot">Hot</span>` : ""
  ].join("");
  return `
    <article class="phrase ${known ? "known" : ""}" data-id="${escapeHtml(id)}" style="animation-delay:${Math.min(i, 8) * 0.04}s">
      <div class="es">${escapeHtml(p.es)}</div>
      <div class="actions">
        <button type="button" class="icon-btn play" data-id="${escapeHtml(id)}" aria-label="Play Spanish">SAY</button>
        <button type="button" class="icon-btn ghost fav ${fav ? "on" : ""}" data-id="${escapeHtml(id)}" aria-label="Favorite">${fav ? "★" : "☆"}</button>
        <button type="button" class="icon-btn ghost mark ${known ? "on" : ""}" data-id="${escapeHtml(id)}" aria-label="Mark known">${known ? "GOT" : "GOT?"}</button>
      </div>
      <div class="en">${escapeHtml(p.en)}</div>
      <div class="meta">
        ${badges}
        ${p.tip ? `<span class="tip">${escapeHtml(p.tip)}</span>` : ""}
      </div>
    </article>
  `;
}

function findById(id) {
  return getAllPhrases().find(p => phraseId(p) === id);
}

function attachPhraseHandlers(root = main) {
  root.querySelectorAll(".play").forEach(b => {
    b.onclick = (e) => {
      e.stopPropagation();
      b.classList.remove("speak-pulse");
      void b.offsetWidth;
      b.classList.add("speak-pulse");
      const p = findById(b.dataset.id);
      if (p) speak(p);
      else speak(b.dataset.text || "");
    };
  });
  root.querySelectorAll(".fav").forEach(b => {
    b.onclick = (e) => {
      e.stopPropagation();
      toggleFavorite(b.dataset.id);
      toast(favoriteIds.has(b.dataset.id) ? "Starred" : "Unstarred");
      if (currentView === "home") renderHome();
      else renderProgress();
    };
  });
  root.querySelectorAll(".mark").forEach(b => {
    b.onclick = (e) => {
      e.stopPropagation();
      const id = b.dataset.id;
      const was = knownIds.has(id);
      toggleKnown(id);
      if (!was) scheduleReview(id, "good");
      toast(knownIds.has(id) ? "Marked as known" : "Unmarked");
      if (currentView === "home") renderHome();
      else renderProgress();
    };
  });
}

function filteredPhrases() {
  const all = getAllPhrases();
  let list = currentCat === "all" ? all
    : currentCat === "Custom" ? all.filter(p => p.custom)
    : currentCat === "favorites" ? all.filter(p => favoriteIds.has(phraseId(p)))
    : currentCat === "due" ? duePhrases()
    : all.filter(p => p.cat === currentCat);
  const q = searchEl.value.trim().toLowerCase();
  if (q) {
    list = list.filter(p =>
      p.es.toLowerCase().includes(q) ||
      p.en.toLowerCase().includes(q) ||
      (p.cat || "").toLowerCase().includes(q) ||
      (p.tip || "").toLowerCase().includes(q)
    );
  }
  return list;
}

function categoryIcon(c) {
  const meta = DATA.images && c.icon ? DATA.images[c.icon] : null;
  if (!meta) return "";
  return `<img class="pic" src="${escapeHtml(meta.src)}" alt="" width="48" height="48">`;
}

function renderHome() {
  searchWrap.style.display = "";
  const all = getAllPhrases();
  const results = filteredPhrases();
  const searching = searchEl.value.trim().length > 0;
  const due = duePhrases();
  const favs = all.filter(p => favoriteIds.has(phraseId(p)));

  if (currentCat === "all" && !searching) {
    const popular = all.slice(0, 8);
    main.innerHTML = `
      <div class="quick-row">
        <button type="button" class="btn" id="goReview">${due.length ? `Review ${due.length} due` : "Review (none due)"}</button>
        <button type="button" class="btn steel" id="goFavs">★ Favorites (${favs.length})</button>
      </div>
      <div class="cat-grid">
        ${categories.map(c => `
          <button type="button" class="cat-btn ${c.id === "Custom" ? "wide" : ""}" data-cat="${escapeHtml(c.id)}">
            ${categoryIcon(c)}
            <h3>${escapeHtml(c.name)}</h3>
            <p>${escapeHtml(c.desc)}</p>
          </button>
        `).join("")}
      </div>
      <div class="section-head">
        <h2>Start yelling these</h2>
        <span>${all.length} phrases · <span class="audio-pill">MX audio</span></span>
      </div>
      <div class="phrase-list">${popular.map((p, i) => phraseCard(p, i)).join("")}</div>
    `;
    main.querySelectorAll(".cat-btn").forEach(c => {
      c.onclick = () => { currentCat = c.dataset.cat; render(); };
    });
    document.getElementById("goReview").onclick = () => {
      currentView = "quiz";
      quizMode = "review";
      document.querySelectorAll(".nav-btn").forEach(x => x.classList.toggle("on", x.dataset.view === "quiz"));
      startQuiz(true);
    };
    document.getElementById("goFavs").onclick = () => {
      currentCat = "favorites";
      render();
    };
  } else {
    const titleMap = {
      all: "Results",
      favorites: "Favorites",
      due: "Due for review"
    };
    const title = titleMap[currentCat] || (categories.find(c => c.id === currentCat)?.name || "Phrases");
    main.innerHTML = `
      <div class="section-head">
        <h2>${escapeHtml(title)}</h2>
        <span>${results.length}</span>
      </div>
      ${results.length
        ? `<div class="phrase-list">${results.map((p, i) => phraseCard(p, i)).join("")}</div>`
        : `<div class="empty"><h3>Nothing here</h3><p>Try another word — or add your own crew slang.</p></div>`}
    `;
  }
  attachPhraseHandlers();
}

function startCards(reshuffle = true) {
  searchWrap.style.display = "none";
  let all = getAllPhrases();
  if (quizMode === "favorites") all = all.filter(p => favoriteIds.has(phraseId(p)));
  if (quizMode === "review") {
    const due = duePhrases();
    all = due.length ? due : all;
  }
  if (!all.length) {
    main.innerHTML = `<div class="empty"><h3>No phrases</h3><p>Add some slang or star favorites first.</p></div>`;
    return;
  }
  if (reshuffle || !cardDeck.length) {
    cardDeck = shuffle(all);
    cardIndex = 0;
  }
  cardFlipped = false;
  if (cardIndex >= cardDeck.length) cardIndex = 0;
  showCard();
}

function showCard() {
  const p = cardDeck[cardIndex];
  const id = phraseId(p);
  const known = knownIds.has(id);
  const fav = favoriteIds.has(id);
  main.innerHTML = `
    <div class="quiz-meta">
      <span>Card ${cardIndex + 1} / ${cardDeck.length}</span>
      <span>${known ? "Known" : "Learning"}${fav ? " · ★" : ""}</span>
    </div>
    <div class="track"><i style="width:${((cardIndex) / cardDeck.length) * 100}%"></i></div>
    <div class="flip-stage">
      <div class="flip-card ${cardFlipped ? "show-back" : ""}" id="flipCard" role="button" tabindex="0" aria-label="Flip card">
        <div class="flip-face front">
          <div class="lang">Spanish · tap to flip</div>
          <div class="big">${escapeHtml(p.es)}</div>
          <div class="hint">${escapeHtml(p.cat)}${p.custom ? " · Mine" : ""}</div>
        </div>
        <div class="flip-face back">
          <div class="lang">English</div>
          <div class="big">${escapeHtml(p.en)}</div>
          <div class="hint">${p.tip ? escapeHtml(p.tip) : "No tip — you got this"}</div>
        </div>
      </div>
    </div>
    <div class="btn-row">
      <button type="button" class="btn" id="hearCard">Hear Spanish</button>
      <button type="button" class="btn steel" id="flipBtn">Flip</button>
    </div>
    <div class="btn-row">
      <button type="button" class="btn ghost" id="prevCard">Back</button>
      <button type="button" class="btn ghost" id="favCard">${fav ? "Unstar" : "★ Fav"}</button>
      <button type="button" class="btn ghost" id="markCard">${known ? "Unmark" : "Got it"}</button>
      <button type="button" class="btn" id="nextCard">Next</button>
    </div>
    <div class="btn-row">
      <button type="button" class="btn ghost" id="againCard">Again (review)</button>
      <button type="button" class="btn ghost" id="shuffleCards">Shuffle deck</button>
    </div>
  `;
  const flip = () => {
    cardFlipped = !cardFlipped;
    document.getElementById("flipCard").classList.toggle("show-back", cardFlipped);
  };
  document.getElementById("flipCard").onclick = flip;
  document.getElementById("flipCard").onkeydown = (e) => {
    if (e.key === "Enter" || e.key === " ") { e.preventDefault(); flip(); }
  };
  document.getElementById("flipBtn").onclick = flip;
  document.getElementById("hearCard").onclick = () => speak(p);
  document.getElementById("prevCard").onclick = () => {
    cardIndex = (cardIndex - 1 + cardDeck.length) % cardDeck.length;
    cardFlipped = false;
    showCard();
  };
  document.getElementById("nextCard").onclick = () => {
    cardIndex = (cardIndex + 1) % cardDeck.length;
    cardFlipped = false;
    showCard();
  };
  document.getElementById("favCard").onclick = () => {
    toggleFavorite(id);
    toast(favoriteIds.has(id) ? "Starred" : "Unstarred");
    showCard();
  };
  document.getElementById("markCard").onclick = () => {
    const was = knownIds.has(id);
    toggleKnown(id);
    if (!was) scheduleReview(id, "good");
    toast(knownIds.has(id) ? "Marked known" : "Unmarked");
    showCard();
  };
  document.getElementById("againCard").onclick = () => {
    scheduleReview(id, "again");
    toast("Back in 10 min");
    cardIndex = (cardIndex + 1) % cardDeck.length;
    cardFlipped = false;
    showCard();
  };
  document.getElementById("shuffleCards").onclick = () => startCards(true);
}

function renderAdd() {
  searchWrap.style.display = "none";
  main.innerHTML = `
    <div class="panel blaze">
      <h2>Add your slang</h2>
      <p class="lead">If your crew says it — even the filthy stuff — it belongs here.</p>
      <label for="newEs">Spanish</label>
      <input id="newEs" type="text" placeholder="Pásame la varilla">
      <label for="newEn">English</label>
      <input id="newEn" type="text" placeholder="Pass me the rebar">
      <label for="newCat">Category</label>
      <select id="newCat">
        ${categories.filter(c => c.id !== "Custom").map(c =>
          `<option value="${escapeHtml(c.id)}">${escapeHtml(c.name)}</option>`
        ).join("")}
        <option value="Custom">My Phrases</option>
      </select>
      <label for="newTip">Tip (optional)</label>
      <input id="newTip" type="text" placeholder="When the foreman is mid-rant…">
      <div class="btn-row">
        <button type="button" class="btn" id="savePhrase">Save phrase</button>
      </div>
      <p class="status" id="addStatus"></p>
    </div>
  `;
  document.getElementById("savePhrase").onclick = saveCustomPhrase;
}

function saveCustomPhrase() {
  const es = document.getElementById("newEs").value.trim();
  const en = document.getElementById("newEn").value.trim();
  const cat = document.getElementById("newCat").value;
  const tip = document.getElementById("newTip").value.trim();
  const status = document.getElementById("addStatus");
  if (!es || !en) {
    status.textContent = "Need both Spanish and English.";
    status.className = "status bad";
    return;
  }
  customPhrases.push({
    id: `custom-${Date.now()}`,
    cat, es, en, tip: tip || undefined
  });
  localStorage.setItem("customPhrases", JSON.stringify(customPhrases));
  status.textContent = "Locked in. It'll show up in Drill.";
  status.className = "status ok";
  document.getElementById("newEs").value = "";
  document.getElementById("newEn").value = "";
  document.getElementById("newTip").value = "";
  toast("Phrase saved");
}

function speakInterp(lang) {
  const text = document.getElementById("interpText").value.trim();
  if (!text) {
    toast("Type something first");
    return;
  }
  speakTTS(text, lang === "es" ? "es-MX" : "en-US");
  if (lang === "es" && !document.getElementById("interpEs").value) {
    document.getElementById("interpEs").value = text;
  }
  if (lang === "en" && !document.getElementById("interpEn").value) {
    document.getElementById("interpEn").value = text;
  }
}

function saveFromInterpreter() {
  const es = document.getElementById("interpEs").value.trim();
  const en = document.getElementById("interpEn").value.trim();
  const cat = document.getElementById("interpCat").value;
  const status = document.getElementById("interpStatus");
  if (!es || !en) {
    status.textContent = "Need Spanish and English to save.";
    status.className = "status bad";
    return;
  }
  customPhrases.push({ id: `custom-${Date.now()}`, cat, es, en });
  localStorage.setItem("customPhrases", JSON.stringify(customPhrases));
  status.textContent = "Saved. Go crush Drill.";
  status.className = "status ok";
  toast("Added to learning");
}

function startQuiz(fresh = true) {
  searchWrap.style.display = "none";
  let all = getAllPhrases();
  if (quizMode === "favorites") all = all.filter(p => favoriteIds.has(phraseId(p)));
  if (quizMode === "review") {
    const due = duePhrases();
    all = due.length ? due : all.filter(p => !knownIds.has(phraseId(p))).slice(0, 20);
    if (!all.length) all = getAllPhrases();
  }
  if (all.length < 4) {
    main.innerHTML = `<div class="empty"><h3>Need more phrases</h3><p>Add a few, star favorites, or wait for reviews to come due.</p></div>`;
    return;
  }
  if (fresh) {
    quizQuestions = shuffle(all).slice(0, Math.min(10, all.length));
    quizIndex = 0;
    quizScore = 0;
    quizStreak = 0;
  }
  showQuestion();
}

function pickLine(bucket) {
  return bucket[Math.floor(Math.random() * bucket.length)];
}

function showQuestion() {
  if (quizIndex >= quizQuestions.length) {
    if (quizScore > bestScore) {
      bestScore = quizScore;
      localStorage.setItem("bestScore", String(bestScore));
    }
    const ratio = quizScore / quizQuestions.length;
    const line = ratio >= 0.8 ? pickLine(QUIZ_LINES.win)
      : ratio >= 0.5 ? pickLine(QUIZ_LINES.mid)
      : pickLine(QUIZ_LINES.low);
    main.innerHTML = `
      <div class="panel blaze" style="text-align:center;">
        <h2>Shift over</h2>
        <div class="score-big">${quizScore}/${quizQuestions.length}</div>
        <p class="lead">${escapeHtml(line)}</p>
        ${streakBest ? `<p class="streak">Best streak: ${streakBest}</p>` : ""}
        <div class="btn-row" style="justify-content:center;">
          <button type="button" class="btn" id="retryQuiz">Run it back</button>
          <button type="button" class="btn ghost" id="homeAfterQuiz">Home</button>
        </div>
      </div>
    `;
    document.getElementById("retryQuiz").onclick = () => startQuiz(true);
    document.getElementById("homeAfterQuiz").onclick = () => {
      currentView = "home";
      quizMode = "mixed";
      document.querySelectorAll(".nav-btn").forEach(x => x.classList.toggle("on", x.dataset.view === "home"));
      render();
    };
    return;
  }

  const q = quizQuestions[quizIndex];
  const pool = getAllPhrases();
  const esToEn = quizDirection !== "en-es";
  const prompt = esToEn ? q.es : q.en;
  const answer = esToEn ? q.en : q.es;
  const options = [answer];
  let guard = 0;
  while (options.length < 4 && guard++ < 80) {
    const randP = pool[Math.floor(Math.random() * pool.length)];
    const rand = esToEn ? randP.en : randP.es;
    if (!options.includes(rand)) options.push(rand);
  }
  options.sort(() => Math.random() - 0.5);

  main.innerHTML = `
    <div class="panel">
      <div class="mode-switch" role="group" aria-label="Drill mode">
        <button type="button" class="${quizMode === "mixed" ? "on" : ""}" data-mode="mixed">All</button>
        <button type="button" class="${quizMode === "review" ? "on" : ""}" data-mode="review">Review</button>
        <button type="button" class="${quizMode === "favorites" ? "on" : ""}" data-mode="favorites">★ Favs</button>
      </div>
      <div class="mode-switch" role="group" aria-label="Drill direction" style="margin-top:8px;">
        <button type="button" class="${esToEn ? "on" : ""}" data-dir="es-en">ES → EN</button>
        <button type="button" class="${!esToEn ? "on" : ""}" data-dir="en-es">EN → ES</button>
      </div>
      <div class="quiz-meta">
        <span>Q ${quizIndex + 1} / ${quizQuestions.length}</span>
        <span>${quizStreak ? `Streak ${quizStreak}` : "No streak yet"}</span>
      </div>
      <div class="track"><i style="width:${(quizIndex / quizQuestions.length) * 100}%"></i></div>
      <div class="quiz-prompt">${escapeHtml(prompt)}</div>
      <p class="lead" style="margin-bottom:0;">${esToEn ? "What does it mean?" : "How do you say it?"}</p>
      <div class="options">
        ${options.map(o =>
          `<button type="button" class="option" data-correct="${o === answer}">${escapeHtml(o)}</button>`
        ).join("")}
      </div>
      <div class="btn-row">
        <button type="button" class="btn ghost" id="hearQ">Hear Spanish</button>
      </div>
    </div>
  `;
  document.querySelectorAll(".mode-switch button[data-mode]").forEach(b => {
    b.onclick = () => {
      quizMode = b.dataset.mode;
      startQuiz(true);
    };
  });
  document.querySelectorAll(".mode-switch button[data-dir]").forEach(b => {
    b.onclick = () => {
      quizDirection = b.dataset.dir;
      localStorage.setItem("quizDirection", quizDirection);
      showQuestion();
    };
  });
  document.getElementById("hearQ").onclick = () => speak(q);
  document.querySelectorAll(".option").forEach(opt => {
    opt.onclick = () => {
      document.querySelectorAll(".option").forEach(o => { o.disabled = true; });
      const correct = opt.dataset.correct === "true";
      const id = phraseId(q);
      if (correct) {
        opt.classList.add("correct");
        quizScore++;
        quizStreak++;
        if (quizStreak > streakBest) {
          streakBest = quizStreak;
          localStorage.setItem("streakBest", String(streakBest));
        }
        scheduleReview(id, "good");
        if (!knownIds.has(id)) {
          knownIds.add(id);
          persistKnown();
        }
        toast(quizStreak >= 3 ? `Streak ${quizStreak} — on fire` : "Nice");
      } else {
        opt.classList.add("wrong");
        quizStreak = 0;
        scheduleReview(id, "again");
        const right = document.querySelector('.option[data-correct="true"]');
        if (right) right.classList.add("correct");
        toast("Nope — back in review soon");
      }
      setTimeout(() => { quizIndex++; showQuestion(); }, 850);
    };
  });
}

function renderProgress() {
  searchWrap.style.display = "none";
  const known = knownIds.size;
  const customCount = customPhrases.length;
  const total = getAllPhrases().length;
  const pct = Math.min(100, Math.round((known / Math.max(total, 1)) * 100));
  const offline = !navigator.onLine;
  const due = duePhrases().length;
  const favs = favoriteIds.size;

  main.innerHTML = `
    <div class="mode-switch" role="tablist">
      <button type="button" class="${moreTab === "stats" ? "on" : ""}" data-tab="stats">Stats</button>
      <button type="button" class="${moreTab === "speak" ? "on" : ""}" data-tab="speak">Speak</button>
      <button type="button" class="${moreTab === "customs" ? "on" : ""}" data-tab="customs">My slang</button>
    </div>
    <div id="morePanel"></div>
  `;
  document.querySelectorAll(".mode-switch button").forEach(b => {
    b.onclick = () => { moreTab = b.dataset.tab; renderProgress(); };
  });

  const panel = document.getElementById("morePanel");
  if (moreTab === "speak") {
    panel.innerHTML = `
      <div class="panel">
        <h2>Speak it</h2>
        <p class="lead">Type anything. Device TTS for freeform; built-in phrases use Mexican Spanish clips.</p>
        <label for="interpText">Phrase</label>
        <textarea id="interpText" placeholder="Type English or Spanish…"></textarea>
        <label>Speech speed</label>
        <div class="rate-row">
          <span style="font-weight:800;font-size:0.75rem;">Slow</span>
          <input type="range" id="speechRate" min="0.55" max="1.25" step="0.05" value="${speechRate}">
          <span style="font-weight:800;font-size:0.75rem;">Fast</span>
        </div>
        <div class="btn-row">
          <button type="button" class="btn" id="speakEs">Speak Spanish</button>
          <button type="button" class="btn steel" id="speakEn">Speak English</button>
        </div>
        <hr style="border:none;border-top:2px solid var(--line);margin:20px 0;">
        <h2 style="font-size:1.5rem;">Keep it</h2>
        <label for="interpEs">Spanish</label>
        <input id="interpEs" type="text" placeholder="Spanish version">
        <label for="interpEn">English</label>
        <input id="interpEn" type="text" placeholder="English version">
        <label for="interpCat">Category</label>
        <select id="interpCat">
          ${categories.filter(c => c.id !== "Custom").map(c =>
            `<option value="${escapeHtml(c.id)}">${escapeHtml(c.name)}</option>`
          ).join("")}
          <option value="Custom">My Phrases</option>
        </select>
        <div class="btn-row">
          <button type="button" class="btn" id="saveInterp">Add to learning</button>
        </div>
        <p class="status" id="interpStatus"></p>
      </div>
    `;
    document.getElementById("speechRate").oninput = (e) => {
      speechRate = Number(e.target.value);
      localStorage.setItem("speechRate", String(speechRate));
    };
    document.getElementById("speakEs").onclick = () => speakInterp("es");
    document.getElementById("speakEn").onclick = () => speakInterp("en");
    document.getElementById("saveInterp").onclick = saveFromInterpreter;
    return;
  }

  if (moreTab === "customs") {
    panel.innerHTML = `
      <div class="panel">
        <h2>My slang</h2>
        <p class="lead">${customCount ? "Delete anything that doesn't earn its keep." : "Nothing custom yet — Add some crew talk."}</p>
        <div class="custom-list">
          ${customPhrases.length ? customPhrases.map((p, i) => `
            <div class="custom-row">
              <div class="txt">${escapeHtml(p.es)}<small>${escapeHtml(p.en)} · ${escapeHtml(p.cat || "Custom")}</small></div>
              <button type="button" class="danger-btn" data-i="${i}">Delete</button>
            </div>
          `).join("") : `<div class="empty"><h3>Empty</h3><p>Your additions show up here.</p></div>`}
        </div>
      </div>
    `;
    panel.querySelectorAll(".danger-btn").forEach(b => {
      b.onclick = () => {
        const i = Number(b.dataset.i);
        customPhrases.splice(i, 1);
        localStorage.setItem("customPhrases", JSON.stringify(customPhrases));
        toast("Deleted");
        renderProgress();
      };
    });
    return;
  }

  panel.innerHTML = `
    <div class="panel">
      <h2>Your stats</h2>
      <p class="lead">
        Known + favorites + spaced review. Built-in jerga ships with MX audio.
        ${offline ? `<span class="offline-pill">Offline</span>` : `<span class="offline-pill" style="background:#fff;">Online ready</span>`}
      </p>
      <div class="stat-grid">
        <div class="stat"><b>${known}</b><span>Known</span></div>
        <div class="stat"><b>${favs}</b><span>Favorites</span></div>
        <div class="stat"><b>${due}</b><span>Due</span></div>
        <div class="stat"><b>${bestScore}</b><span>Best drill</span></div>
        <div class="stat"><b>${streakBest}</b><span>Best streak</span></div>
        <div class="stat"><b>${customCount}</b><span>Custom</span></div>
      </div>
      <div class="quiz-meta"><span>Banked · ${total} total</span><span>${pct}%</span></div>
      <div class="track"><i style="width:${pct}%"></i></div>
      <div class="btn-row">
        <button type="button" class="btn" id="goFlip">Flip cards</button>
        <button type="button" class="btn steel" id="goDrill">Start Drill</button>
        <button type="button" class="btn ghost" id="goReviewMore">Review due</button>
      </div>
      <div class="btn-row">
        <button type="button" class="btn ghost" id="clearKnown">Reset known</button>
        <button type="button" class="btn ghost" id="replayOnboard">Show tips</button>
      </div>
    </div>
  `;
  document.getElementById("goFlip").onclick = () => {
    currentView = "cards";
    quizMode = "mixed";
    document.querySelectorAll(".nav-btn").forEach(x => x.classList.toggle("on", x.dataset.view === "cards"));
    startCards(true);
  };
  document.getElementById("goDrill").onclick = () => {
    currentView = "quiz";
    quizMode = "mixed";
    document.querySelectorAll(".nav-btn").forEach(x => x.classList.toggle("on", x.dataset.view === "quiz"));
    startQuiz(true);
  };
  document.getElementById("goReviewMore").onclick = () => {
    currentView = "quiz";
    quizMode = "review";
    document.querySelectorAll(".nav-btn").forEach(x => x.classList.toggle("on", x.dataset.view === "quiz"));
    startQuiz(true);
  };
  document.getElementById("clearKnown").onclick = () => {
    knownIds = new Set();
    persistKnown();
    toast("Known list cleared");
    renderProgress();
  };
  document.getElementById("replayOnboard").onclick = () => {
    onboarded = false;
    onboardStep = 0;
    localStorage.removeItem("onboarded");
    renderOnboard();
  };
}

function render() {
  renderTabs();
  if (currentView === "home") renderHome();
  else if (currentView === "cards") startCards(true);
  else if (currentView === "quiz") startQuiz(true);
  else if (currentView === "add") renderAdd();
  else if (currentView === "progress") renderProgress();
}

document.querySelectorAll(".nav-btn").forEach(b => {
  b.onclick = () => {
    stopAudio();
    const toastEl = document.getElementById("toast");
    toastEl.classList.remove("show");
    clearTimeout(toast._t);
    document.querySelectorAll(".nav-btn").forEach(x => x.classList.remove("on"));
    b.classList.add("on");
    currentView = b.dataset.view;
    currentCat = "all";
    if (currentView !== "quiz" && currentView !== "cards") quizMode = "mixed";
    searchEl.value = "";
    render();
  };
});

searchEl.oninput = () => {
  if (currentView === "home") renderHome();
};

render();
renderOnboard();

function hideSplash() {
  const el = document.getElementById("splash");
  if (!el || el.classList.contains("hide")) return;
  el.classList.add("hide");
  const done = () => { if (el.parentNode) el.remove(); };
  el.addEventListener("transitionend", done, { once: true });
  setTimeout(done, 700);
}
if (!new URLSearchParams(location.search).has("splash")) {
  window.addEventListener("load", () => setTimeout(hideSplash, 500));
  setTimeout(hideSplash, 2500);
}

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("./sw.js").catch(() => {});
  });
}
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="description" content="Jerga de obra for construction crews — safety, tools, and unfiltered shop talk with Mexican Spanish audio.">
<title>Jerga de Obra</title>
<link rel="manifest" href="manifest.json">
<link rel="icon" href="icon.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="theme-color" content="#FFD100">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Jerga de Obra">
<meta property="og:type" content="website">
<meta property="og:title" content="Jerga de Obra">
<meta property="og:description" content="Unfiltered Spanish for construction crews — jerga de obra, not tourist Spanish.">
<meta property="og:url" content="https://glenngerbrick-ship-it.github.io/jerga-de-obra/">
<meta property="og:image" content="https://glenngerbrick-ship-it.github.io/jerga-de-obra/cover.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Jerga de Obra">
<meta name="twitter:description" content="Unfiltered Spanish for construction crews — jerga de obra, not tourist Spanish.">
<meta name="twitter:image" content="https://glenngerbrick-ship-it.github.io/jerga-de-obra/cover.png">
<link rel="apple-touch-startup-image" media="(device-width: 440px) and (device-height: 956px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)" href="splash/1320x2868.png">
<link rel="apple-touch-startup-image" media="(device-width: 430px) and (device-height: 932px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)" href="splash/1290x2796.png">
<link rel="apple-touch-startup-image" media="(device-width: 402px) and (device-height: 874px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)" href="splash/1206x2622.png">
<link rel="apple-touch-startup-image" media="(device-width: 393px) and (device-height: 852px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)" href="splash/1179x2556.png">
<link rel="apple-touch-startup-image" media="(device-width: 390px) and (device-height: 844px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)" href="splash/1170x2532.png">
<link rel="apple-touch-startup-image" media="(device-width: 428px) and (device-height: 926px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)" href="splash/1284x2778.png">
<link rel="apple-touch-startup-image" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)" href="splash/1242x2688.png">
<link rel="apple-touch-startup-image" media="(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)" href="splash/1125x2436.png">
<link rel="apple-touch-startup-image" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)" href="splash/828x1792.png">
<link rel="apple-touch-startup-image" media="(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)" href="splash/750x1334.png">
<link rel="apple-touch-startup-image" media="(device-width: 414px) and (device-height: 736px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)" href="splash/1242x2208.png">
<link rel="apple-touch-startup-image" media="(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)" href="splash/2048x2732.png">
<link rel="apple-touch-startup-image" media="(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)" href="splash/1668x2388.png">
<link rel="apple-touch-startup-image" media="(device-width: 820px) and (device-height: 1180px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)" href="splash/1640x2360.png">
<link rel="apple-touch-startup-image" media="(device-width: 810px) and (device-height: 1080px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)" href="splash/1620x2160.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{CSS_FULL}
</head>
<body>
<div id="splash" class="splash" role="status" aria-label="Jerga de Obra">
  <div class="splash-mark">
    <img src="icon-512.png" alt="" width="512" height="512">
  </div>
  <p class="splash-title">JERGA <em>DE OBRA</em></p>
  <p class="splash-tag">Crew slang. Not tourist Spanish.</p>
</div>
<div class="app">
  <header class="top">
    <div class="brand-row">
      <img src="icon.png" alt="" class="logo" width="56" height="56">
      <div class="brand-text">
        <h1>JERGA <em>DE OBRA</em></h1>
        <p class="tagline">Crew slang. Not tourist Spanish.</p>
      </div>
    </div>
    <div class="search-wrap" id="searchWrap">
      <span class="mag" aria-hidden="true"></span>
      <input type="search" id="search" placeholder="Search jerga, tools, slang…" autocomplete="off" enterkeyhint="search">
    </div>
  </header>

  <nav class="rail" id="categoryTabs" aria-label="Categories"></nav>
  <main id="mainContent"></main>
</div>

<nav class="bottom-nav" aria-label="Primary">
  <button class="nav-btn on" data-view="home"><span class="glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11.5 12 4l8 7.5"/><path d="M6.5 10.2V20h11V10.2"/><path d="M10 20v-6h4v6"/></svg></span>Home</button>
  <button class="nav-btn" data-view="cards"><span class="glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="8" y="3" width="11" height="14" rx="2"/><path d="M16 17v1a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h1"/></svg></span>Flip</button>
  <button class="nav-btn" data-view="quiz"><span class="glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="1.25" fill="currentColor" stroke="none"/></svg></span>Drill</button>
  <button class="nav-btn" data-view="add"><span class="glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg></span>Add</button>
  <button class="nav-btn" data-view="progress"><span class="glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><circle cx="5.5" cy="12" r="1.7"/><circle cx="12" cy="12" r="1.7"/><circle cx="18.5" cy="12" r="1.7"/></svg></span>More</button>
</nav>
<div class="toast" id="toast" role="status"></div>
<div class="onboard" id="onboard" hidden></div>

<script src="phrases.js"></script>
<script>
{JS}
</script>
</body>
</html>
"""

ROOT.joinpath("index.html").write_text(html, encoding="utf-8")
print("wrote index.html", len(html), "chars")
