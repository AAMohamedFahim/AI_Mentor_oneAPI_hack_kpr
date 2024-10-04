document.addEventListener('DOMContentLoaded', function() {
    const profileIcon = document.getElementById('profileIcon');
    const profilePopup = document.getElementById('profilePopup');
    const closeBtn = profilePopup.querySelector('.close');

    profileIcon.addEventListener('click', function(e) {
        e.preventDefault();
        profilePopup.style.display = 'block';
    });

    closeBtn.addEventListener('click', function() {
        profilePopup.style.display = 'none';
    });

    window.addEventListener('click', function(e) {
        if (e.target === profilePopup) {
            profilePopup.style.display = 'none';
        }
    });
});