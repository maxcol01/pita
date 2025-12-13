document.addEventListener("DOMContentLoaded", () => {

    // Dashboard display options

    const btn = document.getElementsByClassName("select-storage-btns")
    console.log(btn)




    // dynamically show the item card container

    // get the current date to dynamically apply it to the page
    const date = new Date();
    const dateSpan = document.getElementById("date");
    console.log(dateSpan)
    dateSpan.innerText = String(date.getFullYear());
})