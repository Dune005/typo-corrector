<template>
  <div class="landing-page">
    <!-- Navigation Bar (optional, kann später hinzugefügt werden) -->
    <!--
    <nav class="navbar">
      <div class="container">
        <div class="logo">Typo Corrector</div>
        <div class="nav-links">
          <a href="#features">Funktionen</a>
          <a href="#about">Über uns</a>
        </div>
      </div>
    </nav>
    -->

    <!-- Hero Section -->
    <header class="hero-section">
      <div class="container hero-content">
        <h1 class="main-headline">Präzise Textkorrektur für Schweizerdeutsch</h1>
        <p class="sub-headline">
          Unser intelligentes Tool korrigiert Tippfehler und Grammatikfehler in deinen Texten – schnell, zuverlässig und mit Stil. Wähle zwischen Casual- und Expertenmodus für perfekte Ergebnisse.
        </p>
        <NuxtLink to="/homepage-test" class="cta-button-windsurf">
          Jetzt Text korrigieren
           <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16" class="icon-arrow-small">
             <path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"/>
          </svg>
        </NuxtLink>
      </div>
      <div class="hero-background-gradient"></div>
    </header>

    <!-- Features Section -->
    <section id="features" class="features-section">
      <div class="container">
        <h2 class="section-title">Funktionen im Überblick</h2>
        <div class="features-grid">
          <div class="feature-card">
             <div class="feature-icon">
              <!-- Placeholder Icon -->
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16"><path d="M8 4.754a3.246 3.246 0 1 0 0 6.492 3.246 3.246 0 0 0 0-6.492zM5.754 8a2.246 2.246 0 1 1 4.492 0 2.246 2.246 0 0 1-4.492 0z"/><path d="M9.796 1.343c-.527-1.79-3.065-1.79-3.592 0l-.094.319a.873.873 0 0 1-1.255.52l-.292-.16c-1.64-.892-3.433.902-2.54 2.541l.159.292a.873.873 0 0 1-.52 1.255l-.319.094c-1.79.527-1.79 3.065 0 3.592l.319.094a.873.873 0 0 1 .52 1.255l-.16.292c-.892 1.64.901 3.434 2.541 2.54l.292-.159a.873.873 0 0 1 1.255.52l.094.319c.527 1.79 3.065 1.79 3.592 0l.094-.319a.873.873 0 0 1 1.255-.52l.292.16c1.64.893 3.434-.902 2.54-2.541l-.159-.292a.873.873 0 0 1 .52-1.255l.319-.094c1.79-.527 1.79-3.065 0-3.592l-.319-.094a.873.873 0 0 1-.52-1.255l.16-.292c.893-1.64-.902-3.433-2.541-2.54l-.292.159a.873.873 0 0 1-1.255-.52l-.094-.319z"/></svg>
            </div>
            <h3>Zwei Korrekturmodi</h3>
            <p>Wähle zwischen dem <strong>Casual-Modus</strong> für alltägliche Texte und dem kommenden <strong>Expertenmodus</strong> für präzise Kontrolle.</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">
              <!-- Placeholder Icon -->
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16"><path d="M1 3.5A1.5 1.5 0 0 1 2.5 2h11A1.5 1.5 0 0 1 15 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 1 12.5v-9zM2.5 3a.5.5 0 0 0-.5.5v9a.5.5 0 0 0 .5.5h11a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-11z"/><path d="M2 5.5a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-1z"/></svg>
            </div>
            <h3>Formatierung beibehalten</h3>
            <p>Optional kannst du die ursprüngliche Formatierung deines Textes während der Korrektur bewahren.</p>
          </div>
          <div class="feature-card">
             <div class="feature-icon">
               <!-- Placeholder Icon -->
               <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16"><path d="M11.854.146a.5.5 0 0 1 .11.54l-2 7A.5.5 0 0 1 9.5 8h-1a.5.5 0 0 1-.474-.334L6.5 3.236V13a.5.5 0 0 1-1 0V3.236L4.026 7.666A.5.5 0 0 1 3.5 8h-1a.5.5 0 0 1-.474-.666l2-7a.5.5 0 0 1 .11-.123h1.17a.5.5 0 0 1 .318.098l1.88 1.88L9.36 1.243A.5.5 0 0 1 9.5 1h1.17a.5.5 0 0 1 .318.098l1.88 1.88L14.36.243a.5.5 0 0 1 .54-.11z"/></svg>
            </div>
            <h3>Einfache Bedienung</h3>
            <p>Gib deinen Text ein, klicke auf "Korrigieren" und erhalte sofort das Ergebnis. Kopiere es mit einem Klick.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Image Placeholder Section -->
    <section class="image-placeholder-section">
      <div class="container">
         <h2 class="section-title">So einfach geht's</h2>
        <div class="placeholder-image">
           <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="currentColor" class="placeholder-icon" viewBox="0 0 16 16">
            <path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/>
            <path d="M2.002 1a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2h-12zm12 1a1 1 0 0 1 1 1v6.5l-3.777-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12V3a1 1 0 0 1 1-1h12z"/>
          </svg>
          <span>Hier könnte ein Screenshot deines Tools stehen</span>
        </div>
      </div>
    </section>

    <!-- Call to Action Section -->
    <section class="cta-section">
      <div class="container">
        <h2 class="section-title">Bereit für fehlerfreie Texte?</h2>
        <p>Starte jetzt und erlebe den Unterschied.</p>
        <NuxtLink to="/homepage-test" class="cta-button-windsurf">
          Kostenlos ausprobieren
           <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16" class="icon-arrow-small">
             <path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"/>
          </svg>
        </NuxtLink>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <div class="container">
        <p>&copy; {{ new Date().getFullYear() }} Typo Corrector. Alle Rechte vorbehalten.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
