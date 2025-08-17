// dictionary of all translations
const translations = {
    en: {
        titles: "Digital artist · web & app developer",
        button: "한국어",
        blog:"My blog",
    },
    ko: {
        titles: "디지털 예술가 · 웹·앱 개발자",
        button: "English",
        blog: "저의 블로그",
    }
};

// keep track of current language
let currentLang = "en";

// get elements to translate
const elements = document.querySelectorAll("[data-i18n]");
const langToggle = document.getElementById("langToggle");

// set language
function setLanguage(lang){
    elements.forEach(el => {
        const key = el.getAttribute("data-i18n");
        if(translations[lang][key]){
            el.textContent = translations[lang][key];
        }
    });

    langToggle.textContent = translations[lang].button;
    currentLang = lang;
}

langToggle.addEventListener("click", ()=> {
    setLanguage(currentLang === "en" ? "ko" : "en");

});

setLanguage(currentLang);