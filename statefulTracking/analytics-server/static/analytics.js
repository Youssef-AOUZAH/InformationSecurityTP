function getCookie(name) {
    const cookies = document.cookie.split("; ");
    for (let cookie of cookies) {
        const [key, value] = cookie.split("=");
        if (key === name) {
            return value;
        }
    }
    return null;
}

let analyticsId = getCookie("aid");

if (!analyticsId) {
    analyticsId = Math.random().toString(36).substring(2, 12);
    document.cookie = `aid=${analyticsId}; path=/; max-age=31536000`;
}

const pageTitle = document.title || window.location.pathname;

fetch(`http://lab.test:9004/collect?aid=${analyticsId}&page=${encodeURIComponent(pageTitle)}`);