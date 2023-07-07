const categorys = JSON.parse(document.getElementById("categorys").textContent);
const req_list = JSON.parse(document.getElementById("req_list").textContent);

console.log(req_list);

document.addEventListener(
  "DOMContentLoaded",
  function () {
    const checkboxes = document.querySelectorAll(
      "input[type=checkbox][name=categorys]"
    );

    for (var checkbox of checkboxes) {
      checkbox.addEventListener("change", function (event) {
        // event.preventDefault();
        const categoryForm = document.getElementById("categoryForm").submit();
      });
    }
  },
  false
);
