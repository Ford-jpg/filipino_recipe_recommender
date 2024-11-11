const API_URL = "http://127.0.0.1:5000/api";

async function unifiedSearch() {
    const prompt = document.getElementById("search-input").value;
    displayResults("search-results", [], true); // Show loading indicator

    try {
        // Send the prompt to the backend's unified prompt search endpoint
        const response = await fetch(`${API_URL}/recipes/prompt_search`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt })
        });

        const results = await response.json();
        displayResults("search-results", results);
    } catch (error) {
        displayResults("search-results", [], false, error.message);
    }
}

function displayResults(elementId, data, isLoading = false, error = '') {
    const container = document.getElementById(elementId);
    container.innerHTML = "";

    if (isLoading) {
        container.innerHTML = `<p class="loading">Loading...</p>`;
        return;
    }

    if (error) {
        container.innerHTML = `<p class="error">Error: ${error}</p>`;
        return;
    }

    if (Array.isArray(data) && data.length > 0) {
        data.forEach(item => {
            const div = document.createElement("div");
            div.className = "recipe";
            div.innerHTML = `<strong>${item.title}</strong>: ${item.description || 'No description'}`;
            container.appendChild(div);
        });
    } else {
        container.innerHTML = "<p>No recipes found.</p>";
    }
}
