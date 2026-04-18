// --- BACTERIA DATABASE BY REGION ---
const BACTERIA_DB = {
    // Global pathogens (found everywhere)
    global: [
        { name: "E. coli", emoji: "🦠", disease: "Diarrhoea, UTIs", severity: "moderate", symptoms: "💧 Watery diarrhoea, 🤢 Nausea, 🤕 Cramps" },
        { name: "Salmonella", emoji: "🧫", disease: "Typhoid, Gastroenteritis", severity: "high", symptoms: "🤒 Fever, 💩 Diarrhoea, 🤮 Vomiting" },
        { name: "Vibrio cholerae", emoji: "💀", disease: "Cholera", severity: "critical", symptoms: "💧 Severe watery diarrhoea, 🥵 Dehydration, ⚡ Rapid onset" }
    ],

    south_asia: [
        { name: "Shigella", emoji: "🔴", disease: "Shigellosis (Bloody diarrhoea)", severity: "high", symptoms: "🩸 Bloody stool, 🤒 Fever, 🤕 Severe cramps" },
        { name: "Hepatitis A virus", emoji: "🟡", disease: "Hepatitis A", severity: "high", symptoms: "🟡 Jaundice, 😴 Fatigue, 🤢 Nausea" },
        { name: "Rotavirus", emoji: "🔵", disease: "Severe diarrhoea (children)", severity: "high", symptoms: "🤮 Vomiting, 💧 Watery diarrhoea, 🤒 Fever" },
        { name: "Entamoeba histolytica", emoji: "🟤", disease: "Amoebic dysentery", severity: "high", symptoms: "🩸 Bloody diarrhoea, 😣 Abdominal pain, 🤒 Fever" }
    ],

    sub_saharan_africa: [
        { name: "Vibrio cholerae O1", emoji: "💀", disease: "Epidemic Cholera", severity: "critical", symptoms: "💧 Rice-water stool, ⚡ Rapid dehydration, 🆘 Life-threatening" },
        { name: "Cryptosporidium", emoji: "🟢", disease: "Cryptosporidiosis", severity: "moderate", symptoms: "💧 Watery diarrhoea, 🤕 Cramps, 😴 Fatigue" },
        { name: "Schistosoma", emoji: "🐛", disease: "Schistosomiasis (Bilharzia)", severity: "high", symptoms: "🩸 Blood in urine, 🤕 Abdominal pain, 😴 Chronic fatigue" },
        { name: "Guinea worm", emoji: "🪱", disease: "Dracunculiasis", severity: "moderate", symptoms: "🔥 Burning blister, 🦵 Leg ulcers, 🤒 Fever" }
    ],

    southeast_asia: [
        { name: "Leptospira", emoji: "🌀", disease: "Leptospirosis", severity: "high", symptoms: "🤒 High fever, 🤕 Headache, 💪 Muscle pain, 🟡 Jaundice" },
        { name: "Hepatitis E virus", emoji: "🟠", disease: "Hepatitis E", severity: "high", symptoms: "🟡 Jaundice, 🤢 Nausea, 🤰 Dangerous in pregnancy" },
        { name: "Campylobacter", emoji: "🔷", disease: "Campylobacteriosis", severity: "moderate", symptoms: "💧 Diarrhoea, 🤒 Fever, 🤕 Abdominal cramps" },
        { name: "Giardia lamblia", emoji: "🟣", disease: "Giardiasis", severity: "moderate", symptoms: "💨 Bloating, 💧 Greasy diarrhoea, 🤢 Nausea" }
    ],

    latin_america: [
        { name: "Cyclospora", emoji: "🔘", disease: "Cyclosporiasis", severity: "moderate", symptoms: "💧 Watery diarrhoea, 😴 Fatigue, 📉 Weight loss" },
        { name: "Enteroaggregative E. coli", emoji: "🦠", disease: "Traveler's diarrhoea", severity: "moderate", symptoms: "💧 Persistent diarrhoea, 🤢 Nausea, 🤕 Cramps" },
        { name: "Norovirus", emoji: "🟪", disease: "Viral gastroenteritis", severity: "moderate", symptoms: "🤮 Projectile vomiting, 💧 Diarrhoea, ⚡ Rapid spread" },
        { name: "Ascaris", emoji: "🪱", disease: "Ascariasis (Roundworm)", severity: "moderate", symptoms: "🤕 Abdominal pain, 🫁 Cough, 📉 Malnutrition" }
    ],

    middle_east: [
        { name: "Enterococcus", emoji: "🟤", disease: "Gastroenteritis, UTIs", severity: "moderate", symptoms: "💧 Diarrhoea, 🔥 Painful urination, 🤒 Fever" },
        { name: "Pseudomonas aeruginosa", emoji: "🟢", disease: "Skin/ear infections", severity: "moderate", symptoms: "👂 Ear pain, 🩹 Skin rash, 🤒 Fever" },
        { name: "Legionella", emoji: "🫁", disease: "Legionnaires' disease", severity: "high", symptoms: "🫁 Pneumonia, 🤒 High fever, 🤕 Headache" }
    ],

    east_asia: [
        { name: "Clonorchis sinensis", emoji: "🐛", disease: "Liver fluke infection", severity: "moderate", symptoms: "🤕 Abdominal pain, 🟡 Jaundice, 😴 Fatigue" },
        { name: "Aeromonas", emoji: "🔵", disease: "Gastroenteritis, wound infections", severity: "moderate", symptoms: "💧 Diarrhoea, 🩹 Wound infection, 🤒 Fever" },
        { name: "Vibrio parahaemolyticus", emoji: "🦐", disease: "Seafood poisoning", severity: "moderate", symptoms: "💧 Watery diarrhoea, 🤕 Cramps, 🤮 Vomiting" }
    ],

    europe: [
        { name: "Campylobacter jejuni", emoji: "🔷", disease: "Campylobacteriosis", severity: "moderate", symptoms: "💧 Diarrhoea, 🤒 Fever, 🤕 Cramps" },
        { name: "Giardia", emoji: "🟣", disease: "Giardiasis", severity: "low", symptoms: "💨 Bloating, 💧 Diarrhoea, 🤢 Nausea" },
        { name: "Cryptosporidium parvum", emoji: "🟢", disease: "Cryptosporidiosis", severity: "low", symptoms: "💧 Watery diarrhoea, 🤕 Cramps, 😴 Fatigue" }
    ],

    north_america: [
        { name: "Giardia lamblia", emoji: "🟣", disease: "Giardiasis (Beaver fever)", severity: "low", symptoms: "💨 Gas/bloating, 💧 Diarrhoea, 🤕 Cramps" },
        { name: "Legionella pneumophila", emoji: "🫁", disease: "Legionnaires' disease", severity: "high", symptoms: "🫁 Pneumonia, 🤒 Fever, 💪 Muscle aches" },
        { name: "Naegleria fowleri", emoji: "🧠", disease: "Brain-eating amoeba", severity: "critical", symptoms: "🧠 Severe headache, 🤒 Fever, 🆘 Rapidly fatal" }
    ],

    oceania: [
        { name: "Burkholderia pseudomallei", emoji: "🔴", disease: "Melioidosis", severity: "high", symptoms: "🤒 Fever, 🫁 Pneumonia, 🩹 Skin abscesses" },
        { name: "Leptospira", emoji: "🌀", disease: "Leptospirosis", severity: "high", symptoms: "🤒 Fever, 🤕 Headache, 🟡 Jaundice" },
        { name: "Vibrio vulnificus", emoji: "🦪", disease: "Wound infections, sepsis", severity: "critical", symptoms: "🩹 Severe wound infection, 🆘 Sepsis, 🤒 Fever" }
    ]
};

