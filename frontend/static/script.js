document.addEventListener("DOMContentLoaded", () => {
    const header = document.getElementsByTagName("h1")[0];
    header.addEventListener("click",()=>{
        alert("ok it works")
    })


    // get the current date to dynamically apply it to the page
    const date = new Date();
    const dateSpan = document.getElementById("date");
    console.log(dateSpan)
    dateSpan.innerText = String(date.getFullYear());
})