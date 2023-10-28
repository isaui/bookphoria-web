async function refreshBookList() {
  const loading = document.getElementById('loading-text')
  try {
      loading.style.display = 'flex';
      const bookList = document.getElementById("book-list")
      const response = await fetch("/profile/get-books")
      console.log("====================================")
      console.log(response)
      const data = await response.json()
      console.log(data)
      console.log("====================================")
      bookList.innerHTML = ""
      if (data.books.length == 0){
          bookList.innerHTML = `<p>You have no books :(</p>`
      } else {
          data.books.forEach(book => {
              bookList.innerHTML += "\n" +
                  `<img src="${book.thumbnail}" class="h-full w-auto object-contain shadow-xl"/>`
          })
      }
      loading.style.display = 'none';
  } catch (err) {
      console.log(err)
      loading.style.display = 'none';
  }
}

window.addEventListener("DOMContentLoaded", async ()=>{
  await refreshBookList()
  console.log("DOM Loaded")
  homeContent.classList.remove("hidden"); 
  function addBook() {
      fetch("{% url 'Dashboard:add_book' %}", {
          method: "POST",
          body: new FormData(document.querySelector('#add-book-form'))
      }).then(refreshBookList)

      document.getElementById("add-book-form").reset()
      document.querySelector('[data-modal-hide="add-book-modal"]').click()
  }

  document.getElementById("submit_new_book").onclick = addBook

  function validateSize(input) {
      const fileSize = input.files[0].size / 1024 / 1024; // in MiB
      if (fileSize > 2) {
          alert('File size exceeds 2 MiB');
          input.value = '';
      }
  }
})