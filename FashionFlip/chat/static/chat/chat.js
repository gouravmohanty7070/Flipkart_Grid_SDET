document.getElementById("chatForm").addEventListener("submit", function (e) {
  // Prevent the form from submitting (page reload)
  e.preventDefault();

  // Get the input field
  const inputField = document.querySelector(".message-input");

  // Get the message from the input field
  const message = inputField.value;

  // Check if the message is not empty
  if (message.trim() !== "") {
    // Create a new chat bubble
    const chatBubble = document.createElement("div");
    chatBubble.className = "chat-bubble user-bubble";
    chatBubble.innerHTML = `
            <div class="bubble-text">${message}</div>
            <div class="profile-picture"><img src="https://res.cloudinary.com/dhhax6yae/image/upload/v1691769490/Paneer_qc1zhn.png" alt="User Profile"></div>
        `;

    // Add the chat bubble to the messages-container above the input field
    const messagesContainer = document.querySelector(".messages-container");
    messagesContainer.appendChild(chatBubble);

    // Clear the input field for the next message
    inputField.value = "";

    // Scroll the messages container to show the new message
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const attachmentIcon = document.querySelector(".fa-paperclip");
  const popup = document.querySelector(".attachment-popup");
  const closePopupButton = document.getElementById("closePopup");
  const clothesVisualizerButton = document.getElementById("clothesVisualizer");
  const searchFashionButton = document.getElementById("searchFashion");
  const clothesVisualizerContent = document.getElementById(
    "clothesVisualizerContent"
  );
  const searchFashionContent = document.getElementById("searchFashionContent");
  const dragDropCard = document.getElementById("dragDropCard");
  const inputContainer = document.getElementById("inputContainer");
  const promptInput = document.getElementById("promptInput");
  const saveButton = document.getElementById("saveButton");
  const imageContainer = document.getElementById("imageContainer");
  const fileInput = document.getElementById("fileInput");

  attachmentIcon.addEventListener("click", function () {
    popup.style.display = "block";
    clothesVisualizerContent.style.display = "none";
    searchFashionContent.style.display = "none";
    clothesVisualizerButton.classList.remove("active");
    searchFashionButton.classList.remove("active");
  });

  closePopupButton.addEventListener("click", function () {
    popup.style.display = "none";
  });

  clothesVisualizerButton.addEventListener("click", function () {
    if (!clothesVisualizerButton.classList.contains("active")) {
      clothesVisualizerButton.classList.add("active");
      searchFashionButton.classList.remove("active");
      clothesVisualizerContent.style.display = "block";
      inputContainer.style.display = "block";
      dragDropCard.style.display = "block";
      searchFashionContent.style.display = "none";
    }
  });

  searchFashionButton.addEventListener("click", function () {
    if (!searchFashionButton.classList.contains("active")) {
      searchFashionButton.classList.add("active");
      clothesVisualizerButton.classList.remove("active");
      clothesVisualizerContent.style.display = "none";
      inputContainer.style.display = "none";
      dragDropCard.style.display = "none";
      searchFashionContent.style.display = "block";
    }
  });

  dragDropCard.addEventListener("dragover", function (event) {
    event.preventDefault();
  });

  dragDropCard.addEventListener("drop", function (event) {
    event.preventDefault();
    handleFileUpload(event.dataTransfer.files[0]);
  });

  fileInput.addEventListener("change", function (event) {
    handleFileUpload(event.target.files[0]);
  });

  saveButton.addEventListener("click", function () {
    const promptText = promptInput.value;
    if (promptText) {
      const imageUrl =
        "https://res.cloudinary.com/dhhax6yae/image/upload/v1692253401/undraw_Fashion_blogging_re_fhi5_fxxa0i.png";
      const imagePreview = document.createElement("img");
      imagePreview.src = imageUrl;
      imagePreview.alt = "Image Preview";
      imageContainer.innerHTML = "";
      imageContainer.appendChild(imagePreview);
    }
  });

  function handleFileUpload(file) {
    if (file) {
      const reader = new FileReader();
      reader.onload = function (event) {
        const imagePreview = document.createElement("img");
        imagePreview.src = event.target.result;
        imagePreview.alt = "Image Preview";
        imageContainer.innerHTML = "";
        imageContainer.appendChild(imagePreview);
      };
      reader.readAsDataURL(file);
    }
  }
});
