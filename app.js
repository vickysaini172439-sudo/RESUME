(function () {
var root = document.documentElement;
var btn = document.getElementById('theme-toggle');
try { var saved = localStorage.getItem('vs-theme'); if (saved) root.setAttribute('data-theme', saved); } catch (e) {}
btn.addEventListener('click', function () {
var current = root.getAttribute('data-theme') ||
(window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
var next = current === 'light' ? 'dark' : 'light';
root.setAttribute('data-theme', next);
try { localStorage.setItem('vs-theme', next); } catch (e) {}
});
var toast = document.getElementById('toast');
function show(msg) { toast.textContent = msg; toast.classList.add('show'); setTimeout(function () { toast.classList.remove('show'); }, 1800); }
document.getElementById('copy-email').addEventListener('click', function () {
var text = document.getElementById('email').textContent.trim();
var done = function () { show('Email copied'); };
var fallback = function () {
var r = document.createRange(); r.selectNodeContents(document.getElementById('email'));
var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
show('Email selected. Press Ctrl+C to copy');
};
if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(text).then(done, fallback); } else { fallback(); }
});
document.getElementById('year').textContent = new Date().getFullYear();
if (window.QRCode) { new QRCode(document.getElementById('qr'), { text: 'https://vicky-cse.vercel.app', width: 440, height: 440, colorDark: '#0F1420', colorLight: '#ffffff', correctLevel: QRCode.CorrectLevel.H }); }
var links = document.querySelectorAll('.nav-links a');
var map = {};
links.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
if ('IntersectionObserver' in window) {
var io = new IntersectionObserver(function (entries) {
entries.forEach(function (en) {
if (en.isIntersecting && map[en.target.id]) {
links.forEach(function (l) { l.classList.remove('active'); });
map[en.target.id].classList.add('active');
}
});
}, { rootMargin: '-45% 0px -50% 0px' });
document.querySelectorAll('section[id]').forEach(function (s) { io.observe(s); });
}
var dlg = document.getElementById('viewer');
var vimg = document.getElementById('viewer-img');
var vcap = document.getElementById('viewer-cap');
document.querySelectorAll('[data-full]').forEach(function (b) {
b.addEventListener('click', function () {
vimg.src = b.getAttribute('data-full');
vimg.alt = b.getAttribute('data-caption') || '';
vcap.textContent = b.getAttribute('data-caption') || '';
if (dlg.showModal) { dlg.showModal(); } else { window.open(vimg.src, '_blank', 'noopener'); }
});
});
document.getElementById('viewer-close').addEventListener('click', function () { dlg.close(); });
dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
document.querySelectorAll('.card').forEach(function (c) {
c.addEventListener('pointermove', function (e) {
var r = c.getBoundingClientRect();
var x = e.clientX - r.left, y = e.clientY - r.top;
c.style.setProperty('--mx', x + 'px'); c.style.setProperty('--my', y + 'px');
if (finePointer && !reduce && r.width < 700) {
c.classList.add('tilt');
var rx = ((y / r.height) - 0.5) * -6, ry = ((x / r.width) - 0.5) * 6;
c.style.transform = 'perspective(900px) rotateX(' + rx.toFixed(2) + 'deg) rotateY(' + ry.toFixed(2) + 'deg) translateY(-4px)';
}
});
c.addEventListener('pointerleave', function () { c.style.transform = ''; c.classList.remove('tilt'); });
});
var filters = document.querySelectorAll('.filter');
var apps = document.querySelectorAll('.app[data-tags]');
filters.forEach(function (f) {
f.addEventListener('click', function () {
var key = f.getAttribute('data-filter');
filters.forEach(function (o) { o.setAttribute('aria-pressed', o === f ? 'true' : 'false'); });
apps.forEach(function (a) {
var match = key === 'all' || (' ' + a.getAttribute('data-tags') + ' ').indexOf(' ' + key + ' ') > -1;
a.classList.toggle('is-dim', !match);
});
});
});
function countUp(el) {
var to = parseFloat(el.getAttribute('data-to')), dec = parseInt(el.getAttribute('data-dec') || '0', 10), suf = el.getAttribute('data-suffix') || '';
var start = null, dur = 1200;
function step(t) {
if (!start) start = t;
var k = Math.min((t - start) / dur, 1), v = to * (1 - Math.pow(1 - k, 3));
el.textContent = v.toFixed(dec) + suf;
if (k < 1) requestAnimationFrame(step);
}
requestAnimationFrame(step);
}
if (!reduce && 'IntersectionObserver' in window) {
var co = new IntersectionObserver(function (entries) {
entries.forEach(function (en) { if (en.isIntersecting) { countUp(en.target); co.unobserve(en.target); } });
}, { threshold: 0.6 });
document.querySelectorAll('.count').forEach(function (el) { co.observe(el); });
}
var bar = document.getElementById('progress');
var top = document.getElementById('to-top');
var ticking = false;
function onScroll() {
var h = document.documentElement.scrollHeight - window.innerHeight;
var y = window.scrollY || window.pageYOffset;
bar.style.transform = 'scaleX(' + (h > 0 ? y / h : 0) + ')';
top.classList.toggle('show', y > 700);
ticking = false;
}
window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
onScroll();
top.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); });
})();
