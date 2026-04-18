#!/usr/bin/env python3
"""Add multi-language support, disclaimer, and other features to Water Safety Risk Engine"""

# Read the HTML file
with open('waternajia.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Language picker modal HTML - insert after <body>
lang_modal_html = '''
<!-- Language Picker Modal -->
<div id="lang_modal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm">
    <div class="glass-panel rounded-3xl p-8 max-w-md w-full mx-4 transform scale-100">
        <div class="text-center mb-6">
            <div class="text-5xl mb-4">🌍</div>
            <h2 class="text-2xl font-bold text-white mb-2">Select Language</h2>
            <p class="text-slate-400 text-sm">Choose your preferred language</p>
        </div>
        <div class="grid grid-cols-1 gap-3">
            <button onclick="setLanguage('en')" class="flex items-center gap-4 p-4 rounded-xl bg-white/5 hover:bg-cyan-500/20 border border-white/10 hover:border-cyan-500/30 transition-all group">
                <span class="text-3xl">🇬🇧</span>
                <div class="text-left">
                    <div class="font-semibold text-white group-hover:text-cyan-300">English</div>
                    <div class="text-xs text-slate-500">English</div>
                </div>
            </button>
            <button onclick="setLanguage('fr')" class="flex items-center gap-4 p-4 rounded-xl bg-white/5 hover:bg-cyan-500/20 border border-white/10 hover:border-cyan-500/30 transition-all group">
                <span class="text-3xl">🇫🇷</span>
                <div class="text-left">
                    <div class="font-semibold text-white group-hover:text-cyan-300">Francais</div>
                    <div class="text-xs text-slate-500">French</div>
                </div>
            </button>
            <button onclick="setLanguage('es')" class="flex items-center gap-4 p-4 rounded-xl bg-white/5 hover:bg-cyan-500/20 border border-white/10 hover:border-cyan-500/30 transition-all group">
                <span class="text-3xl">🇪🇸</span>
                <div class="text-left">
                    <div class="font-semibold text-white group-hover:text-cyan-300">Espanol</div>
                    <div class="text-xs text-slate-500">Spanish</div>
                </div>
            </button>
            <button onclick="setLanguage('ar')" class="flex items-center gap-4 p-4 rounded-xl bg-white/5 hover:bg-cyan-500/20 border border-white/10 hover:border-cyan-500/30 transition-all group">
                <span class="text-3xl">🇸🇦</span>
                <div class="text-left">
                    <div class="font-semibold text-white group-hover:text-cyan-300">العربية</div>
                    <div class="text-xs text-slate-500">Arabic</div>
                </div>
            </button>
            <button onclick="setLanguage('pt')" class="flex items-center gap-4 p-4 rounded-xl bg-white/5 hover:bg-cyan-500/20 border border-white/10 hover:border-cyan-500/30 transition-all group">
                <span class="text-3xl">🇧🇷</span>
                <div class="text-left">
                    <div class="font-semibold text-white group-hover:text-cyan-300">Portugues</div>
                    <div class="text-xs text-slate-500">Portuguese</div>
                </div>
            </button>
        </div>
    </div>
</div>

'''

# Insert modal after <body class="min-h-screen">
content = content.replace(
    '<body class="min-h-screen">',
    '<body class="min-h-screen">\n' + lang_modal_html
)

# 2. Add Export and Photo buttons to header + language globe button
new_header_buttons = '''<div class="flex gap-3 flex-wrap">
             <button onclick="exportData()" class="glass-panel hover:bg-white/10 text-emerald-300 px-4 py-2 rounded-lg font-medium transition flex items-center gap-2 border border-emerald-500/20 text-sm" title="Export Assessment">
                <i class="fas fa-download"></i> <span data-i18n="export">Export</span>
             </button>
             <button onclick="document.getElementById('photo_input').click()" class="glass-panel hover:bg-white/10 text-amber-300 px-4 py-2 rounded-lg font-medium transition flex items-center gap-2 border border-amber-500/20 text-sm" title="Add Photo">
                <i class="fas fa-camera"></i>
             </button>
             <input type="file" id="photo_input" accept="image/*" capture="environment" class="hidden" onchange="handlePhoto(event)">
             <button onclick="resampleRisk()" class="glass-panel hover:bg-white/10 text-purple-300 px-4 py-2 rounded-lg font-medium transition flex items-center gap-2 border border-purple-500/20 text-sm">
                <i class="fas fa-dice"></i> <span data-i18n="resample">Resample</span>
             </button>
             <button onclick="runTests()" class="glass-panel hover:bg-white/10 text-cyan-300 px-4 py-2 rounded-lg font-medium transition flex items-center gap-2 border border-cyan-500/20 text-sm">
                <i class="fas fa-vial"></i> <span data-i18n="runVerification">Run Verification</span>
             </button>
             <button onclick="resetInputs()" class="glass-panel hover:bg-white/10 text-slate-300 px-4 py-2 rounded-lg font-medium transition text-sm" data-i18n="reset">
                Reset
             </button>
             <button onclick="showLanguagePicker()" class="glass-panel hover:bg-white/10 text-slate-300 px-3 py-2 rounded-lg font-medium transition text-sm" title="Change Language">
                <i class="fas fa-globe"></i> <span id="current_lang_flag">🇬🇧</span>
             </button>
        </div>'''

# Replace the existing header buttons
old_header_buttons = '''<div class="flex gap-3">
             <button onclick="resampleRisk()" class="glass-panel hover:bg-white/10 text-purple-300 px-4 py-2 rounded-lg font-medium transition flex items-center gap-2 border border-purple-500/20 text-sm">
                <i class="fas fa-dice"></i> Resample
             </button>
             <button onclick="runTests()" class="glass-panel hover:bg-white/10 text-cyan-300 px-4 py-2 rounded-lg font-medium transition flex items-center gap-2 border border-cyan-500/20 text-sm">
                <i class="fas fa-vial"></i> Run Verification
             </button>
             <button onclick="resetInputs()" class="glass-panel hover:bg-white/10 text-slate-300 px-4 py-2 rounded-lg font-medium transition text-sm">
                Reset
             </button>
        </div>'''

content = content.replace(old_header_buttons, new_header_buttons)

# 3. Add disclaimer footer before closing </div> of max-w-7xl
disclaimer_html = '''
    <!-- Disclaimer Footer -->
    <footer class="mt-12 pt-8 border-t border-white/10">
        <div class="glass-panel rounded-2xl p-6">
            <div class="flex items-start gap-4">
                <div class="text-3xl">⚠️</div>
                <div class="flex-1">
                    <h4 class="font-bold text-amber-300 mb-2" data-i18n="disclaimerTitle">Important Disclaimer</h4>
                    <p class="text-sm text-slate-400 leading-relaxed mb-3" data-i18n="disclaimerText">
                        This tool is for <strong class="text-white">educational and informational purposes only</strong>.
                        It is <strong class="text-amber-300">NOT an official WHO application</strong> and has not been endorsed
                        or validated by the World Health Organization. Risk assessments are based on statistical models and
                        should not replace professional water quality testing or medical advice. Always consult local health
                        authorities and water quality experts for definitive guidance.
                    </p>
                    <div class="flex flex-wrap gap-4 text-xs text-slate-500">
                        <a href="https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health" target="_blank" class="hover:text-cyan-400 transition flex items-center gap-1">
                            <i class="fas fa-external-link-alt"></i> WHO Water & Sanitation
                        </a>
                        <span>|</span>
                        <span>v1.2.0</span>
                        <span>|</span>
                        <span>by Najia Ahmad</span>
                    </div>
                </div>
            </div>
        </div>
        <p class="text-center text-xs text-slate-600 mt-4">
            Risk model methodology based on WHO Guidelines for Drinking-water Quality (4th ed.)
        </p>
    </footer>
'''

# Find position before closing </div> of max-w-7xl (just before </div></body>)
content = content.replace(
    '</div>\n\n<script>',
    disclaimer_html + '\n</div>\n\n<script>'
)

# 4. Add Photo Preview panel after bacteria panel
photo_panel_html = '''
            <!-- Photo Documentation -->
            <div id="photo_panel" class="glass-panel p-6 rounded-2xl hidden">
                <h3 class="font-semibold text-white mb-4 flex items-center gap-2">
                    <i class="fas fa-camera text-amber-400"></i> <span data-i18n="photoDoc">Photo Documentation</span>
                </h3>
                <div id="photo_preview" class="grid grid-cols-2 md:grid-cols-3 gap-3">
                    <!-- Photos added here -->
                </div>
                <p class="text-xs text-slate-500 mt-3" data-i18n="photoHint">Photos are stored locally and included in exports</p>
            </div>
'''

content = content.replace(
    '<!-- Decay Curve (Full Width) -->',
    photo_panel_html + '\n\n            <!-- Decay Curve (Full Width) -->'
)

# 5. Add translations object and all new functions after COLORS constant
translations_js = '''
// --- MULTI-LANGUAGE SUPPORT ---
const LANG = {
    en: {
        title: "Water Safety Risk Engine",
        resample: "Resample",
        runVerification: "Run Verification",
        reset: "Reset",
        export: "Export",
        sourceVulnerability: "Source & Vulnerability",
        sourceType: "Source Type",
        pipedChlorinated: "Piped (Chlorinated)",
        protectedBorehole: "Protected Borehole",
        protectedWell: "Protected Well",
        rainwaterCatchment: "Rainwater Catchment",
        unprotectedBorehole: "Unprotected Borehole",
        unprotectedWell: "Unprotected Well",
        surfaceWater: "Surface Water (River/Dam)",
        householdVulnerable: "Household Vulnerable?",
        environment: "Environment",
        heavyRain: "Heavy Rain (Last 5 days)",
        flooding: "Flooding (Last 5 days)",
        hoursSinceEvent: "Hours Since Event",
        yourLocation: "Your Location",
        detect: "Detect",
        selectRegion: "Select Region...",
        southAsia: "South Asia",
        subSaharanAfrica: "Sub-Saharan Africa",
        southeastAsia: "Southeast Asia",
        latinAmerica: "Latin America",
        middleEast: "Middle East / N. Africa",
        eastAsia: "East Asia",
        europe: "Europe",
        northAmerica: "North America",
        oceania: "Oceania",
        detectingLocation: "Detecting location...",
        locationDenied: "Location denied - please select manually",
        couldNotDetect: "Could not detect region",
        observations: "Observations",
        turbidityVisible: "Turbidity Visible",
        smellTasteChange: "Smell/Taste Change",
        latrineDistance: "Latrine Distance",
        safeDistance: "Safe Distance (>30m)",
        lat10to30: "10m - 30m",
        latUnder10: "Under 10m (High Risk)",
        storageDuration: "Storage Duration",
        freshCovered: "Fresh / Covered",
        uncovered24h: "Uncovered > 24h",
        uncovered48h: "Uncovered > 48h",
        riskAssessmentResult: "Risk Assessment Result",
        calculating: "Calculating...",
        probContamination: "Probability of Contamination",
        low: "Low",
        moderate: "Mod",
        high: "High",
        confidenceInterval: "Confidence Interval (90% Credible)",
        topDrivers: "Top Drivers",
        noSignificantFactors: "No significant risk factors (baseline only)",
        recommendedActions: "Recommended Actions",
        urgentTreatment: "Urgent Treatment Required",
        urgentTreatmentText: "Do not consume without treatment. Boil for at least 1 minute or use Chlorine/Aquatabs (double dose if cloudy).",
        treatmentRecommended: "Treatment Recommended",
        treatmentRecommendedText: "Treat water before drinking. Chlorination or Solar Disinfection (SODIS) is advised.",
        maintainSafe: "Maintain Safe Practices",
        maintainSafeText: "Water appears safe. Ensure transport and storage containers are clean to prevent re-contamination.",
        clearWater: "Clear the Water",
        clearWaterText: "Turbidity reduces chlorine effectiveness. Filter through a cloth or let settle before treating.",
        sanitizeStorage: "Sanitize Storage",
        sanitizeStorageText: "Scrub the storage container with soap and water. Keep it covered and elevated off the ground.",
        sourceProtection: "Source Protection",
        sourceProtectionText: "Inspect the well apron/head for cracks. Divert runoff away from the water source.",
        commonPathogens: "Common Waterborne Pathogens",
        selectRegionBacteria: "Select your region to see common waterborne bacteria in your area",
        symptoms: "Symptoms:",
        decayEffect: "Rain/Flood Effect Decay",
        verificationSuite: "Verification Suite (12 Tests)",
        ready: "Ready",
        waitingExecution: "> Waiting for execution... Click \\"Run Verification\\" above.",
        categoryLow: "low",
        categoryModerate: "moderate",
        categoryHigh: "high",
        photoDoc: "Photo Documentation",
        photoHint: "Photos are stored locally and included in exports",
        disclaimerTitle: "Important Disclaimer",
        disclaimerText: "This tool is for educational and informational purposes only. It is NOT an official WHO application and has not been endorsed or validated by the World Health Organization. Risk assessments are based on statistical models and should not replace professional water quality testing or medical advice."
    },

    fr: {
        title: "Moteur de Risque de Securite de l'Eau",
        resample: "Reechantillonner",
        runVerification: "Verification",
        reset: "Reinitialiser",
        export: "Exporter",
        sourceVulnerability: "Source & Vulnerabilite",
        sourceType: "Type de Source",
        pipedChlorinated: "Canalisee (Chloree)",
        protectedBorehole: "Forage Protege",
        protectedWell: "Puits Protege",
        rainwaterCatchment: "Collecte d'Eau de Pluie",
        unprotectedBorehole: "Forage Non Protege",
        unprotectedWell: "Puits Non Protege",
        surfaceWater: "Eau de Surface (Riviere/Barrage)",
        householdVulnerable: "Menage Vulnerable?",
        environment: "Environnement",
        heavyRain: "Fortes Pluies (5 derniers jours)",
        flooding: "Inondation (5 derniers jours)",
        hoursSinceEvent: "Heures Depuis l'Evenement",
        yourLocation: "Votre Emplacement",
        detect: "Detecter",
        selectRegion: "Selectionner Region...",
        southAsia: "Asie du Sud",
        subSaharanAfrica: "Afrique Subsaharienne",
        southeastAsia: "Asie du Sud-Est",
        latinAmerica: "Amerique Latine",
        middleEast: "Moyen-Orient / Afrique N.",
        eastAsia: "Asie de l'Est",
        europe: "Europe",
        northAmerica: "Amerique du Nord",
        oceania: "Oceanie",
        detectingLocation: "Detection de l'emplacement...",
        locationDenied: "Localisation refusee - selectionnez manuellement",
        couldNotDetect: "Impossible de detecter la region",
        observations: "Observations",
        turbidityVisible: "Turbidite Visible",
        smellTasteChange: "Changement d'Odeur/Gout",
        latrineDistance: "Distance des Latrines",
        safeDistance: "Distance Sure (>30m)",
        lat10to30: "10m - 30m",
        latUnder10: "Moins de 10m (Risque Eleve)",
        storageDuration: "Duree de Stockage",
        freshCovered: "Frais / Couvert",
        uncovered24h: "Non couvert > 24h",
        uncovered48h: "Non couvert > 48h",
        riskAssessmentResult: "Resultat d'Evaluation des Risques",
        calculating: "Calcul en cours...",
        probContamination: "Probabilite de Contamination",
        low: "Faible",
        moderate: "Mod",
        high: "Eleve",
        confidenceInterval: "Intervalle de Confiance (90%)",
        topDrivers: "Principaux Facteurs",
        noSignificantFactors: "Aucun facteur significatif",
        recommendedActions: "Actions Recommandees",
        urgentTreatment: "Traitement Urgent Requis",
        urgentTreatmentText: "Ne pas consommer sans traitement. Faire bouillir au moins 1 minute.",
        treatmentRecommended: "Traitement Recommande",
        treatmentRecommendedText: "Traiter l'eau avant de boire.",
        maintainSafe: "Maintenir des Pratiques Sures",
        maintainSafeText: "L'eau semble sure. Assurez-vous que les conteneurs sont propres.",
        clearWater: "Clarifier l'Eau",
        clearWaterText: "La turbidite reduit l'efficacite du chlore.",
        sanitizeStorage: "Assainir le Stockage",
        sanitizeStorageText: "Nettoyer le conteneur avec du savon.",
        sourceProtection: "Protection de la Source",
        sourceProtectionText: "Inspecter le puits pour des fissures.",
        commonPathogens: "Pathogenes Hydriques Courants",
        selectRegionBacteria: "Selectionnez votre region",
        symptoms: "Symptomes:",
        decayEffect: "Effet Decroissant Pluie/Inondation",
        verificationSuite: "Suite de Verification (12 Tests)",
        ready: "Pret",
        waitingExecution: "> En attente d'execution...",
        categoryLow: "faible",
        categoryModerate: "modere",
        categoryHigh: "eleve",
        photoDoc: "Documentation Photo",
        photoHint: "Les photos sont stockees localement",
        disclaimerTitle: "Avertissement Important",
        disclaimerText: "Cet outil est uniquement a des fins educatives. Ce n'est PAS une application officielle de l'OMS."
    },

    es: {
        title: "Motor de Riesgo de Seguridad del Agua",
        resample: "Remuestrear",
        runVerification: "Verificacion",
        reset: "Reiniciar",
        export: "Exportar",
        sourceVulnerability: "Fuente y Vulnerabilidad",
        sourceType: "Tipo de Fuente",
        pipedChlorinated: "Entubada (Clorada)",
        protectedBorehole: "Pozo Perforado Protegido",
        protectedWell: "Pozo Protegido",
        rainwaterCatchment: "Recoleccion de Agua Lluvia",
        unprotectedBorehole: "Pozo Perforado No Protegido",
        unprotectedWell: "Pozo No Protegido",
        surfaceWater: "Agua Superficial (Rio/Presa)",
        householdVulnerable: "Hogar Vulnerable?",
        environment: "Ambiente",
        heavyRain: "Lluvia Fuerte (ultimos 5 dias)",
        flooding: "Inundacion (ultimos 5 dias)",
        hoursSinceEvent: "Horas Desde el Evento",
        yourLocation: "Tu Ubicacion",
        detect: "Detectar",
        selectRegion: "Seleccionar Region...",
        southAsia: "Asia del Sur",
        subSaharanAfrica: "Africa Subsahariana",
        southeastAsia: "Sudeste Asiatico",
        latinAmerica: "America Latina",
        middleEast: "Medio Oriente",
        eastAsia: "Asia Oriental",
        europe: "Europa",
        northAmerica: "America del Norte",
        oceania: "Oceania",
        detectingLocation: "Detectando ubicacion...",
        locationDenied: "Ubicacion denegada",
        couldNotDetect: "No se pudo detectar",
        observations: "Observaciones",
        turbidityVisible: "Turbidez Visible",
        smellTasteChange: "Cambio de Olor/Sabor",
        latrineDistance: "Distancia a Letrina",
        safeDistance: "Distancia Segura (>30m)",
        lat10to30: "10m - 30m",
        latUnder10: "Menos de 10m (Alto Riesgo)",
        storageDuration: "Duracion de Almacenamiento",
        freshCovered: "Fresco / Cubierto",
        uncovered24h: "Descubierto > 24h",
        uncovered48h: "Descubierto > 48h",
        riskAssessmentResult: "Resultado de Evaluacion",
        calculating: "Calculando...",
        probContamination: "Probabilidad de Contaminacion",
        low: "Bajo",
        moderate: "Mod",
        high: "Alto",
        confidenceInterval: "Intervalo de Confianza (90%)",
        topDrivers: "Principales Factores",
        noSignificantFactors: "Sin factores significativos",
        recommendedActions: "Acciones Recomendadas",
        urgentTreatment: "Tratamiento Urgente",
        urgentTreatmentText: "No consumir sin tratamiento. Hervir al menos 1 minuto.",
        treatmentRecommended: "Tratamiento Recomendado",
        treatmentRecommendedText: "Tratar el agua antes de beber.",
        maintainSafe: "Mantener Practicas Seguras",
        maintainSafeText: "El agua parece segura.",
        clearWater: "Clarificar el Agua",
        clearWaterText: "La turbidez reduce la eficacia del cloro.",
        sanitizeStorage: "Desinfectar Almacenamiento",
        sanitizeStorageText: "Limpiar el contenedor con jabon.",
        sourceProtection: "Proteccion de la Fuente",
        sourceProtectionText: "Inspeccionar el pozo por grietas.",
        commonPathogens: "Patogenos Hidricos Comunes",
        selectRegionBacteria: "Seleccione su region",
        symptoms: "Sintomas:",
        decayEffect: "Efecto Decreciente Lluvia/Inundacion",
        verificationSuite: "Suite de Verificacion (12 Pruebas)",
        ready: "Listo",
        waitingExecution: "> Esperando ejecucion...",
        categoryLow: "bajo",
        categoryModerate: "moderado",
        categoryHigh: "alto",
        photoDoc: "Documentacion Fotografica",
        photoHint: "Fotos almacenadas localmente",
        disclaimerTitle: "Aviso Importante",
        disclaimerText: "Esta herramienta es solo para fines educativos. NO es una aplicacion oficial de la OMS."
    },

    ar: {
        title: "محرك مخاطر سلامة المياه",
        resample: "اعادة العينة",
        runVerification: "تشغيل التحقق",
        reset: "اعادة تعيين",
        export: "تصدير",
        sourceVulnerability: "المصدر والضعف",
        sourceType: "نوع المصدر",
        pipedChlorinated: "انابيب (معالجة بالكلور)",
        protectedBorehole: "بئر ارتوازي محمي",
        protectedWell: "بئر محمي",
        rainwaterCatchment: "تجميع مياه الامطار",
        unprotectedBorehole: "بئر ارتوازي غير محمي",
        unprotectedWell: "بئر غير محمي",
        surfaceWater: "مياه سطحية (نهر/سد)",
        householdVulnerable: "اسرة ضعيفة؟",
        environment: "البيئة",
        heavyRain: "امطار غزيرة (اخر 5 ايام)",
        flooding: "فيضان (اخر 5 ايام)",
        hoursSinceEvent: "ساعات منذ الحدث",
        yourLocation: "موقعك",
        detect: "كشف",
        selectRegion: "اختر المنطقة...",
        southAsia: "جنوب اسيا",
        subSaharanAfrica: "افريقيا جنوب الصحراء",
        southeastAsia: "جنوب شرق اسيا",
        latinAmerica: "امريكا اللاتينية",
        middleEast: "الشرق الاوسط",
        eastAsia: "شرق اسيا",
        europe: "اوروبا",
        northAmerica: "امريكا الشمالية",
        oceania: "اوقيانوسيا",
        detectingLocation: "جاري الكشف...",
        locationDenied: "تم رفض الموقع",
        couldNotDetect: "تعذر الكشف",
        observations: "الملاحظات",
        turbidityVisible: "عكارة مرئية",
        smellTasteChange: "تغير في الرائحة/الطعم",
        latrineDistance: "المسافة من المرحاض",
        safeDistance: "مسافة امنة (>30م)",
        lat10to30: "10م - 30م",
        latUnder10: "اقل من 10م (خطر عالي)",
        storageDuration: "مدة التخزين",
        freshCovered: "طازج / مغطى",
        uncovered24h: "مكشوف > 24 ساعة",
        uncovered48h: "مكشوف > 48 ساعة",
        riskAssessmentResult: "نتيجة تقييم المخاطر",
        calculating: "جاري الحساب...",
        probContamination: "احتمال التلوث",
        low: "منخفض",
        moderate: "متوسط",
        high: "عالي",
        confidenceInterval: "فاصل الثقة (90٪)",
        topDrivers: "العوامل الرئيسية",
        noSignificantFactors: "لا توجد عوامل خطر كبيرة",
        recommendedActions: "الاجراءات الموصى بها",
        urgentTreatment: "العلاج العاجل مطلوب",
        urgentTreatmentText: "لا تستهلك بدون معالجة.",
        treatmentRecommended: "يوصى بالعلاج",
        treatmentRecommendedText: "عالج الماء قبل الشرب.",
        maintainSafe: "الحفاظ على الممارسات الامنة",
        maintainSafeText: "يبدو الماء امنا.",
        clearWater: "صفي الماء",
        clearWaterText: "تقلل العكارة من فعالية الكلور.",
        sanitizeStorage: "تعقيم التخزين",
        sanitizeStorageText: "اغسل الحاوية بالصابون.",
        sourceProtection: "حماية المصدر",
        sourceProtectionText: "افحص البئر للتشققات.",
        commonPathogens: "مسببات الامراض الشائعة",
        selectRegionBacteria: "اختر منطقتك",
        symptoms: "الاعراض:",
        decayEffect: "تاثير تناقص المطر/الفيضان",
        verificationSuite: "مجموعة التحقق",
        ready: "جاهز",
        waitingExecution: "> في انتظار التنفيذ...",
        categoryLow: "منخفض",
        categoryModerate: "متوسط",
        categoryHigh: "عالي",
        photoDoc: "توثيق بالصور",
        photoHint: "يتم تخزين الصور محليا",
        disclaimerTitle: "تنويه مهم",
        disclaimerText: "هذه الاداة لاغراض تعليمية فقط. هذا ليس تطبيقا رسميا لمنظمة الصحة العالمية."
    },

    pt: {
        title: "Motor de Risco de Seguranca da Agua",
        resample: "Reamostrar",
        runVerification: "Verificacao",
        reset: "Reiniciar",
        export: "Exportar",
        sourceVulnerability: "Fonte e Vulnerabilidade",
        sourceType: "Tipo de Fonte",
        pipedChlorinated: "Canalizada (Clorada)",
        protectedBorehole: "Furo Protegido",
        protectedWell: "Poco Protegido",
        rainwaterCatchment: "Captacao de Agua da Chuva",
        unprotectedBorehole: "Furo Nao Protegido",
        unprotectedWell: "Poco Nao Protegido",
        surfaceWater: "Agua Superficial (Rio/Barragem)",
        householdVulnerable: "Agregado Vulneravel?",
        environment: "Ambiente",
        heavyRain: "Chuva Forte (ultimos 5 dias)",
        flooding: "Inundacao (ultimos 5 dias)",
        hoursSinceEvent: "Horas Desde o Evento",
        yourLocation: "Sua Localizacao",
        detect: "Detetar",
        selectRegion: "Selecionar Regiao...",
        southAsia: "Sul da Asia",
        subSaharanAfrica: "Africa Subsaariana",
        southeastAsia: "Sudeste Asiatico",
        latinAmerica: "America Latina",
        middleEast: "Medio Oriente",
        eastAsia: "Asia Oriental",
        europe: "Europa",
        northAmerica: "America do Norte",
        oceania: "Oceania",
        detectingLocation: "Detetando localizacao...",
        locationDenied: "Localizacao negada",
        couldNotDetect: "Nao foi possivel detetar",
        observations: "Observacoes",
        turbidityVisible: "Turbidez Visivel",
        smellTasteChange: "Mudanca de Cheiro/Sabor",
        latrineDistance: "Distancia da Latrina",
        safeDistance: "Distancia Segura (>30m)",
        lat10to30: "10m - 30m",
        latUnder10: "Menos de 10m (Alto Risco)",
        storageDuration: "Duracao de Armazenamento",
        freshCovered: "Fresco / Coberto",
        uncovered24h: "Descoberto > 24h",
        uncovered48h: "Descoberto > 48h",
        riskAssessmentResult: "Resultado da Avaliacao",
        calculating: "Calculando...",
        probContamination: "Probabilidade de Contaminacao",
        low: "Baixo",
        moderate: "Mod",
        high: "Alto",
        confidenceInterval: "Intervalo de Confianca (90%)",
        topDrivers: "Principais Fatores",
        noSignificantFactors: "Sem fatores significativos",
        recommendedActions: "Acoes Recomendadas",
        urgentTreatment: "Tratamento Urgente",
        urgentTreatmentText: "Nao consumir sem tratamento.",
        treatmentRecommended: "Tratamento Recomendado",
        treatmentRecommendedText: "Tratar a agua antes de beber.",
        maintainSafe: "Manter Praticas Seguras",
        maintainSafeText: "A agua parece segura.",
        clearWater: "Clarificar a Agua",
        clearWaterText: "A turbidez reduz a eficacia do cloro.",
        sanitizeStorage: "Higienizar Armazenamento",
        sanitizeStorageText: "Limpar o recipiente com sabao.",
        sourceProtection: "Protecao da Fonte",
        sourceProtectionText: "Inspecionar o poco para rachaduras.",
        commonPathogens: "Patogenos Hidricos Comuns",
        selectRegionBacteria: "Selecione sua regiao",
        symptoms: "Sintomas:",
        decayEffect: "Efeito Decrescente",
        verificationSuite: "Suite de Verificacao",
        ready: "Pronto",
        waitingExecution: "> Aguardando execucao...",
        categoryLow: "baixo",
        categoryModerate: "moderado",
        categoryHigh: "alto",
        photoDoc: "Documentacao Fotografica",
        photoHint: "Fotos armazenadas localmente",
        disclaimerTitle: "Aviso Importante",
        disclaimerText: "Esta ferramenta e apenas para fins educacionais. NAO e uma aplicacao oficial da OMS."
    }
};

const LANG_FLAGS = { en: '🇬🇧', fr: '🇫🇷', es: '🇪🇸', ar: '🇸🇦', pt: '🇧🇷' };
let currentLang = 'en';
let capturedPhotos = [];

function showLanguagePicker() {
    document.getElementById('lang_modal').style.display = 'flex';
}

function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('waterSafetyLang', lang);
    document.getElementById('lang_modal').style.display = 'none';
    document.getElementById('current_lang_flag').textContent = LANG_FLAGS[lang];
    document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
    document.documentElement.lang = lang;
    applyTranslations();
}

function t(key) {
    return LANG[currentLang]?.[key] || LANG.en[key] || key;
}

function applyTranslations() {
    const L = LANG[currentLang];

    // Header title
    const h1 = document.querySelector('h1');
    if (h1) {
        const versionSpan = h1.querySelector('.text-cyan-300');
        const authorSpan = h1.querySelector('span[style]');
        h1.childNodes[0].textContent = L.title + ' ';
    }

    // Buttons with data-i18n
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (L[key]) {
            if (el.tagName === 'SPAN' || el.tagName === 'BUTTON') {
                el.textContent = L[key];
            } else if (el.tagName === 'P' || el.tagName === 'H4') {
                el.innerHTML = L[key];
            }
        }
    });

    // Update source select options
    const sourceSelect = document.getElementById('source_type');
    if (sourceSelect && sourceSelect.options.length >= 7) {
        sourceSelect.options[0].text = L.pipedChlorinated;
        sourceSelect.options[1].text = L.protectedBorehole;
        sourceSelect.options[2].text = L.protectedWell;
        sourceSelect.options[3].text = L.rainwaterCatchment;
        sourceSelect.options[4].text = L.unprotectedBorehole;
        sourceSelect.options[5].text = L.unprotectedWell;
        sourceSelect.options[6].text = L.surfaceWater;
    }

    // Region select
    const regionSelect = document.getElementById('region_select');
    if (regionSelect && regionSelect.options.length >= 10) {
        regionSelect.options[0].text = L.selectRegion;
        regionSelect.options[1].text = L.southAsia;
        regionSelect.options[2].text = L.subSaharanAfrica;
        regionSelect.options[3].text = L.southeastAsia;
        regionSelect.options[4].text = L.latinAmerica;
        regionSelect.options[5].text = L.middleEast;
        regionSelect.options[6].text = L.eastAsia;
        regionSelect.options[7].text = L.europe;
        regionSelect.options[8].text = L.northAmerica;
        regionSelect.options[9].text = L.oceania;
    }

    updateBacteria();
    updateUI();
}

// --- PHOTO DOCUMENTATION ---
function handlePhoto(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {
        const photoData = {
            data: e.target.result,
            timestamp: new Date().toISOString(),
            id: Date.now()
        };
        capturedPhotos.push(photoData);
        renderPhotos();
        document.getElementById('photo_panel').classList.remove('hidden');
    };
    reader.readAsDataURL(file);
    event.target.value = '';
}

function renderPhotos() {
    const container = document.getElementById('photo_preview');
    container.innerHTML = capturedPhotos.map((p, i) => `
        <div class="relative group">
            <img src="${p.data}" class="w-full h-24 object-cover rounded-lg border border-white/10">
            <button onclick="removePhoto(${i})" class="absolute top-1 right-1 w-6 h-6 bg-red-500/80 rounded-full text-white text-xs opacity-0 group-hover:opacity-100 transition">
                <i class="fas fa-times"></i>
            </button>
            <div class="absolute bottom-1 left-1 text-[8px] text-white/70 bg-black/50 px-1 rounded">
                ${new Date(p.timestamp).toLocaleTimeString()}
            </div>
        </div>
    `).join('');
}

function removePhoto(index) {
    capturedPhotos.splice(index, 1);
    renderPhotos();
    if (capturedPhotos.length === 0) {
        document.getElementById('photo_panel').classList.add('hidden');
    }
}

// --- DATA EXPORT ---
function exportData() {
    const inputs = getInputs();
    const result = computeRisk(inputs, MODEL, currentSeed);
    const region = document.getElementById('region_select').value;

    const exportObj = {
        meta: {
            appName: "Water Safety Risk Engine",
            version: "1.2.0",
            exportDate: new Date().toISOString(),
            language: currentLang,
            disclaimer: "NOT AN OFFICIAL WHO APPLICATION - For educational purposes only"
        },
        assessment: {
            inputs: inputs,
            result: {
                probability: result.P,
                category: result.category,
                confidence_interval: { low: result.min, high: result.max },
                confidence: result.confidence,
                top_drivers: result.contributions.slice(0, 5)
            },
            region: region,
            timestamp: new Date().toISOString()
        },
        photos: capturedPhotos.map(p => ({
            timestamp: p.timestamp,
            data: p.data.substring(0, 100) + '...[truncated]'
        }))
    };

    // Create download
    const blob = new Blob([JSON.stringify(exportObj, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `water-safety-assessment-${new Date().toISOString().split('T')[0]}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);

    // Also create CSV for surveillance integration
    const csv = [
        'timestamp,source_type,region,risk_probability,risk_category,ci_low,ci_high,vulnerable,heavy_rain,flooding,hours_since,turbidity,smell_change,latrine_under_10m,latrine_10_30m,storage_24h,storage_48h',
        [
            exportObj.assessment.timestamp,
            inputs.source_type,
            region,
            result.P.toFixed(4),
            result.category,
            result.min.toFixed(4),
            result.max.toFixed(4),
            inputs.is_vulnerable,
            inputs.heavy_rain,
            inputs.flooding,
            inputs.hours_since_rain_or_flood || '',
            inputs.turbidity_visible,
            inputs.smell_or_taste_change,
            inputs.latrine_under_10m,
            inputs.latrine_10_to_30m,
            inputs.storage_uncovered_over_24h,
            inputs.storage_uncovered_over_48h
        ].join(',')
    ].join('\\n');

    const csvBlob = new Blob([csv], { type: 'text/csv' });
    const csvUrl = URL.createObjectURL(csvBlob);
    const csvLink = document.createElement('a');
    csvLink.href = csvUrl;
    csvLink.download = `water-safety-${new Date().toISOString().split('T')[0]}.csv`;
    document.body.appendChild(csvLink);
    csvLink.click();
    document.body.removeChild(csvLink);
    URL.revokeObjectURL(csvUrl);
}

'''

# Find position to insert (after COLORS constant)
insert_pos = content.find("// --- BACTERIA DATABASE BY REGION ---")
content = content[:insert_pos] + translations_js + "\n" + content[insert_pos:]

# 6. Modify initialization to check for saved language
init_code = '''
// --- INITIALIZATION ---
document.addEventListener('DOMContentLoaded', function() {
    const savedLang = localStorage.getItem('waterSafetyLang');
    if (savedLang && LANG[savedLang]) {
        setLanguage(savedLang);
    } else {
        document.getElementById('lang_modal').style.display = 'flex';
    }
});
'''

# Replace the resetInputs() call at the end
content = content.replace(
    'resetInputs();\n</script>',
    'resetInputs();\n' + init_code + '\n</script>'
)

# Update version number in header
content = content.replace('v1.1.0', 'v1.2.0')

# Write the modified file
with open('waternajia.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("All features added successfully!")
print("- Multi-language support (EN, FR, ES, AR with RTL, PT)")
print("- Language picker modal on first load")
print("- Globe button to change language anytime")
print("- Disclaimer footer (NOT an official WHO app)")
print("- Export button (JSON + CSV for surveillance)")
print("- Photo documentation with camera capture")
print("- Version updated to 1.2.0")
