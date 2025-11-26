document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("artistMusic");
    const outputDiv = document.getElementById("lyricsDiv");

    input.addEventListener("keydown", async (e) => {
        if (e.key !== "Enter") return;

        const q = input.value.trim();
        if (!q) return;

        const res = await fetch(`/api/recipes/search?q=${encodeURIComponent(q)}&type=title`);
        const data = await res.json();

        outputDiv.style.visibility = "visible";

        outputDiv.innerHTML = data.length
            ? data.map(item => `
                <div style="margin: 10px; padding: 10px; border: 1px solid #00ffe1; border-radius: 8px;">
                    <h3>${item.title}</h3>
                    <p>${item.description || ""}</p>
                </div>
              `).join("")
            : "<p>No results found.</p>";
    });
});
