var currentBooks = [];
const dropdownButton = document.getElementById("dropdownDelayButton");
const dropdownCurrentText = document.getElementById("dropdownButtonText")
const dropdownContent = document.getElementById("dropdownDelay");
const dropdownButtonsContent = dropdownContent.querySelectorAll("button");
const dropdownIcon = document.getElementById("homeDropdownIcon");
const homeContent = document.getElementById("homeContent");
const MAX_HOMEPAGEBOOKS = 12;
var currentValue = 'Terbaru';
var isDropdownOpen = false;
const NO_THUMBNAIL_URL = 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/495px-No-Image-Placeholder.svg.png?20200912122019'
const getBooks = async ()=>{
    const loading = document.getElementById('loading-text');
    try {
        loading.style.display = 'flex';
        const resJson = await fetch('/get-books/', {
            method:'GET'
        });
        const res = await resJson.json();
        console.log(res);
        const books = res.books;
        books.reverse();
        setCarouselBooks(getRandomElementsFromArray(books, 5));
        setHomepageBooks(books);
        currentBooks = [...books];
        loading.style.display = 'none';
    } catch (error) {
        loading.style.display = 'none';
    }

}

window.addEventListener("load", ()=>{
    dropdownCurrentText.textContent = currentValue;
    establishDropdownSelectedValueColor();
})

document.addEventListener("click", (event) => {
// Periksa apakah elemen yang diklik adalah dropdownButton
if (event.target !== dropdownContent) {
    // Periksa apakah elemen yang diklik adalah dropdownContent atau elemen dalam dropdownContent
    if (!dropdownContent.contains(event.target)) {
        // Jika bukan dropdownButton, dropdownContent, atau elemen dalam dropdownContent yang diklik, maka tutup dropdownContent
        closeDropdown();
    }
}
});

const sortBooksBy = (identifier) => {
    const newBooks = [...currentBooks];
    if(identifier == "Terbaru"){
        setHomepageBooks(newBooks)
    }
    else if(identifier == "Terlama"){
        newBooks.reverse();
        setHomepageBooks(newBooks);
    }
}

const establishDropdownSelectedValueColor =  ()=>{
    dropdownButtonsContent.forEach(button => {
        if(button.getAttribute("data-value") != currentValue){
            button.classList.remove("bg-purple-600");
        }
        else {
            if(!button.classList.contains("bg-purple-600")){
                button.classList.add("bg-purple-600")
            }
        }
    })
}

const openDropdown = () => {
    dropdownContent.classList.remove('hidden');
    isDropdownOpen = true;
    dropdownIcon.setAttribute("transform", "scale(1, -1)");
}

const toggleDropdown = () => {
    if(isDropdownOpen){
        closeDropdown()
    }
    else{
        openDropdown()
    }
}

const closeDropdown = () => {
    if(!dropdownContent.classList.contains('hidden')){
        dropdownContent.classList.add('hidden')
    }
    isDropdownOpen = false;
    dropdownIcon.setAttribute("transform", "scale(1, 1)");
}
dropdownButton.addEventListener("click", (event) => {
    toggleDropdown();
    event.stopPropagation();
    
});

dropdownButtonsContent.forEach(button => {
    button.addEventListener("click", ()=>{
        const newValue = button.getAttribute("data-value");
        currentValue = newValue;
        dropdownCurrentText.textContent = currentValue;
        establishDropdownSelectedValueColor();
        sortBooksBy(newValue)
        closeDropdown();
    })
});


function getRandomElementsFromArray(array, numElements) {
    const newArray = [...array];
    const shuffledArray = newArray.sort(() => 0.5 - Math.random()); // Mengacak urutan array
    return shuffledArray.slice(0, numElements); // Mengambil sejumlah elemen
  }

