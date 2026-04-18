// --- BACTERIA/LOCATION FUNCTIONS ---
function detectLocation() {
    const status = document.getElementById('location_status');
    const detected = document.getElementById('detected_location');
    status.classList.remove('hidden');
    detected.classList.add('hidden');

    if (!navigator.geolocation) {
        status.innerHTML = '<span class="text-red-400">Geolocation not supported</span>';
        return;
    }

    navigator.geolocation.getCurrentPosition(
        async (position) => {
            try {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                const resp = await fetch(`https://nominatim.openstreetmap.org/reverse?lat=${lat}&lon=${lon}&format=json`);
                const data = await resp.json();
                const country = data.address?.country_code?.toUpperCase() || '';
                const countryName = data.address?.country || 'Unknown';

                status.classList.add('hidden');
                detected.classList.remove('hidden');
                detected.innerHTML = `<i class="fas fa-check-circle text-emerald-400"></i> ${countryName}`;

                const region = COUNTRY_TO_REGION[country] || 'europe';
                document.getElementById('region_select').value = region;
                updateBacteria();
            } catch (e) {
                status.innerHTML = '<span class="text-red-400">Could not detect region</span>';
            }
        },
        (error) => {
            status.innerHTML = '<span class="text-yellow-400">Location denied - please select manually</span>';
        }
    );
}

function updateBacteria() {
    const region = document.getElementById('region_select').value;
    const container = document.getElementById('bacteria_content');

    if (!region) {
        container.innerHTML = `
            <div class="text-center py-4">
                <i class="fas fa-map-marker-alt text-2xl mb-2 opacity-30"></i>
                <p>Select your region to see common waterborne bacteria</p>
            </div>`;
        return;
    }

    const globalBacteria = BACTERIA_DB.global || [];
    const regionalBacteria = BACTERIA_DB[region] || [];
    const allBacteria = [...regionalBacteria, ...globalBacteria];

    const severityColors = {
        critical: 'bg-red-900/40 border-red-500/40 text-red-200',
        high: 'bg-orange-900/40 border-orange-500/40 text-orange-200',
        moderate: 'bg-yellow-900/40 border-yellow-500/40 text-yellow-200',
        low: 'bg-emerald-900/40 border-emerald-500/40 text-emerald-200'
    };

    const severityLabels = {
        critical: '🚨 CRITICAL',
        high: '⚠️ HIGH',
        moderate: '⚡ MODERATE',
        low: '✅ LOW'
    };

    let html = '<div class="space-y-3">';

    allBacteria.forEach(b => {
        const color = severityColors[b.severity] || severityColors.moderate;
        const label = severityLabels[b.severity] || '⚡ MODERATE';

        html += `
            <div class="${color} border rounded-xl p-4">
                <div class="flex items-start justify-between mb-2">
                    <div class="flex items-center gap-2">
                        <span class="text-2xl">${b.emoji}</span>
                        <div>
                            <h4 class="font-bold text-white">${b.name}</h4>
                            <p class="text-xs opacity-80">${b.disease}</p>
                        </div>
                    </div>
                    <span class="text-[10px] font-bold uppercase tracking-wider opacity-70">${label}</span>
                </div>
                <div class="text-xs mt-2 pt-2 border-t border-white/10">
                    <span class="opacity-70">Symptoms:</span> ${b.symptoms}
                </div>
            </div>`;
    });

    html += '</div>';
    container.innerHTML = html;
}

