// ==================== PART 2: ACTIVE FEATURES ====================
const activeFeatures = {
  language: navigator.language,
  timeZone: Intl.DateTimeFormat().resolvedOptions().timeZone,
  screenResolution: `${screen.width}x${screen.height}`,
  colorDepth: screen.colorDepth,
  pixelRatio: window.devicePixelRatio,
  cpuCores: navigator.hardwareConcurrency,
  deviceMemoryGB: navigator.deviceMemory || "N/A"
};

const featureOutput = document.getElementById("feature-output");
if (featureOutput) {
  featureOutput.textContent = JSON.stringify(activeFeatures, null, 2);
}

// ==================== PART 3 & 4: BEHAVIORAL + HASHING ====================
const targetSentence = document.getElementById("target-sentence").textContent.trim();
const input = document.getElementById("typing-input");
const restartButton = document.getElementById("restart-btn");
const timeDisplay = document.getElementById("time-val");
const speedDisplay = document.getElementById("wpm-val");
const correctionsDisplay = document.getElementById("corrections-val");

let startTime = null;
let corrections = 0;

// SHA-256 Helper using Web Crypto API
async function sha256Data(data) {
  const stringData = JSON.stringify(data);
  const encoded = new TextEncoder().encode(stringData);
  const hashBuffer = await crypto.subtle.digest("SHA-256", encoded);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, "0")).join("");
}

input.addEventListener("keydown", function(event) {
  if (startTime === null && event.key.length === 1) {
    startTime = performance.now();
  }

  if (event.key === "Backspace") {
    corrections = corrections + 1;
    correctionsDisplay.textContent = corrections;
  }
});

input.addEventListener("input", async function() {
  if (input.value === targetSentence) {
    const endTime = performance.now();
    const totalTimeSeconds = (endTime - startTime) / 1000;
    const words = targetSentence.length / 5;
    const minutes = totalTimeSeconds / 60;
    const typingSpeed = (words / minutes).toFixed(2);

    timeDisplay.textContent = totalTimeSeconds.toFixed(2) + " s";
    speedDisplay.textContent = typingSpeed + " WPM";

    // Combine active environment and behavioral features
    const combinedData = {
      ...activeFeatures,
      typingTimeSeconds: parseFloat(totalTimeSeconds.toFixed(2)),
      typingSpeedWPM: parseFloat(typingSpeed),
      correctionsCount: corrections
    };

    // Generate SHA-256 hash
    const hashedFingerprint = await sha256Data(combinedData);
    console.log("Calculated Fingerprint (SHA-256):", hashedFingerprint);

    // Send only the hash identifier to Flask
    fetch("/collect", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ fingerprint: hashedFingerprint })
    });
  }
});

restartButton.addEventListener("click", function() {
  startTime = null;
  corrections = 0;
  input.value = "";
  timeDisplay.textContent = "-";
  speedDisplay.textContent = "-";
  correctionsDisplay.textContent = "0";
  input.focus();
});