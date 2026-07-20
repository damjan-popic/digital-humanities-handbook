document.addEventListener("DOMContentLoaded", () => {
  const launchers = document.querySelectorAll("[data-search-launcher]");
  launchers.forEach((launcher) => {
    launcher.addEventListener("click", (event) => {
      event.preventDefault();
      const toggle = document.querySelector("label[for='__search']");
      if (toggle) {
        toggle.click();
        window.setTimeout(() => {
          const input = document.querySelector(".md-search__input");
          if (input) input.focus();
        }, 120);
      }
    });
  });
});
