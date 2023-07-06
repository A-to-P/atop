const user_id = JSON.parse(document.getElementById("user_id").textContent);
const history_list = JSON.parse(
  document.getElementById("history_list").textContent
);
const ulDOM = document.getElementById("history-list");

const init = () => {
  if (history_list.length == 0) {
    ulDOM.innerHTML = `<li class="history-list-item" style="border:none;"><div class="list-content">컨설팅 내역이 없습니다.</div></li>`;
    return;
  }
  history_list.forEach((history) => {
    const result = `<li class="history-list-item" key="${
      history.consulting_id
    }">
  <div class="list-content">${history.end.slice(0, 10)}</div>
  <div class="list-content">${history.consultant}</div>
  <div class="list-content">${history.tag}</div>
  <div class="list-content">${history.fee}</div>
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
};

init();
