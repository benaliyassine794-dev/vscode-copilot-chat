// Tab switching
document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    if (tab.classList.contains('tab-search')) return;
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
  });
});

// Filter pills
document.querySelectorAll('.pill').forEach(pill => {
  pill.addEventListener('click', () => {
    document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
  });
});

// Subscribe button toggle
const subscribeBtn = document.querySelector('.btn-subscribe');
let subscribed = false;
subscribeBtn.addEventListener('click', () => {
  subscribed = !subscribed;
  subscribeBtn.textContent = subscribed ? 'مشترك ✓' : 'اشترك';
  subscribeBtn.style.background = subscribed ? '#272727' : '#f1f1f1';
  subscribeBtn.style.color = subscribed ? '#f1f1f1' : '#0f0f0f';
});

// Video card click effect
document.querySelectorAll('.video-card').forEach(card => {
  card.addEventListener('click', () => {
    const title = card.querySelector('.video-title').textContent;
    console.log('Playing:', title);
  });
});
