console.log("DURABLE PAPERPLANE");

// get element by id message
const message = document.getElementById("message");
const button = document.getElementById("submitBtn");
const file = document.getElementById("file");

// if button is clicked, check the file input
button.addEventListener("click", function (event) {
  if (file.files.length === 0) {
    message.innerHTML = "사진이 없습니다. 사진을 업로드해주세요.";
   
  } else {
    message.innerHTML = "상품을 찾는 중입니다...";
    
  }
});
