<template>
  <div class="container">
    <!-- Navigation Bar -->
    <nav class="navbar">
      <div class="logo-container">
        <div class="logo">Logo</div>
      </div>
      <div class="nav-links">
        <a href="#" class="nav-link">Features</a>
        <a href="#" class="nav-link">Podcasts</a>
        <a href="#" class="nav-link">Pricing</a>
      </div>
      <div class="login-button-container">
        <button class="login-button">Login</button>
      </div>
    </nav>

    <!-- Main Content -->
    <main>
      <h1 class="main-title" style="color: rgb(0, 0, 0);">Best Typo Corrector</h1>
      <h1 class="main-title">Worldwide</h1>

      <!-- Mode Toggle -->
      <div class="mode-toggle">
        <button
          class="mode-button active"
        >Casual</button>
        <button
          class="mode-button disabled"
          title="Coming soon!"
        >Expert</button>
      </div>

      <!-- Text Areas -->
      <div class="text-areas">
        <div class="text-area-container">
          <label for="input-text">Eingabe</label>
          <textarea
            id="input-text"
            v-model="inputText"
            placeholder="Text hier eingeben..."
          ></textarea>
        </div>
        <div class="text-area-container">
          <label for="output-text">Ausgabe</label>
          <textarea
            id="output-text"
            v-model="outputText"
            placeholder="Korrigierter Text..."
            readonly
          ></textarea>
          <div class="copy-icon" @click="copyToClipboard" v-if="outputText">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
              <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
            </svg>
          </div>
        </div>
      </div>

      <!-- Controls Container -->
      <div class="controls-container">
        <!-- Settings Icon (Left aligned) -->
        <div class="settings-container">
          <div class="settings-icon" @click="toggleSettings">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="3"></circle>
              <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
            </svg>
            <span>Optionen</span>
          </div>

          <!-- Settings Panel -->
          <div class="settings-panel" v-if="showSettings">
            <h3>Einstellungen</h3>
            <div class="settings-option">
              <input type="checkbox" id="preserve-formatting" v-model="preserveFormatting">
              <label for="preserve-formatting">Formatierung beibehalten</label>
            </div>
            <!-- Hier können in Zukunft weitere Optionen hinzugefügt werden -->
          </div>
        </div>

        <!-- Correct Button (Center aligned) -->
        <div class="button-container">
          <button
            class="correct-button"
            @click="correctText"
            :disabled="isLoading"
          >
            {{ isLoading ? 'Correcting...' : 'Correct' }}
          </button>
        </div>
      </div>

      <!-- Error Message -->
      <div class="error-container" v-if="error">
        <p class="error-message">{{ error }}</p>
      </div>

      <!-- Expert Mode Section -->
      <div class="expert-mode-section">
        <h2 style="color: rgb(0, 0, 0);">Expert Mode</h2>
        <p>
          Aktiviere präzise Kontrolle über jede Korrekturegel.
          Behalte Formatierungen bei, sieh Änderungen in Echtzeit
          und exportiere deinen Text direkt als HTML oder
          Markdown.
        </p>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const inputText = ref('');
const outputText = ref('');
const isLoading = ref(false);
const error = ref('');
const preserveFormatting = ref(false);
const showSettings = ref(false);

// Funktion zum Ein-/Ausblenden der Einstellungen
function toggleSettings() {
  showSettings.value = !showSettings.value;
}

// Event-Listener zum Schließen des Einstellungsmenüs, wenn außerhalb geklickt wird
function closeSettingsOnClickOutside(event) {
  const settingsContainer = document.querySelector('.settings-container');
  if (showSettings.value && settingsContainer && !settingsContainer.contains(event.target)) {
    showSettings.value = false;
  }
}

// Event-Listener beim Mounten hinzufügen und beim Unmounten entfernen

