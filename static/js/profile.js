const getUser = async (username) => {
  const loading = document.getElementById('loading-text')
  try {
    loading.style.display = 'flex';
    const res = await fetch(`/get-user/${username}`, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });
    const data = await res.json();
    if (data) {
      console.log(data);
      document.querySelector("#username").textContent = data.username;
      document.querySelector("#email").textContent = data.email;
    }
    loading.style.display = 'none';
  } catch (err) {
    loading.style.display = 'none';
    console.log(err);
  }
}

window.addEventListener("DOMContentLoaded", async ()=>{
  const params = new URLSearchParams(window.location.search);
  const username = params.get('username');
  console.log(username)
  await getUser(username);
  homeContent.classList.remove("hidden"); 
})