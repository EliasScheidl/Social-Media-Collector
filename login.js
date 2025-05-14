document.getElementById('loginForm').addEventListener('submit', function(event) {
document.getElementById('loginForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const username = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value.trim();
            const errorDiv = document.getElementById('loginError');
            if (!username || !password) {
                errorDiv.textContent = 'Bitte geben Sie sowohl Benutzername als auch Passwort ein. Dies hilft, Fehler beim Anmelden zu vermeiden.';
                errorDiv.classList.remove('d-none');
                return;
            }
            // Simulate form submission (replace with real AJAX or remove event.preventDefault for real submit)
            // For demonstration, always show error
            errorDiv.textContent = 'Anmeldung fehlgeschlagen. Überprüfen Sie Ihre Eingaben und versuchen Sie es erneut. Falls Sie Hilfe benötigen, lesen Sie die Hinweise oder wenden Sie sich an den Administrator.';
            errorDiv.classList.remove('d-none');
            });
});