onMounted(() => {
  document.addEventListener('click', closeSettingsOnClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', closeSettingsOnClickOutside);
});

// Backend URL
const backendUrl = 'http://localhost:5001/correct';

// Function to copy text to clipboard
function copyToClipboard() {
  if (outputText.value) {
    navigator.clipboard.writeText(outputText.value)
      .then(() => {
        alert('Text copied to clipboard!');
      })
      .catch(err => {
        console.error('Failed to copy text: ', err);
      });
  }
}

async function correctText() {
  isLoading.value = true;
  error.value = '';
  outputText.value = ''; // Clear output

  try {
    const response = await fetch(backendUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        text: inputText.value,
        preserve_formatting: preserveFormatting.value
      }),
    });

    if (!response.ok) {
      // Try to read error message from backend
      let errorData;
      try {
        errorData = await response.json();
      } catch (e) {
        // If response is not JSON
        throw new Error(`HTTP error ${response.status}: ${response.statusText}`);
      }
      throw new Error(`Error from backend: ${errorData.description || response.statusText}`);
    }

    const data = await response.json();
    outputText.value = data.corrected_text;

  } catch (err) {
    console.error('Error calling API:', err);
    error.value = `Error: ${err.message}`;
  } finally {
    isLoading.value = false;
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,200..900;1,7..72,200..900&display=swap');


:root {
  --primary-color: #4f46e5;
  --primary-hover: #000000;
  --secondary-color: #10b981;
  --bg-color: #f9fafb;
  --card-bg: #ffffff;
  --text-color: #1e293b;
  --text-light: #64748b;
  --border-radius: 12px;
  --shadow: 0 4px 12px rgb(0, 0, 0);
  --accent-gradient: linear-gradient(135deg, #4f46e5, #8b5cf6);
}

body {
  background-color: var(--bg-color);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: "Literata", serif;
  background-color: var(--bg-color);
  min-height: 100vh;
  color: var(--text-color);
}

/* Navigation Bar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 60px;
  padding: 15px 0;
}

.logo-container {
  flex: 1;
}

.logo {
  background: var(--accent-gradient);
  color: white;
  padding: 12px 24px;
  display: inline-block;
  text-align: center;
  width: 120px;
  border-radius: 8px;
  font-weight: 600;
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2);
}

.nav-links {
  flex: 2;
  display: flex;
  justify-content: center;
  gap: 30px;
}

.nav-link {
  text-decoration: none;
  color: var(--text-color);
  font-weight: 500;
  position: relative;
  padding: 5px 0;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: var(--primary-color);
}

.nav-link::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: var(--primary-color);
  transition: width 0.3s ease;
}

.nav-link:hover::after {
  width: 100%;
}

.login-button-container {
  flex: 1;
  display: flex;
  justify-content: flex-end;
}

.login-button {
  background-color: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2);
  min-width: 80px;
  max-width: 100px;
}

.login-button:hover {
  background-color: var(--primary-hover);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(79, 70, 229, 0.25);
}

/* Main Content */
main {
  padding: 20px 0;
}

.main-title {
  text-align: center;
  font-size: 3rem;
  margin: 0;
  line-height: 1.2;
  font-weight: 700;
  color: #000000;
  letter-spacing: -0.5px;
}

/* Mode Toggle */
.mode-toggle {
  display: flex;
  justify-content: center;
  margin: 40px 0;
  position: relative;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  border-radius: 24px;
  padding: 4px;
  background-color: #f3f4f6;
  width: fit-content;
  margin-left: auto;
  margin-right: auto;
}

.mode-button {
  background-color: #e5e7eb;
  border: none;
  padding: 10px 24px;
  cursor: pointer;
  border-radius: 20px;
  font-weight: 500;
  transition: all 0.3s ease;
  color: var(--text-color);
}

.mode-button.active {
  background-color: white;
  color: var(--primary-color);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.mode-button.disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Text Areas */
.text-areas {
  display: flex;
  gap: 30px;
  margin-bottom: 30px;
}

.text-area-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  position: relative;
  padding: 24px;
  border-radius: var(--border-radius);
  box-shadow: var(--shadow);
}

label {
  margin-bottom: 12px;
  font-weight: 600;
  color: var(--text-color);
  font-size: 1.1rem;
}

textarea {
  height: 500px;
  padding: 16px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  resize: none;
  font-family: 'Inter', sans-serif;
  font-size: 1rem;
  line-height: 1.6;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  background-color: #f8fafc;
}

textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.2);
}

