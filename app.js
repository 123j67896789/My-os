const windows = [...document.querySelectorAll('.window')];
const runningApps = document.getElementById('running-apps');
const clock = document.getElementById('clock');
const frame = document.getElementById('scramjet-frame');

const SCRAMJET_HOME = 'https://scramjet.org';

function showWindow(id) {
  const win = document.getElementById(id);
  if (!win) return;
  win.classList.remove('hidden');
  renderRunning();
}

function hideWindow(id) {
  const win = document.getElementById(id);
  if (!win) return;
  win.classList.add('hidden');
  renderRunning();
}

function renderRunning() {
  const open = windows.filter((w) => !w.classList.contains('hidden'));
  runningApps.innerHTML = open
    .map((w) => `<span class="task-pill">${w.querySelector('h2').textContent}</span>`)
    .join('');
}

for (const icon of document.querySelectorAll('.desktop-icon')) {
  icon.addEventListener('click', () => showWindow(icon.dataset.open));
}
for (const btn of document.querySelectorAll('[data-minimize]')) {
  btn.addEventListener('click', () => hideWindow(btn.dataset.minimize));
}

document.getElementById('open-scramjet-home').addEventListener('click', () => {
  frame.src = SCRAMJET_HOME;
});

document.getElementById('open-scramjet-url').addEventListener('click', () => {
  const url = document.getElementById('scramjet-url').value.trim();
  if (!/^https?:\/\//.test(url)) {
    alert('Please enter a full URL starting with http:// or https://');
    return;
  }
  frame.src = url;
});

function updateClock() {
  clock.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}
setInterval(updateClock, 1000);
updateClock();

// Default open apps
showWindow('browser-window');
hideWindow('apps-window');
hideWindow('about-window');
frame.src = SCRAMJET_HOME;
