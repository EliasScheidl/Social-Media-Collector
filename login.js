document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Create a form data object to send the plain password and username
    const formData = new FormData();
    formData.append('n', username);
    formData.append('pw', password);

    // Send the data to the server
    fetch(this.action, {
        method: 'POST',
        body: formData
    }).then(response => {
        if (response.ok) {
            // Handle successful login
            alert('Login successful');
        } else {
            // Handle login failure
            alert('Login failed');
        }
    }).catch(error => {
        console.error('Error:', error);
        alert('An error occurred');
    });
});