.copy-icon {
  position: absolute;
  bottom: 36px;
  right: 36px;
  cursor: pointer;
  background-color: white;
  border-radius: 50%;
  padding: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.copy-icon:hover {
  transform: scale(1.1);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Controls Container */
.controls-container {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  width: 100%;
  max-width: 1200px;
  margin: 20px auto;
  padding: 0 24px;
  align-items: center;
}

/* Settings Container */
.settings-container {
  position: relative;
  grid-column: 1;
  justify-self: start;
}

.settings-icon {
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: #f8fafc;
  padding: 8px 16px;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
  cursor: pointer;
  transition: all 0.2s ease;
}

.settings-icon:hover {
  background-color: #f1f5f9;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.settings-icon svg {
  color: var(--text-color);
}

.settings-icon span {
  font-size: 0.9rem;
  color: var(--text-color);
}

.settings-panel {
  position: absolute;
  top: 100%;
  width: 300px;
  background-color: white;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 16px;
  margin-top: 8px;
  z-index: 10;
}

.settings-panel h3 {
  margin-top: 0;
  margin-bottom: 16px;
  font-size: 1.1rem;
  color: var(--text-color);
  border-bottom: 1px solid #e2e8f0;
  padding-bottom: 8px;
}

.settings-option {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.settings-option label {
  font-size: 0.9rem;
  color: var(--text-color);
  cursor: pointer;
}

.settings-option input[type="checkbox"] {
  cursor: pointer;
}

/* Correct Button */
.button-container {
  display: flex;
  justify-content: center;
  grid-column: 2;
}

.correct-button {
  background: black;
  color: rgb(255, 255, 255);
  border: none;
  padding: 12px 24px;
  border-radius: 50px;
  cursor: pointer;
  font-size: 1.1rem;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.25);
  letter-spacing: 0.5px;
  min-width: 120px;
  max-width: 160px;
}

.correct-button:hover {
  transform: translateY(-3px);
  box-shadow: black;
}

.correct-button:disabled {
  background: #a0aec0;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

/* Error Message */
.error-container {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.error-message {
  color: #e53e3e;
  font-size: 0.9rem;
  text-align: center;
  padding: 12px 20px;
  background-color: #fff5f5;
  border-radius: 8px;
  border: 1px solid #fed7d7;
  box-shadow: 0 2px 8px rgba(229, 62, 62, 0.1);
}

/* Expert Mode Section */
.expert-mode-section {
  background-color: white;
  border-radius: var(--border-radius);
  border: 1px solid #c7c7c7;  /* Hier wird die Kontur hinzugefügt */
  border-color: #c7c7c7;
  padding: 36px;
  max-width: 700px;
  margin: 40px auto 0;
  text-align: center;
  box-shadow: var(--shadow);
  position: relative;
  overflow: hidden;
}

.expert-mode-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: var(--accent-gradient);
}

.expert-mode-section h2 {
  margin-top: 0;
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 16px;
  color: black;
  display: inline-block;
}

.expert-mode-section p {
  color: var(--text-light);
  line-height: 1.8;
  font-size: 1.05rem;
  max-width: 80%;
  margin: 0 auto;
}

/* Responsive Design */
@media (max-width: 768px) {
  .text-areas {
    flex-direction: column;
  }

  .main-title {
    font-size: 2.5rem;
  }

  .expert-mode-section p {
    max-width: 100%;
  }
}
</style>

