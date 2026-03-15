const SERVER_URL = "https://твоя-ссылка-на-render.onrender.com"; // <- сюда ставим URL сервера

async function sendMessage() {
    const msgArea = document.getElementById("userMessage");
    const msg = msgArea.value.trim();
    if(!msg) return;

    const model = document.getElementById("modelSelect").value;
    const chatDiv = document.getElementById("chat");

    chatDiv.innerHTML += `<div class="message"><span class="user">Вы:</span> ${msg}</div>`;
    chatDiv.scrollTop = chatDiv.scrollHeight;

    msgArea.value = "";

    try {
        const response = await fetch(`${SERVER_URL}/chat`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({message: msg, model: model})
        });

        const data = await response.json();
        chatDiv.innerHTML += `<div class="message"><span class="bot">${model}:</span> ${data.response}</div>`;
        chatDiv.scrollTop = chatDiv.scrollHeight;

    } catch (err) {
        chatDiv.innerHTML += `<div class="message"><span class="bot">Ошибка:</span> ${err}</div>`;
    }
}

function insertFunction(func) {
    const msgArea = document.getElementById("userMessage");
    switch(func){
        case 'код': msgArea.value = "Сгенерируй код для..."; break;
        case 'идеи': msgArea.value = "Придумай идеи для..."; break;
        case 'учеба': msgArea.value = "Объясни тему..."; break;
        case 'бизнес': msgArea.value = "Составь план для бизнеса..."; break;
        case 'развлечения': msgArea.value = "Придумай шутку или историю..."; break;
    }
    msgArea.focus();
}