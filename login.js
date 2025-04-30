document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("loginForm");
    form.action = `${window.location.origin}/interact/auth`; // Set form action to the current server's origin with /interact/auth

    form.addEventListener("submit", async (event) => {
        event.preventDefault(); // Prevent default form submission
        const passwordField = document.getElementById("password");
        const password = passwordField.value;

        try {
            const hash = await argon2.hash({
                pass: password,
                salt: crypto.getRandomValues(new Uint8Array(16)),
                type: argon2.ArgonType.Argon2id,
                hashLen: 32, // Length of the hash
                time: 3, // Number of iterations
                mem: 65536, // Memory usage in KiB
                parallelism: 1 // Number of threads
            });

            passwordField.value = hash.encoded; // Replace the password with the hashed version
            form.submit(); // Submit the form
        } catch (error) {
            console.error("Error hashing password:", error);
            alert("An error occurred while processing your request. Please try again.");
        }
    });
});