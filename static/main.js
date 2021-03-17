const copyBtns = document.querySelectorAll(".btn-site");
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

copyBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    const { siteid } = btn.dataset;
    const url = "/";
    fetch(url, {
      method: "POST",
      mode: "same-origin",
      headers: {
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({ site_id: siteid }),
    })
      .then((res) => res.json())
      .then((data) => {
        navigator.clipboard.writeText(data.msg);
        btn.innerHTML = '<i class="fas fa-check"></i>';
        setInterval(
          () => (btn.innerHTML = '<i class="fas fa-copy"></i>'),
          2000
        );
      });
  });
});
