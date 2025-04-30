<template>
  <div class="landing-container">
    <!-- Header Section -->
    <header class="header">
      <div class="logo">Typo Corrector</div>
      <nav>
        <!-- Optional: Add more nav links if needed -->
        <NuxtLink to="/homepage-test" class="cta-button header-cta">Try Corrector</NuxtLink>
      </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-content">
        <h1 class="hero-title">Effortless Text Correction</h1>
        <p class="hero-subtitle">
          Refine your writing with our intelligent typo corrector. Choose between Casual mode for quick fixes or the upcoming Expert mode for fine-grained control.
        </p>
        <NuxtLink to="/homepage-test" class="cta-button hero-cta">Get Started Now</NuxtLink>
      </div>
      <div class="hero-image-placeholder">
        <!-- Placeholder for a visual representation -->
        <svg width="100%" height="100%" viewBox="0 0 400 300" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="400" height="300" rx="12" fill="#e2e8f0"/>
          <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Literata, serif" font-size="20" fill="#64748b">App Screenshot Placeholder</text>
        </svg>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features-section">
      <h2 class="section-title">Why Choose Typo Corrector?</h2>
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">✨</div>
          <h3 class="feature-title">Smart Correction</h3>
          <p class="feature-description">Leverages advanced rules to catch common and complex typos accurately.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">⚙️</div>
          <h3 class="feature-title">Flexible Modes</h3>
          <p class="feature-description">Use Casual mode for everyday text or switch to Expert (coming soon!) for precise control.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">📄</div>
          <h3 class="feature-title">Preserve Formatting</h3>
          <p class="feature-description">Optionally keep your original text formatting intact during correction.</p>
        </div>
         <div class="feature-card">
          <div class="feature-icon">🚀</div>
          <h3 class="feature-title">Fast & Easy</h3>
          <p class="feature-description">Get corrected text quickly with a simple and intuitive interface.</p>
        </div>
      </div>
    </section>

     <!-- Call to Action Section -->
    <section class="cta-section">
        <h2 class="section-title">Ready to Improve Your Text?</h2>
        <p>Click the button below to start correcting your text instantly.</p>
        <NuxtLink to="/homepage-test" class="cta-button cta-section-button">Try the Corrector</NuxtLink>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <p>&copy; {{ new Date().getFullYear() }} Typo Corrector. All rights reserved.</p>
      <!-- Optional: Add more footer links -->
    </footer>

  </div>
</template>

<script setup>
// No specific script logic needed for this static landing page yet.
// We can add animations or interactions here later.
import { ref, onMounted } from 'vue';

// Example: Add simple fade-in effect on mount (requires CSS)
const isMounted = ref(false);
onMounted(() => {
  isMounted.value = true;
  // You might want to add Intersection Observer here for more complex animations
});

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,200..900;1,7..72,200..900&display=swap');

:root {
  --primary-color: #4f46e5; /* From homepage-test */
  --primary-hover: #4338ca; /* Darker shade for hover */
  --text-color: #1e293b;    /* From homepage-test */
  --text-light: #64748b;   /* From homepage-test */
  --bg-color: #f9fafb;      /* From homepage-test */
  --card-bg: #ffffff;     /* From homepage-test */
  --border-radius: 12px;  /* From homepage-test */
  --shadow: 0 4px 12px rgba(0, 0, 0, 0.08); /* Softer shadow */
  --font-family: "Literata", serif;
}

.landing-container {
  font-family: var(--font-family);
  background-color: var(--bg-color);
  color: var(--text-color);
  line-height: 1.6;
  opacity: 0;
  animation: fadeIn 0.5s ease-out forwards;
}

@keyframes fadeIn {
  to {
    opacity: 1;
  }
}

/* General Styles */
h1, h2, h3 {
  font-weight: 700;
  line-height: 1.3;
  letter-spacing: -0.5px;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 40px;
  color: var(--text-color);
}