// Kein spezifisches JavaScript für diese statische Seite benötigt.
// NuxtLink wird automatisch von Nuxt 3 bereitgestellt.
import { NuxtLink } from '#components';
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400..700;1,7..72,400..700&display=swap');

:root {
  --primary-color: #0052cc; /* Angepasstes Blau */
  --primary-hover: #0041a3;
  --accent-color: #17a2b8; /* Teal Akzent */
  --bg-color: #b64747;
  --bg-light-gray: #f8f9fa;
  --bg-darker-gray: #e9ecef;
  --text-dark: #343a40; /* Dunklerer Text */
  --text-color: #495057; /* Standard Text */
  --text-muted: #6c757d; /* Hellerer Text */
  --border-color: #e0e0e0; /* Weichere Border */
  --border-radius: 12px; /* Grösserer Radius */
  --shadow: 0 6px 16px rgba(0, 0, 0, 0.08); /* Subtilerer Schatten */
  --shadow-hover: 0 10px 20px rgba(0, 0, 0, 0.12);
  --gradient-start: #f0f9ff; /* Hellerer Gradient */
  --gradient-end: #ffffff;
}

.landing-page {
  font-family: 'Literata', serif;
  background-color: var(--bg-color);
  color: var(--text-color);
  line-height: 1.7; /* Erhöhte Zeilenhöhe */
  letter-spacing: 0.2px; /* Leichtes Letter-Spacing */
}

.container {
  max-width: 1200px; /* Etwas breiter */
  margin: 0 auto;
  padding: 0 24px; /* Mehr Padding */
}

/* Section Title */
.section-title {
  text-align: center;
  font-size: 2.25rem; /* 36px */
  font-weight: 700;
  margin-bottom: 60px; /* Mehr Abstand */
  color: var(--text-dark);
}


/* Hero Section */
.hero-section {
  padding: 120px 0 100px; /* Mehr Padding */
  text-align: center;
  background-color: var(--bg-light-gray);
  position: relative;
  overflow: hidden;
}

.hero-content {
  position: relative;
  z-index: 2;
}

.main-headline {
  font-size: 3.5rem; /* 56px - Grösser */
  font-weight: 700;
  margin-bottom: 24px; /* Mehr Abstand */
  line-height: 1.25;
  color: var(--text-dark);
  letter-spacing: -0.5px;
}

.sub-headline {
  font-size: 1.25rem; /* 20px - Grösser */
  color: var(--text-color); /* Etwas dunkler */
  max-width: 750px; /* Etwas breiter */
  margin: 0 auto 48px; /* Mehr Abstand unten */
}

