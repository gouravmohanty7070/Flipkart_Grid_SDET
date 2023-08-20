document.getElementById("chatForm").addEventListener("submit", function (e) {
  e.preventDefault();

  let userInput = document.getElementById("userInput").value;
  displayUserMessage(userInput);
  document.getElementById("userInput").value = "";
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  fetch(window.chatUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      text: userInput,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Assuming data contains a 'text' field for the bot's reply and other fields contain image recommendations
      displayBotReply(data.text);

      for (const category in data) {
        if (category !== "text" && data[category]) {
          // If category isn't 'text' and has data
          displayBotReply(category, data[category]); // Display image for each category recommendation
        }
      }
    })
    .catch((error) => {
      console.error("There was an error with the request:", error);
    });
});

function displayUserMessage(message) {
  const chatContainer = document.querySelector(".chat-ui");

  const userBubble = document.createElement("div");
  userBubble.classList.add("chat-bubble", "user-bubble");

  const bubbleText = document.createElement("div");
  bubbleText.classList.add("bubble-text");
  bubbleText.textContent = message;

  const profilePic = document.createElement("div");
  profilePic.classList.add("profile-picture");
  const img = document.createElement("img");
  img.src =
    "https://res.cloudinary.com/dhhax6yae/image/upload/v1691769490/Paneer_qc1zhn.png";
  img.alt = "User Profile";
  profilePic.appendChild(img);

  userBubble.appendChild(bubbleText);
  userBubble.appendChild(profilePic);

  chatContainer.appendChild(userBubble);
}

function displayBotReply(text, base64Image = null) {
  const chatContainer = document.querySelector(".chat-ui");

  const botBubble = document.createElement("div");
  botBubble.classList.add("chat-bubble", "ai-bubble");

  const profilePic = document.createElement("div");
  profilePic.classList.add("profile-picture");
  const img = document.createElement("img");
  img.src =
    "https://res.cloudinary.com/dhhax6yae/image/upload/v1692184252/Illustration_8_-modified_ohqeeu.png";
  img.alt = "AI Profile";
  profilePic.appendChild(img);

  const bubbleText = document.createElement("div");
  bubbleText.classList.add("bubble-text");
  bubbleText.textContent = text;

  botBubble.appendChild(profilePic);
  botBubble.appendChild(bubbleText);

  if (base64Image) {
    const imageElement = document.createElement("img");
    imageElement.src = `data:image/jpeg;base64,${base64Image}`;
    imageElement.classList.add("chat-image"); // You can style this class for better visuals
    botBubble.appendChild(imageElement);
  }

  chatContainer.appendChild(botBubble);
}

document
  .getElementById("chatForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const userMessage = document.getElementById("userInput").value;

    // Display user's message
    const userBubble = `
      <div class="chat-bubble user-bubble">
          <div class="bubble-text">${userMessage}</div>
          <div class="profile-picture">
              <img src="https://res.cloudinary.com/dhhax6yae/image/upload/v1691769490/Paneer_qc1zhn.png" alt="User Profile">
          </div>
      </div>`;
    document.querySelector(".chat-ui").innerHTML += userBubble;

    // Fetch recommendations from backend
    fetch(window.chatUrl, {
      method: "POST",
      body: JSON.stringify({ message: userMessage }),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
          .value,
      },
    })
      .then((response) => response.json())
      .then((data) => {
        // Display bot's reply
        displayBotReply(data.text, data.base64Image);

        let dataArray = [];

        for (const category in data) {
          dataArray.push({
            category: category,
            images: data[category],
          });
        }

        // console.log(dataArray);
        console.log(typeof dataArray);
        // Display recommended products
        let productHtml = "";
        dataArray.forEach((item) => {
          if (Array.isArray(item.images)) {
            item.images.forEach((imgUrl) => {
              productHtml += `
            <div class="product-card">
                <img src="${imgUrl}" alt="Product Image">
                <div class="product-details">
                    <div class="product-name">${item.category}</div>
                    <div class="product-price">$100</div> 
                </div>
                <div class="product-actions">
                    <button class="add-to-cart">Add to Cart</button>
                    <button class="favorite">Favorite</button>
                </div>
            </div>`;
            });
          }
        });

        document.getElementById("recommendedProducts").innerHTML = productHtml;
      })
      .catch((error) => console.error("Error:", error));

    // Clear the user input
    document.getElementById("userInput").value = "";
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
