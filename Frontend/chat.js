document.addEventListener("DOMContentLoaded", function() {
    const attachmentIcon = document.querySelector(".fa-paperclip");
    const popup = document.querySelector(".attachment-popup");
    const closePopupButton = document.getElementById("closePopup");
    const clothesVisualizerButton = document.getElementById("clothesVisualizer");
    const searchFashionButton = document.getElementById("searchFashion");

    attachmentIcon.addEventListener("click", function() {
        popup.style.display = "block";
    });

    closePopupButton.addEventListener("click", function() {
        popup.style.display = "none";
    });

    clothesVisualizerButton.addEventListener("click", function() {
        
        popup.style.display = "none";
    });

    searchFashionButton.addEventListener("click", function() {
       
        popup.style.display = "none";
    });
});
