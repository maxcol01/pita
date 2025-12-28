/*
* P.I.T.A - Pantry Inventory Tracking Application
* Script JS - Dynamism of the app
*/


document.addEventListener("DOMContentLoaded", () => {

    // check if I get a response (for the loader)
    const generateRcpBtn = document.getElementById("gen-rec-btn");
    const spinner = document.getElementById("spinner");


    // display the recipe history (selection of one recipe)
    const selectedRecipe = document.getElementById("user-recipe");
    if (selectedRecipe){
        selectedRecipe.addEventListener("change", (e) => {
            const idRecipe = e.target.value;
            window.location.href = `/display_recipe/${idRecipe}`;
        })
    }

    // manage the spinner while loading
    if (generateRcpBtn){
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
    }



    // get the current date to dynamically apply it to the page
    const date = new Date();
    const dateSpan = document.getElementById("date");
    console.log(dateSpan)
    dateSpan.innerText = String(date.getFullYear());
})