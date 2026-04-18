# Water Safety Risk Engine - Rust/WASM

Bit-exact Rust implementation of the Water Safety Risk Engine for WebAssembly compilation.

## Features

- XorShift128Plus PRNG (bit-exact with JS BigInt implementation)
- Box-Muller transform for normal distribution
- Bayesian risk scoring with logit/sigmoid transforms
- Monte Carlo simulation (200 samples)
- Exponential decay for rain/flood effects
- Factor group exclusivity ("max_only" mode)

## Build

```bash
# Install wasm-pack if not already installed
cargo install wasm-pack

# Build for web target
wasm-pack build --target web

# Run tests
cargo test
```

## Usage in JavaScript

```javascript
import init, { compute_risk } from './pkg/water_safety_wasm.js';

await init();

const inputs = JSON.stringify({
  source_type: "protected_well",
  is_vulnerable: false,
  heavy_rain: true,
  flooding: false,
  hours_since_rain_or_flood: 12,
  turbidity_visible: false,
  smell_or_taste_change: false,
  storage_uncovered_over_24h: false,
  storage_uncovered_over_48h: false,
  animals_access_or_open_container: false,
  latrine_under_10m: false,
  latrine_10_to_30m: false,
  dirty_fetch_container: false,
  diarrhoea_signal_mild: false,
  diarrhoea_signal_strong: false
});

const result = compute_risk(inputs, 12345n);
console.log(result); // { p: 0.xxx, min: 0.xxx, max: 0.xxx, category: "...", ... }
```

## Golden Tests

The implementation includes golden tests with seed=12345 to ensure bit-exact matching with the JavaScript reference implementation:

| Test | Expected P | Tolerance |
|------|-----------|-----------|
| Piped Baseline | 0.0636 | ±0.005 |
| Surface Water | 0.5962 | ±0.01 |
| Flood h=12 | 0.5461 | ±0.02 |
| Flood h=72 | 0.3437 | ±0.02 |
| Full Risk Stack | 0.9207 | ±0.02 |

## License

MIT