const setCarouselBooks = (res) => {
    const carousel = document.getElementById('carousel');
    let booksString = '';
    try {
        res.forEach((book, index)=>{
            const bookString = `<div class="flex w-full h-full justify-center  items-center flex-shrink-0 ">
            <div  class="my-auto">
                <div class=" px-2  flex  min-h-[13rem] max-w-[24rem] md:max-w-[32rem] lg:max-w-[48rem] py-2">
                    <img class=" rounded-md h-[11rem] md:h-[18rem] aspect-[3/4]" src=${book.thumbnail? book.thumbnail : NO_THUMBNAIL_URL } alt="">
                    <div class=" pl-3 flex-1 flex flex-col  ">
                        <div class="flex   justify-between items-start ">
                        <div class="mt-1 mr-2">
                        <h1 class=" font-bold  text-sm line-clamp-2 text-[#460C90]">${book.title? book.title : 'No Title'}</h1>
                        <h1 class="text-[#C52A62] text-xs line-clamp-2">
                        ${book.authors.length > 0 ? book.authors.map((author,index)=>{
                            if(index == book.authors.length - 1){
                                return `<a>${author}</a><span>.</span>`
                            }
                            return `<a>${author}</a><span>, </span>`
                        }) : 'Unknown'}
                        </h1>
                    </div> 
                            <div class="ml-auto flex flex-col items-center justify-center">
                                <div class=" fas fa-heart text-red-500 text-lg">
                                </div>
                                <h1 class="text-xs">1024</h1>
                            </div>
                        </div>
                        <div class="text-xs text-black mt-1 line-clamp-1">
                            Created by <span class="text-[#460C90]">Isa Citra</span>
                        </div>
                        <div class="mt-1 flex items-center space-x-2">
                            <div class="rating text-yellow-400 text-sm">
                                <span class="fas fa-star"></span>
                                <span class="fas fa-star"></span>
                                <span class="fas fa-star"></span>
                                <span class="fas fa-star"></span>
                                <span class="fas fa-star-half-alt"></span>
                            </div> 
                            <div class="text-xs text-black line-clamp-1">
                                415 Reviews
                            </div>
                        </div>    
                        <div  class="mt-1 text-[#C52A62] text-xs line-clamp-2">
                        ${book.categories.length > 0 ? book.categories.map((category,index)=>{
                            if(index == book.categories.length - 1){
                                return `<a>${category}</a><span>.</span>`
                            }
                            return `<a>${category}</a><span>, </span>`
                        }) : 'No categories'}
                        </div>
                        <div  class=" text-black text-xs md:text-sm line-clamp-2 md:line-clamp-4">
                            ${book.description? book.description : 'No description'}
                        </div>
                        <div  class="mt-1 text-[#C52A62] font-bold text-sm line-clamp-2">
                        ${book.currencyCode && book.price? `${book.currencyCode} <span>${book.price}</span>` : 'FREE'}
                        </div>
                        <a href="{% url 'Bookphoria:book_detail' book.pk %}" class="mt-auto w-full max-w-[16rem] flex items-center justify-center text-sm md:text-base text-white py-2 rounded-md bg-slate-950">
                            <button>
                                Lihat Detail Buku
                            </button
                        </a>

                    </div>
                </div>
                </div>
    
          </div>`;
          booksString += bookString;
        });
        carousel.innerHTML = booksString;

        // document.addEventListener("DOMContentLoaded", function() {
        //     const detailButtons = document.querySelectorAll('.lihat-detail-buku');
        //     detailButtons.forEach((button, index) => {
        //         button.addEventListener('click', () => {
        //             const bookId = button.getAttribute('data-book-id');
        //             window.location.href = `/book/${bookId}/`;
        //         });
        //     });
        // });
        

        
    } catch (error) {
        console.log(error)
    }
}
const setHomepageBooks = (res) => {
    const booksCardContainer = document.getElementById('book-cards-container');
    res = res.slice(0,MAX_HOMEPAGEBOOKS);
    let booksString = '';
    try {
        res.forEach((book,index) => {
            const isFirstLast = index == res.length -1;
            const isSecondLast = index == res.length -2;
            const isThirdLast = index == res.length -3;
            const bookString = `
            <div  class="">
                    <div class=" px-2  flex  min-h-[13rem]  py-2">
                        <img class="rounded-md h-[10rem] aspect-[3/4]" src=${book.thumbnail? book.thumbnail : NO_THUMBNAIL_URL } alt="">
                        <div class=" pl-3 flex-1 flex flex-col">
                            <div class="flex  justify-between items-start ">
                            <div class="mt-1 mr-2">
                            <h1 class=" font-bold  text-sm line-clamp-2 text-[#460C90]">${book.title? book.title : 'No Title'}</h1>
                            <h1 class="text-gray-400 text-xs line-clamp-2">
                            ${book.authors.length > 0 ? book.authors.map((author,index)=>{
                                if(index == book.authors.length - 1){
                                    return `<a>${author}</a><span>.</span>`
                                }
                                return `<a>${author}</a><span>, </span>`
                            }) : 'Unknown'}
                            </h1>
                        </div>  
                                
                                <div class="ml-auto flex flex-col items-center justify-center">
                                    <div class=" fas fa-heart text-red-500 text-lg">
                                    </div>
                                    <h1 class="text-xs">1024</h1>
                                </div>
                            </div>
                            
                            <div class="text-xs text-gray-400 mt-1">
                                Created by <span class="text-[#460C90]">Isa Citra</span>
                            </div>
                            <div class="mt-1 flex items-center space-x-2">
                                <div class="rating text-yellow-400 text-sm">
                                    <span class="fas fa-star"></span>
                                    <span class="fas fa-star"></span>
                                    <span class="fas fa-star"></span>
                                    <span class="fas fa-star"></span>
                                    <span class="fas fa-star-half-alt"></span>
                                </div> 
                                <div class="text-xs text-gray-400">
                                    415 Reviews
                                </div>
                            </div>    
                            <div  class="mt-1 text-gray-400 text-xs line-clamp-2">
                                ${book.categories.length > 0 ? book.categories.map((category,index)=>{
                                    if(index == book.categories.length - 1){
                                        return `<a>${category}</a><span>.</span>`
                                    }
                                    return `<a>${category}</a><span>, </span>`
                                }) : 'No categories'}
                            </div>
                            <div  class="mt-2 text-[#C52A62] font-bold text-sm line-clamp-2">
                                ${book.currencyCode && book.price? `${book.currencyCode} <span>${book.price}</span>` : 'FREE'}
                            </div>
                            <div class="mt-auto ml-auto text-xs text-gray-500">
                                2 hari yang lalu
                            </div>
                        </div>
                    </div>
                    <div class="border-b border-[#460C90] w-full opacity-20 ${isFirstLast? ' hidden ' : isSecondLast? `${res.length % 2 == 0? ` md:hidden ` :
                     res.length % 3 == 0? ` lg:hidden `:' '}`: isThirdLast? `${res.length % 3 == 0? ` lg:hidden `: ``}` : ``}">
                    </div>
                    </div>
            `
            booksString += bookString;
        });
        booksCardContainer.innerHTML = booksString;
    
    } catch (error) {
        console.log(error)
    }
}

window.addEventListener("DOMContentLoaded", async ()=>{
    await getBooks();
    homeContent.classList.remove("hidden");
})