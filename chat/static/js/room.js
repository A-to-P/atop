function fileToBase64(file) {
  return new Promise((resolve) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function () {
      resolve(reader.result);
    };
  });
}

function dataURLtoFile(dataurl, filename) {
  var arr = dataurl.split(","),
    mime = arr[0].match(/:(.*?);/)[1],
    bstr = atob(arr[1]),
    n = bstr.length,
    u8arr = new Uint8Array(n);

  while (n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }

  return new File([u8arr], filename, { type: mime });
}

// JSON.parse() 메소드 : json 문자열의 구문을 분석하고 결과로 javascript 값이나 객체 생성
const roomName = JSON.parse(document.getElementById("room-name").textContent);
const userName = JSON.parse(document.getElementById("user-name").textContent);
const user_id = JSON.parse(document.getElementById("user_id").textContent);

// DOM
const chatLogDom = document.querySelector("#chat-log");

// chatSocket 변수에 생선된 webSocket 할당 / ws://ws/chat/roomName
const chatSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/chat/" + roomName + "/"
);

// chatSocket에 onopen 메소드 지정
chatSocket.onopen = function (e) {
  fetchMessages();
};

// chat-log id를 통해서 기존 message 에 추가해서 message 를 onmessage 해줌
chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  if (data["command"] === "messages") {
    for (let i = 0; i < data["messages"].length; i++) {
      createMessage(data["messages"][i]);
    }
  } else if (data["command"] === "new_message") {
    createMessage(data["message"]);
  }
};

// 에러났을 때는 onclose
chatSocket.onclose = function (e) {
  console.error("Chat socket closed unexpectedly");
};

// 파일 인풋에 onchange 이벤트가 발생하면 첨부파일 이름 미리보기 변경
const messageFileDom = document.querySelector("#chat_file_input");
// const onChangeFile = async(e)=>
messageFileDom.onchange = (e) => {
  const file = e.target.files[0];
  // console.log("file :", file);

  document.querySelector("#file_name").innerText = file.name;
};

// 엔터를 눌러도 click 이벤트가 발생하게 처리
document.querySelector("#chat_inputbox").onkeyup = function (e) {
  if (e.keyCode === 13) {
    // enter, return
    document.querySelector("#chat_submit_button").click();
  }
};

// onclick 이벤트가 발생하면 input value를 message에 저장해서 json형태로 chatSocket으로 전송
// chatSocket 전송이 완료되면 input box value 를 공백으로 초기화
document.querySelector("#chat_submit_button").onclick = async function (e) {
  const messageInputDom = document.querySelector("#chat_inputbox");

  // 메시지
  const message = messageInputDom.value;

  // 첨부파일
  const _file = messageFileDom.files[0];
  let file = { filename: "", base64URL: "" };

  // 첨부파일이 있다면
  if (_file) {
    console.log("file:", _file);
    const base64URL = await fileToBase64(_file);
    file.filename = _file.name;
    file.base64URL = base64URL;
  } else {
    // 첨부파일도 없고 메시지도 없다면
    if (message == "") {
      console.log("메시지를 입력하세요");
      // 메시지 전송 안함!
      return;
    }
  }

  chatSocket.send(
    JSON.stringify({
      message: message,
      user_id: user_id,
      command: "new_message",
      file: file,
    })
  );
  messageInputDom.value = "";
  messageFileDom.value = "";
  document.querySelector("#file_name").innerText = "첨부파일이 없습니다.";
};

function fetchMessages() {
  chatSocket.send(JSON.stringify({ command: "fetch_messages" }));
}

function createMessage(data) {
  // console.log("createMessage_data:", data);
  const author = data["author"];

  const _timestamp = new Date(data.timestamp);
  const timestamp = `${
    _timestamp.getMonth() + 1
  }/${_timestamp.getDate()} ${_timestamp.getHours()}:${_timestamp.getMinutes()}`;

  const file = data["file"][0];
  // console.log(file.filename);
  // 메시지 내용이 없으면 display: none
  const isContent = data.content != "" ? "" : "display: none";

  const fileContent =
    file.filename == ""
      ? ``
      : `
      <div class="chat-message p-2 ms-2 me-2 mb-1 rounded-3 bg-warning d-flex justify-content-between align-items-center">
      <div>${file.filename}</div>
      <button class="file-download"><span style="display: none">${JSON.stringify(
        file
      )}</span></button></div>
      `;

  const aChat =
    author == userName
      ? `<p class="small mb-0 me-2 text-end text-muted d-flex justify-content-end">${timestamp}</p>
      
      <div class="d-flex flex-row justify-content-end pt-1 me">
              <div class="d-flex flex-row">
                
                <div><p class="chat-message p-2 me-2 mb-1 text-white rounded-3 bg-primary" style="${isContent}">${data.content}</p>
                ${fileContent}</div>
              </div>
            </div>`
      : `<div class="d-flex flex-row justify-content-start you">
              <div class="d-flex flex-row">
              <div>
                <p class="chat-message p-2 ms-2 mb-1 rounded-3" style="background-color:#f5f6f7;" style="${isContent}">${data.content}</p>
                ${fileContent}</div>
                <p class="small ms-2 mb-1 rounded-3 text-muted">${timestamp}</p>
              </div>
            </div>`;

  // 채팅 추가하고 스크롤바 내리기
  chatLogDom.innerHTML += aChat;
  chatLogDom.scrollTop = chatLogDom.scrollHeight;
}

// 파일 다운로드
// 클릭이벤트 감지
chatLogDom.onclick = function (e) {
  const target = e.target;

  if (!target.classList.contains("file-download")) return;
  // 다운로드버튼을 클릭한경우
  // console.log(JSON.parse(target.children[0].innerText));
  const file_data = JSON.parse(target.children[0].innerText);
  fileDownload(file_data);
};

const fileDownload = (file_data) => {
  const file = dataURLtoFile(file_data.base64URL, file_data.filename); // file 생성

  const objectURL = window.URL.createObjectURL(file);

  // chrome 파일 다운로드
  var a = document.createElement("a");
  a.href = objectURL;
  a.download = file_data.filename; // Set the file name.
  a.style.display = "none";
  document.body.appendChild(a);
  a.click();
  delete a;
};
