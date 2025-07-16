function updateTime() {
    const now = new Date();
    document.getElementById("live-time").innerText = now.toLocaleTimeString();
}

setInterval(updateTime, 1000);

// Hydration reminder every 2 hours
setInterval(() => {
    alert("💧 Time to hydrate! Drink some water!");
}, 2 * 60 * 60 * 1000);
