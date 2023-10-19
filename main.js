const workTag = document.querySelector("#works");
const workPanel = document.querySelector(".works-panel");
const body = document.querySelector("body");

workTag.addEventListener("click", (e) => {
  e.stopPropagation();
  workPanel.classList.toggle("d-none");
});

body.addEventListener("click", (e) => {
  if (window.innerWidth < 900){
    workPanel.classList.add("d-none");
  }
});
