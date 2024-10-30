function toggleVisibility(showElement, hideElement) {
    document.getElementById(showElement).style.display = "block";
    document.getElementById(hideElement).style.display = "none";
}

function toggleButtonColors(activeButton, inactiveButton) {
    document.getElementById(activeButton).style.backgroundColor = "var(--secondary-color)";
    document.getElementById(inactiveButton).style.backgroundColor = "var(--primary-color)";
}

function mostrarRegistro() {
    toggleVisibility("registro", "login");
    toggleVisibility("libro1", "libro2");
    toggleButtonColors("register-button", "login-button");
}

function mostrarLogin() {
    toggleVisibility("login", "registro");
    toggleVisibility("libro2", "libro1");
    toggleButtonColors("login-button", "register-button");
}

