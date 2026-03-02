export function getConfidence(distance) {
  if (distance < 0.6) return "High";
  if (distance < 0.9) return "Medium";
  return "Low";
}