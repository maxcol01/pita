document.addEventListener("DOMContentLoaded", () => {

    // check if I get a response (for the loader)
    const generateRcpBtn = document.getElementById("gen-rec-btn");
    const spinner = document.getElementById("spinner");

    generateRcpBtn.addEventListener("click", async (event) => {
        event.preventDefault();
        spinner.hidden = false;
        const result = await fetch("/my-assistant/generate");
        const data = await result.json()
        // redirect to the assistant page
        if (data){
            window.location.href = "/my-assistant"
            spinner.hidden = true;
        }
    })

    // display the recipe history (selection of one recipe)


    // get the current date to dynamically apply it to the page
    const date = new Date();
    const dateSpan = document.getElementById("date");
    console.log(dateSpan)
    dateSpan.innerText = String(date.getFullYear());
})