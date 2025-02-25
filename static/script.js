document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("contactForm").addEventListener("submit", function (event) {
        event.preventDefault();  // Prevent normal form submission

        let formData = {
            name: document.getElementById("name").value,
            email: document.getElementById("email").value,
            favorite_painting: document.getElementById("favorite_painting").value
        };
        fetch("/submit_contact", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("responseMessage").innerText = data.message;  // Show success message
        })
        .catch(error => {
            console.error("Error:", error);
            document.getElementById("responseMessage").innerText = "There was an error submitting your form.";
        });
    });
});
let currentIndex = 0; // Track the current image
function nextImage() {
    let images = document.querySelectorAll('.slider-image'); // Get all images in the gallery
    // Hide the current image
    images[currentIndex].classList.remove('active');
    // Move to the next image, looping back to the first image if at the end
    currentIndex = (currentIndex + 1) % images.length;
    // Show the new current image
    images[currentIndex].classList.add('active');
}


