document.addEventListener("DOMContentLoaded", () => {

    // check if I get a response (for the loader)
    const generateRcpBtn = document.getElementById("gen-rec-btn");
    generateRcpBtn.addEventListener("click", async (event) => {
        event.preventDefault();
        const result = await fetch("/my-assistant/generate");
        const data = await result.json()
        console.log(data)
    })

    // get the current date to dynamically apply it to the page
    const date = new Date();
    const dateSpan = document.getElementById("date");
    console.log(dateSpan)
    dateSpan.innerText = String(date.getFullYear());
})