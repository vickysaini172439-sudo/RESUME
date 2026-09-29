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
})();