.cta-button {
  display: inline-flex;
  align-items: center;
  justify-content: center; /* Zentriert Inhalt */
  gap: 10px; /* Mehr Abstand zum Icon */
  padding: 14px 32px; /* Grösser */
  border-radius: var(--border-radius);
  text-decoration: none;
  font-weight: 600;
  font-size: 1.05rem; /* Leicht grösser */
  cursor: pointer;
  transition: all 0.3s ease; /* Umfassendere Transition */
  border: 1px solid rgba(0, 0, 0, 0.1); /* border + border-color mit Fallback */
  box-shadow: var(--shadow); /* Standard Schatten */
}

.cta-button.large {
    padding: 16px 40px;
    font-size: 1.1rem;
}

.cta-button.primary {
  background-color: var(--primary-color);
  color: rgb(0, 0, 0);
}

.cta-button.primary:hover {
  background-color: var(--primary-hover);
  transform: translateY(-3px); /* Stärkerer Hover-Effekt */
  box-shadow: var(--shadow-hover); /* Stärkerer Schatten */
}

.cta-button.secondary {
  background-color: white;
  color: var(--primary-color);
  border: 1px solid var(--border-color); /* Weichere Border */
}

.cta-button.secondary:hover {
  background-color: var(--bg-light-gray);
  border-color: var(--primary-color); /* Border-Farbe ändern */
  transform: translateY(-3px);
  box-shadow: var(--shadow-hover);
}

.cta-button .icon-arrow {
  transition: transform 0.3s ease;
  width: 18px; /* Icon Grösse angepasst */
  height: 18px;
}

.cta-button:hover .icon-arrow {
  transform: translateX(4px); /* Stärkere Bewegung */
}

/* Neuer Button im Windsurf-Stil */
.cta-button-windsurf {
  display: inline-flex;
  position: relative; /* Für potenzielle Pseudo-Elemente */
  align-items: center;
  justify-content: center;
  gap: 0.5rem; /* gap-2 */
  border-radius: 9999px; /* rounded-full */
  border: 1px solid transparent; /* Transparenter Rand initial */
  padding: 0.375rem 1rem; /* py-1.5 px-4 */
  font-size: 0.875rem; /* text-sm */
  letter-spacing: -0.025em; /* tracking-tight */
  color: #ffffff; /* Explizit Weiss */
  background-color: #000000; /* Explizit Schwarz */
  /* backdrop-filter: blur(4px); /* Entfernt, da Hintergrund opak */
  text-decoration: none;
  transition: all 0.3s ease-in-out;
  margin-top: 20px; /* Abstand zum oberen Button */
  cursor: pointer;
  box-shadow: var(--shadow); /* Standard Schatten hinzufügen */
  border: 1px solid var(--text-dark); /* Rand in gleicher Farbe */
  border: 1px solid #343a40; /* Rand in gleicher Farbe */
}

.cta-button-windsurf:hover {
  background-color: #495057; /* Helleres Grau beim Hover */
  border-color: #495057;
  box-shadow: var(--shadow-hover); /* Angepasster Schatten */
  transform: translateY(-2px);
}

.cta-button-windsurf .icon-arrow-small {
    width: 14px;
    height: 14px;
    transition: transform 0.3s ease;
}

.cta-button-windsurf:hover .icon-arrow-small {
  transform: translateX(3px);
}

/* Ensure SVG icon color is white */
.cta-button-windsurf svg {
  fill: #ffffff;
}

@media (min-width: 768px) {
  .cta-button-windsurf {
    font-size: 1rem; /* md:text-base */
  }
}

.hero-background-gradient {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, var(--gradient-start) 0%, var(--gradient-end) 70%); /* Angepasster Verlauf */
  opacity: 0.6; /* Leicht stärker */
  z-index: 1;
}

/* Features Section */
.features-section {
  padding: 100px 0; /* Mehr Padding */
  background-color: var(--bg-color);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 40px; /* Mehr Abstand */
}

