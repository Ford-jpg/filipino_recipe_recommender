const API_URL = "http://127.0.0.1:5000/api";

// Function to display results, including loading and error messages
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

// Fetch all recipes
async function fetchAllRecipes() {
    displayResults("all-recipes", [], true);
    try {
        const response = await fetch(`${API_URL}/recipes`);
        if (!response.ok) throw new Error("Network response was not ok");
        const recipes = await response.json();
        displayResults("all-recipes", recipes);
    } catch (error) {
        displayResults("all-recipes", [], false, error.message);
    }
}

// Search recipes by ingredients
async function searchByIngredients() {
    const ingredients = document.getElementById("ingredient-input").value.split(",").map(ing => ing.trim());
    displayResults("ingredient-results", [], true);
    try {
        const response = await fetch(`${API_URL}/recipes/search`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ ingredients })
        });
        if (!response.ok) throw new Error("Failed to fetch recipes by ingredients");
        const results = await response.json();
        displayResults("ingredient-results", results);
    } catch (error) {
        displayResults("ingredient-results", [], false, error.message);
    }
}

// Search recipes based on prompt
async function searchByPrompt() {
    const prompt = document.getElementById("prompt-input").value;
    displayResults("prompt-results", [], true);
    try {
        const response = await fetch(`${API_URL}/recipes/prompt_search`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt })
        });
        if (!response.ok) throw new Error("Failed to fetch recipes by prompt");
        const results = await response.json();
        displayResults("prompt-results", results);
    } catch (error) {
        displayResults("prompt-results", [], false, error.message);
    }
}

// Optional: Debugging message to confirm script.js is loaded
console.log("script.js loaded");
