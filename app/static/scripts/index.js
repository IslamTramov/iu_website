window.addEventListener("load", () => {
  const scroller = document.getElementById("scroller");
  if (!scroller) return;
  scroller.addEventListener("click", () => {
    window.scrollTo({ top: window.innerHeight, behavior: "smooth" });
  })
});
