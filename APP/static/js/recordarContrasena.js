// recordarContrasena.js
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("recoveryForm")

    if (form) {
        form.addEventListener("submit", function (e) {
            e.preventDefault()
            console.log("Formulario enviado")

            const formData = new FormData(this)

            fetch("/recoveringPass", {
                method: "POST",
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    console.log("Datos recibidos:", data)
                    showNotification(data)
                })
                .catch(error => {
                    console.error("Error:", error)
                    showNotification({
                        resultado: "error",
                        mensaje: "Error de conexión",
                    })
                })
        })
    }
})

function showNotification(data) {
    const notification = document.getElementById("notification")
    const notificationMessage = document.getElementById("notificationMessage")

    if (!notification || !notificationMessage) {
        console.error("Elementos de notificación no encontrados")
        return
    }

    // Limpiar cualquier clase previa
    notification.className = "notification"

    // Establecer el mensaje
    notificationMessage.textContent =
        data.mensaje ||
        (data.resultado === "success"
            ? "Operación exitosa"
            : "Error en la operación")

    // Establecer el tipo y hacer visible
    notification.className = `notification ${data.resultado} visible`

    // Asegurar que sea visible
    notification.style.display = "flex"
    notification.style.opacity = "1"

    console.log("Notificación mostrada:", notification.className)

    // Ocultar después de 3 segundos
    setTimeout(hideNotification, 3000)
}

function hideNotification() {
    const notification = document.getElementById("notification")
    if (notification) {
        notification.className = "notification"
        notification.style.opacity = "0"

        // Ocultar completamente después de la transición
        setTimeout(() => {
            notification.style.display = "none"
        }, 300)
    }
}

// Función de prueba
function testNotification() {
    showNotification({
        resultado: "success",
        mensaje: "Esto es una prueba de notificación exitosa",
    })
}
