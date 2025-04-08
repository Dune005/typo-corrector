<template>
  <div class="container">
    <h1>Typo-Corrector MVP</h1>
    
    <div class="text-areas">
      <div class="area">
        <label for="input-text">Eingabe:</label>
        <textarea id="input-text" v-model="inputText" rows="10" placeholder="Text hier eingeben..."></textarea>
      </div>
      <div class="area">
        <label for="output-text">Ausgabe:</label>
        <textarea id="output-text" v-model="outputText" rows="10" readonly placeholder="Korrigierter Text..."></textarea>
      </div>
    </div>
    <button @click="correctText" :disabled="isLoading">
      {{ isLoading ? 'Korrigiere...' : 'Korrigieren' }}
    </button>
    <p v-if="error" class="error-message">{{ error }}</p>
    
    <NuxtLink to="/experiment">Zur Experimentierseite</NuxtLink>
  </div>
  
</template>

<script setup>
import { ref } from 'vue';

const inputText = ref('');
const outputText = ref('');
const isLoading = ref(false);
const error = ref('');

// Stelle sicher, dass der Port mit deinem Backend übereinstimmt (du hast 5001 erwähnt)
const backendUrl = 'http://localhost:5001/correct';

async function correctText() {
  isLoading.value = true;
  error.value = '';
  outputText.value = ''; // Ausgabe leeren

  try {
    const response = await fetch(backendUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: inputText.value }),
    });

    if (!response.ok) {
      // Versuche, die Fehlermeldung vom Backend zu lesen
      let errorData;
      try {
        errorData = await response.json();
      } catch (e) {
        // Wenn die Antwort kein JSON ist
        throw new Error(`HTTP-Fehler ${response.status}: ${response.statusText}`);
      }
      throw new Error(`Fehler vom Backend: ${errorData.description || response.statusText}`);
    }

    const data = await response.json();
    outputText.value = data.corrected_text;

  } catch (err) {
    console.error('Fehler beim Aufrufen der API:', err);
    error.value = `Fehler: ${err.message}`;
  } finally {
    isLoading.value = false;
  }
}
</script>

<style>
body {
  font-family: sans-serif;
  margin: 2em;
  background-color: #f4f4f4;
}

.container {
  background-color: #fff;
  padding: 2em;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  margin: auto;
}

h1 {
  text-align: center;
  color: #333;
  margin-bottom: 1em;
}

.text-areas {
  display: flex;
  gap: 1em;
  margin-bottom: 1em;
}

.area {
  flex: 1;
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 0.5em;
  font-weight: bold;
  color: #555;
}

textarea {
  width: 100%;
  padding: 0.8em;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1em;
  box-sizing: border-box; /* Verhindert, dass Padding die Breite beeinflusst */
  resize: vertical; /* Erlaubt nur vertikales Vergrößern */
}

textarea[readonly] {
  background-color: #e9e9e9;
  cursor: not-allowed;
}

button {
  display: block;
  width: 100%;
  padding: 0.8em 1em;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1.1em;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

button:not(:disabled):hover {
  background-color: #0056b3;
}

.error-message {
  color: red;
  margin-top: 1em;
  text-align: center;
}
</style>
