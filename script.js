document.getElementById("analyzeBtn").addEventListener("click", async () => {
    const newsText = document.getElementById("newsInput").value.trim();
    const loadingIndicator = document.getElementById("loadingIndicator");
    const resultSection = document.getElementById("resultSection");
    const result = document.getElementById("result");
    const confidence = document.getElementById("confidence");
    const explanationList = document.getElementById("explanationList");

    // Reset UI
    resultSection.classList.add("hidden");
    explanationList.innerHTML = "";

    if (!newsText) {
        alert("Please paste a news article to analyze.");
        return;
    }

    try {
        // Show loading indicator
        loadingIndicator.classList.remove("hidden");

        // Fetch the prediction from the backend
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ text: newsText }),
        });

        const data = await response.json();

        // Hide loading indicator
        loadingIndicator.classList.add("hidden");

        if (response.ok) {
            // Update the result
            result.textContent = data.result;
            confidence.textContent = data.confidence;

            // Add example explanation (customize for your model logic)
            explanationList.innerHTML = `
                <li>Unverified sources or claims</li>
                <li>Bias in language or exaggerated statements</li>
                <li>Patterns resembling fake news dataset</li>
            `;
            resultSection.classList.remove("hidden");
        } else {
            throw new Error(data.error || "Failed to get a valid response.");
        }
    } catch (error) {
        loadingIndicator.classList.add("hidden");
        alert("An error occurred: " + error.message);
    }
});
// Particle Animation on Canvas
const canvas = document.getElementById("backgroundCanvas");
const ctx = canvas.getContext("2d");

// Resize canvas to fit the window
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Array to store particles
const particles = [];

// Particle properties
const numParticles = 100;
const particleSize = 3;
const particleSpeed = 1.5;

// Create particles
for (let i = 0; i < numParticles; i++) {
    particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        dx: (Math.random() - 0.5) * particleSpeed,
        dy: (Math.random() - 0.5) * particleSpeed,
    });
}

// Draw particles
function drawParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "rgba(255, 255, 255, 0.8)";

    particles.forEach((particle) => {
        ctx.beginPath();
        ctx.arc(particle.x, particle.y, particleSize, 0, Math.PI * 2);
        ctx.fill();
    });
}

// Update particle positions
function updateParticles() {
    particles.forEach((particle) => {
        particle.x += particle.dx;
        particle.y += particle.dy;

        // Bounce particles off edges
        if (particle.x < 0 || particle.x > canvas.width) particle.dx *= -1;
        if (particle.y < 0 || particle.y > canvas.height) particle.dy *= -1;
    });
}

// Animation loop
function animate() {
    drawParticles();
    updateParticles();
    requestAnimationFrame(animate);
}

// Adjust canvas size on window resize
window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

// Start animation
animate();
