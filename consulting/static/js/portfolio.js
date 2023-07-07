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

/*
포트폴리오 li, 페이지네이션
*/
const user_id = JSON.parse(document.getElementById("user_id").textContent);
const history_list = JSON.parse(
  document.getElementById("history_list").textContent
);
const ulDOM = document.getElementById("history-list");
console.log(history_list);

ulDOM.onclick = function (e) {
  const target = e.target;

  if (!target.classList.contains("file-download")) return;
  // 다운로드버튼을 클릭한경우
  // console.log(JSON.parse(target.children[0].innerText));
  const file_data = JSON.parse(target.children[0].innerText);
  fileDownload(file_data);
};

const init = (cb) => {
  if (history_list.length == 0) {
    ulDOM.innerHTML = `<li class="portfolio-list-item" style="border:none;">
    <div class="list-content" style="border:none;">컨설팅 내역이 없습니다.</div></li>`;
    return;
  }

  history_list.forEach((history) => {
    const deleteBtn = `<button type="button" class="btn btn-primary delete_btn" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
    <span class="d-none">${history.consulting_id}</span>
  </button>`;

    const result = `<li class="portfolio-list-item" key="${
      history.consulting_id
    }"><div class="list-content">
    <div>${history.end.slice(0, 10)}</div>
    <div>${history.restaurant}</div>
    <div>${history.res_tag}</div>
    <div>${history.con_tag}</div>
    <div>|</div>
    <button type="button" class="file-download final-report">최종 레포트 파일
    <span class="d-none">${JSON.stringify(history.final_file)}</span>
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-download" viewbox="0 0 16 16">
        <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"/>
        <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"/>
      </svg>
    </button>
    </div> ${deleteBtn}
    </li>`;
    ulDOM.innerHTML += result;
  });

  // paginator
  const paginator = JSON.parse(
    document.getElementById("paginator").textContent
  );
  console.log("paginator:", paginator);
  // {num_pages: 2, page_number: 3

  const paginationUlDOM = document.getElementById("pagination");

  for (let i = 1; i <= paginator.num_pages; i++) {
    const active = i === parseInt(paginator.page_number) ? "active" : "";
    paginationUlDOM.innerHTML += `<li class="page-item ${active}" aria-current="true">
        <a class="page-link" href="?page=${i}">
          ${i}
        </a>
      </li>`;
  }

  cb();
};

/*
모달 js
*/
function modal_init() {
  var btn = document.querySelectorAll(".delete_btn");
  var modals = document.querySelectorAll("#staticBackdrop");

  const deleteInputDOM = document.getElementById("consulting_id_input");

  for (var i = 0; i < btn.length; i++) {
    btn[i].onclick = function (e) {
      e.preventDefault();
      deleteInputDOM.value = e.target.children[0].innerText;
    };
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function (event) {
    if (event.target.classList.contains("modal-custom")) {
      for (var index in modals) {
        if (typeof modals[index].style !== "undefined")
          modals[index].style.display = "none";
      }
    }
  };
}

init(modal_init);
