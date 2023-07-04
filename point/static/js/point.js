// 유저 포인트
const user_point = JSON.parse(
  document.getElementById("user_point").textContent
);

// 포인트
const nonClick = document.querySelectorAll(".non-click");

// 결제하기 버튼
const pay_btn = document.querySelector("#pay_btn");

function handleClick(event) {
  // 이미 클릭된 건 해제
  if (event.target.classList[2] === "click") {
    event.target.classList.remove("click");
    pay_btn.classList.remove("activate");
    return;
  }
  // div에서 모든 "click" 클래스 제거
  nonClick.forEach((e) => {
    e.classList.remove("click");
    // pay_btn.classList.remove("activate");
  });
  // 클릭한 div만 "click"클래스 추가
  event.target.classList.add("click");
  // 결제하기 버튼 활성화
  pay_btn.classList.add("activate");
}

nonClick.forEach((e) => {
  e.addEventListener("click", handleClick);
});

// 선택 포인트 모달에 띄우기
function calculatePoint(event) {
  nonClick.forEach((e) => {
    if (e.classList[2] === "click") {
      let choiced = e.value;
      document.getElementById("choiced_point").innerHTML = choiced;

      document.getElementById("after_point").innerHTML =
        parseInt(user_point) + parseInt(choiced);
    }
  });
}

pay_btn.addEventListener("click", calculatePoint);
