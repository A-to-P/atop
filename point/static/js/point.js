
const nonClick = document.querySelectorAll(".non-click");
const pay_btn = document.querySelector("#pay_btn");




function handleClick(event) {
  // 이미 클릭된 건 해제 
  if (event.target.classList[2] === "click"){
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