// Map countries to regions
const COUNTRY_TO_REGION = {
    'IN': 'south_asia', 'PK': 'south_asia', 'BD': 'south_asia', 'NP': 'south_asia', 'LK': 'south_asia', 'AF': 'south_asia',
    'NG': 'sub_saharan_africa', 'ET': 'sub_saharan_africa', 'KE': 'sub_saharan_africa', 'TZ': 'sub_saharan_africa',
    'ZA': 'sub_saharan_africa', 'GH': 'sub_saharan_africa', 'UG': 'sub_saharan_africa', 'SN': 'sub_saharan_africa',
    'CD': 'sub_saharan_africa', 'ZW': 'sub_saharan_africa', 'MW': 'sub_saharan_africa', 'ZM': 'sub_saharan_africa',
    'VN': 'southeast_asia', 'TH': 'southeast_asia', 'PH': 'southeast_asia', 'ID': 'southeast_asia',
    'MY': 'southeast_asia', 'MM': 'southeast_asia', 'KH': 'southeast_asia', 'LA': 'southeast_asia',
    'BR': 'latin_america', 'MX': 'latin_america', 'CO': 'latin_america', 'AR': 'latin_america',
    'PE': 'latin_america', 'VE': 'latin_america', 'CL': 'latin_america', 'EC': 'latin_america',
    'EG': 'middle_east', 'SA': 'middle_east', 'IR': 'middle_east', 'IQ': 'middle_east',
    'MA': 'middle_east', 'DZ': 'middle_east', 'TN': 'middle_east', 'JO': 'middle_east',
    'CN': 'east_asia', 'JP': 'east_asia', 'KR': 'east_asia', 'TW': 'east_asia', 'HK': 'east_asia',
    'GB': 'europe', 'DE': 'europe', 'FR': 'europe', 'IT': 'europe', 'ES': 'europe',
    'PL': 'europe', 'NL': 'europe', 'BE': 'europe', 'SE': 'europe', 'NO': 'europe',
    'US': 'north_america', 'CA': 'north_america',
    'AU': 'oceania', 'NZ': 'oceania', 'FJ': 'oceania', 'PG': 'oceania'
};
