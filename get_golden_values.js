// Extract golden values from the engine
const fs = require('fs');
const content = fs.readFileSync('C:/Users/user/Downloads/waternajia/waternajia.html', 'utf8');

// Extract and clean script
const scriptMatch = content.match(/<script>([\s\S]*?)<\/script>/);
let script = scriptMatch[1];

// Remove UI code that needs DOM
script = script.split('// --- 6. UI BINDINGS ---')[0];
script = script.replace(/document\./g, '// document.');

// Create a function wrapper to execute
const fn = new Function(script + `
const BASE = {
    is_vulnerable: false, heavy_rain: false, flooding: false,
    hours_since_rain_or_flood: null, turbidity_visible: false,
    smell_or_taste_change: false, storage_uncovered_over_24h: false,
    storage_uncovered_over_48h: false, animals_access_or_open_container: false,
    latrine_under_10m: false, latrine_10_to_30m: false,
    dirty_fetch_container: false, diarrhoea_signal_mild: false,
    diarrhoea_signal_strong: false
};

console.log('=== ACTUAL GOLDEN VALUES (seed=12345) ===');
console.log('');

let r = computeRisk({...BASE, source_type: 'piped_chlorinated'}, MODEL, 12345);
console.log('Golden #1 - Piped:     P=' + r.P.toFixed(4) + ', min=' + r.min.toFixed(4) + ', max=' + r.max.toFixed(4));

r = computeRisk({...BASE, source_type: 'surface_water'}, MODEL, 12345);
console.log('Golden #2 - Surface:   P=' + r.P.toFixed(4) + ', min=' + r.min.toFixed(4) + ', max=' + r.max.toFixed(4));

r = computeRisk({...BASE, source_type: 'protected_well', flooding: true, hours_since_rain_or_flood: 12}, MODEL, 12345);
console.log('Golden #3 - Flood 12h: P=' + r.P.toFixed(4));

r = computeRisk({...BASE, source_type: 'protected_well', flooding: true, hours_since_rain_or_flood: 72}, MODEL, 12345);
console.log('Golden #4 - Flood 72h: P=' + r.P.toFixed(4));

r = computeRisk({...BASE, source_type: 'unprotected_well', heavy_rain: true, hours_since_rain_or_flood: 6}, MODEL, 12345);
console.log('Golden #5 - Interact:  has_interaction=' + r.contributions.some(c => c.key === 'interaction'));

r = computeRisk({...BASE, source_type: 'unprotected_well', heavy_rain: true, hours_since_rain_or_flood: 6, turbidity_visible: true, latrine_under_10m: true, storage_uncovered_over_48h: true}, MODEL, 12345);
console.log('Golden #6 - Full:      P=' + r.P.toFixed(4) + ', cat=' + r.category);
`);

fn();
