async function runEmotionAnalysis() {
  const text = document.getElementById("textToAnalyze").value;
  const output = document.getElementById("system_response");

  output.textContent = "Analyzing…";

  try {
    const endpoint = `/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`;
    const response = await fetch(endpoint);
    output.textContent = await response.text();
  } catch (_error) {
    output.textContent = "The service is unavailable. Please try again.";
  }
}