/* Header */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 40px;
  background-color: var(--card-bg);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.logo {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--primary-color);
}

/* Buttons */
.cta-button {
  display: inline-block;
  background-color: var(--primary-color);
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 500;
  transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 10px rgba(79, 70, 229, 0.2);
}

.cta-button:hover {
  background-color: var(--primary-hover);
  transform: translateY(-2px);
  box-shadow: 0 6px 15px rgba(79, 70, 229, 0.3);
}

.header-cta {
  padding: 10px 20px;
  font-size: 0.9rem;
}

/* Hero Section */
.hero-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  gap: 60px;
  padding: 80px 40px;
  min-height: 70vh;
  background-color: var(--bg-color); /* Or a subtle gradient */
}

.hero-content {
  max-width: 500px;
}

.hero-title {
  font-size: 3.5rem;
  margin-bottom: 20px;
  color: var(--text-color);
}

.hero-subtitle {
  font-size: 1.1rem;
  color: var(--text-light);
  margin-bottom: 30px;
}

.hero-cta {
  font-size: 1.1rem;
}

.hero-image-placeholder {
  border-radius: var(--border-radius);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: transform 0.3s ease;
}
.hero-image-placeholder:hover {
    transform: scale(1.03);
}

/* Features Section */
.features-section {
  padding: 80px 40px;
  background-color: var(--card-bg); /* Alternate background */
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
}

.feature-card {
  background-color: var(--bg-color); /* Use main bg for cards here */
  padding: 30px;
  border-radius: var(--border-radius);
  text-align: center;
  box-shadow: var(--shadow);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  font-size: 2.5rem;
  margin-bottom: 15px;
  display: inline-block;
}

.feature-title {
  font-size: 1.3rem;
  margin-bottom: 10px;
  color: var(--text-color);
}

.feature-description {
  font-size: 0.95rem;
  color: var(--text-light);
}

/* Call to Action Section */
.cta-section {
    padding: 60px 40px;
    text-align: center;
    background-color: var(--primary-color); /* Use primary color */
    color: white;
    border-radius: var(--border-radius);
    margin: 60px 40px;
    box-shadow: 0 8px 25px rgba(79, 70, 229, 0.3);
}

.cta-section .section-title {
    color: white;
    margin-bottom: 15px;
}

.cta-section p {
    margin-bottom: 30px;
    opacity: 0.9;
}

.cta-section-button {
    background-color: white;
    color: var(--primary-color);
    font-weight: 600;
}

.cta-section-button:hover {
    background-color: #f0f0f0; /* Slightly off-white hover */
    color: var(--primary-hover);
}


/* Footer */
.footer {
  text-align: center;
  padding: 30px 40px;
  margin-top: 40px;
  border-top: 1px solid #e2e8f0;
  color: var(--text-light);
  font-size: 0.9rem;
}

/* Responsive Design */
@media (max-width: 992px) {
  .hero-section {
    grid-template-columns: 1fr;
    text-align: center;
    padding: 60px 30px;
  }
  .hero-content {
      order: 2; /* Content below image on smaller screens */
      max-width: 100%;
  }
   .hero-image-placeholder {
      order: 1;
      margin-bottom: 40px; /* Add space between image and text */
      max-width: 500px; /* Limit image size */
      margin-left: auto;
      margin-right: auto;
   }
  .hero-title {
    font-size: 2.8rem;
  }
  .section-title {
      font-size: 2rem;
  }
}

@media (max-width: 768px) {
  .header {
    padding: 15px 20px;
    flex-direction: column;
    gap: 10px;
  }
  .hero-section {
      padding: 40px 20px;
  }
  .hero-title {
    font-size: 2.2rem;
  }
  .features-section, .cta-section, .footer {
      padding: 60px 20px;
  }
   .cta-section {
       margin: 40px 20px;
   }
  .features-grid {
      grid-template-columns: 1fr; /* Stack features */
  }
}

</style>