.feature-card {
  background-color: white;
  padding: 40px; /* Mehr Padding */
  border-radius: var(--border-radius);
  box-shadow: var(--shadow);
  border: 1px solid var(--border-color);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex; /* Flexbox für Icon + Text */
  flex-direction: column; /* Inhalt untereinander */
  align-items: center; /* Zentriert Inhalt horizontal */
  text-align: center; /* Zentriert Text */
}

.feature-card:hover {
    transform: translateY(-8px); /* Stärkerer Hover */
    box-shadow: var(--shadow-hover);
}

.feature-icon {
  margin-bottom: 24px; /* Abstand Icon zum Text */
  color: var(--primary-color); /* Icon Farbe */
}

.feature-card h3 {
  font-size: 1.3rem; /* 21px */
  font-weight: 600;
  margin-bottom: 16px;
  color: var(--text-dark); /* Dunklerer Text */
}

.feature-card p {
  font-size: 1rem; /* 16px */
  color: var(--text-color); /* Standard Textfarbe */
}

/* Image Placeholder Section */
.image-placeholder-section {
  padding: 80px 0; /* Angepasstes Padding */
  background-color: var(--bg-light-gray);
}

.placeholder-image {
  width: 100%;
  max-width: 900px; /* Maximale Breite */
  margin: 0 auto; /* Zentriert */
  height: 500px; /* Höhe angepasst */
  background-color: var(--bg-darker-gray); /* Dunklerer Hintergrund */
  border-radius: var(--border-radius);
  display: flex;
  flex-direction: column; /* Icon über Text */
  align-items: center;
  justify-content: center;
  border: 1px solid var(--border-color); /* Durchgehende Border */
  box-shadow: var(--shadow);
  text-align: center;
}

.placeholder-icon {
    color: var(--text-muted);
    margin-bottom: 16px;
}

.placeholder-image span {
  color: var(--text-muted);
  font-style: normal; /* Kein Italic */
  font-size: 1rem;
}

/* Call to Action Section */
.cta-section {
  padding: 100px 0; /* Mehr Padding */
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-hover) 100%); /* Farbverlauf */
  text-align: center;
  color: white;
}

.cta-section .section-title {
    color: white; /* Titel in Weiss */
    margin-bottom: 24px;
}

.cta-section p {
  font-size: 1.2rem; /* Grösser */
  margin-bottom: 40px; /* Mehr Abstand */
  opacity: 0.95; /* Fast opak */
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.cta-section .cta-button.primary {
    background-color: white;
    color: var(--primary-color);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

.cta-section .cta-button.primary:hover {
    background-color: var(--bg-light-gray);
    color: var(--primary-hover);
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}


/* Footer */
.footer {
  padding: 40px 0; /* Mehr Padding */
  background-color: var(--bg-darker-gray); /* Dunklerer Hintergrund */
  text-align: center;
  border-top: 1px solid var(--border-color);
  margin-top: 80px; /* Mehr Abstand */
}

.footer p {
  font-size: 0.9rem;
  color: var(--text-muted); /* Hellerer Text */
}

/* Responsive Design Anpassungen */
@media (max-width: 992px) {
  .main-headline {
    font-size: 3rem; /* 48px */
  }
  .sub-headline {
    font-size: 1.125rem; /* 18px */
  }
  .section-title {
      font-size: 2rem; /* 32px */
  }
}

@media (max-width: 768px) {
  .hero-section {
    padding: 100px 0 80px;
  }
  .main-headline {
    font-size: 2.5rem; /* 40px */
  }
   .sub-headline {
    font-size: 1.1rem;
  }
  .features-section, .image-placeholder-section, .cta-section {
    padding: 80px 0;
  }
  .section-title {
      font-size: 1.8rem; /* 29px */
      margin-bottom: 40px;
  }
  .features-grid {
    grid-template-columns: 1fr;
    gap: 30px;
  }
   .feature-card {
       padding: 30px;
   }
  .placeholder-image {
    height: 350px;
  }
   .cta-section p {
       font-size: 1.1rem;
   }
   .cta-button {
       padding: 12px 28px;
       font-size: 1rem;
   }
   .cta-button.large {
       padding: 14px 32px;
       font-size: 1.05rem;
   }
}

</style>
