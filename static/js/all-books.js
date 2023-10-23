var categories = ['All'];
var currentSelectedCategory = 'All';
var currentBooks = [];
var currentfilterBooks= [];
const categoriesContainer = document.getElementById('categories-container');
const nextCategoriesButton = document.getElementById('next-categories-button');
const prevCategoriesButton = document.getElementById('prev-categories-button');
const loadingSpinner = document.getElementById('loading-text');
const homeContent = document.getElementById('homeContent');
const booksCardContainer = document.getElementById('books-card-container');
const categoriesOverlay = document.getElementById('categories-overlay');
let lastScrollPosition = window.scrollY;
let isScrolling;
const scrollThreshold = 100;

window.addEventListener('scroll', () => {
    const currentScrollPosition = window.scrollY;
    clearTimeout(isScrolling);
    isScrolling = setTimeout(()=> {
        categoriesOverlay.style.transform = 'translateY(0)';
    }, scrollThreshold)
    if (currentScrollPosition > lastScrollPosition) {
      // Scrolling down
      
      categoriesOverlay.style.transform = 'translateY(-400%)';
    } else {
      // Scrolling up
      categoriesOverlay.style.transform = 'translateY(0)';
      
    }
  
    lastScrollPosition = currentScrollPosition;
    
  });


const wrapperSetBooks = (res) => {
    loadingSpinner.style.display = 'flex';
    setTimeout(()=> {
        setBooks(res);
        loadingSpinner.style.display = 'none';
    }, 1200)
}

const getBooks = async ()=>{
    try {
        const resJson = await fetch('/get-books/', {
            method:'GET'
        });
        const res = await resJson.json();
        console.log(res);
        const books = res.books;
        books.reverse();
        currentBooks = [...books];
        setBooks(currentBooks)

    } catch (error) {
        console.log(error)
    }
}

const setBooks = (res) => {
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

const handleCategoriesContainerResize = () => {
    if(categoriesContainer.scrollWidth > categoriesContainer.clientWidth){
        if(categoriesContainer.clientWidth + categoriesContainer.scrollLeft 
        >= categoriesContainer.scrollWidth){
            prevCategoriesButton.style.display = 'flex';
            nextCategoriesButton.style.display = 'none';
        }
        else if(categoriesContainer.scrollLeft === 0){
            prevCategoriesButton.style.display = 'none';
            nextCategoriesButton.style.display = 'flex';
        }
        else{
            prevCategoriesButton.style.display = 'flex';
            nextCategoriesButton.style.display = 'flex';
        }
    }
    else{
        prevCategoriesButton.style.display = 'none';
            nextCategoriesButton.style.display = 'none';
    }
}
nextCategoriesButton.addEventListener('click', () => {
// Menggeser scroll ke kanan
categoriesContainer.scrollLeft += 450; // Sesuaikan dengan jumlah pixel yang Anda inginkan
});

// Menambahkan event listener pada tombol "prev" (kiri)
prevCategoriesButton.addEventListener('click', () => {
    // Menggeser scroll ke kiri
categoriesContainer.scrollLeft -= 450; // Sesuaikan dengan jumlah pixel yang Anda inginkan
});
categoriesContainer.addEventListener("scroll", handleCategoriesContainerResize);
window.addEventListener("resize", handleCategoriesContainerResize);
window.addEventListener("DOMContentLoaded", handleCategoriesContainerResize)

const addEventListenerToCategoryButton = () => {
    categories.forEach(category=>{
        const id = category + "-books-btn";
        const element = document.getElementById(id);
        element.addEventListener('click', ()=>{
            setSelectedCategory(category);
        })
    })
}

const setSelectedCategory = (category) => {
    const lastSelectedCategoryElement = document.getElementById(currentSelectedCategory+'-books-btn');
    const nextSelectedCategoryElement = document.getElementById(category+'-books-btn');
    if(lastSelectedCategoryElement == nextSelectedCategoryElement){
        return;
    }
    if(lastSelectedCategoryElement){
        lastSelectedCategoryElement.classList.remove('border-b-2')
        lastSelectedCategoryElement.classList.remove('border-black')
    }
    if(nextSelectedCategoryElement){
        nextSelectedCategoryElement.classList.add('border-b-2')
        nextSelectedCategoryElement.classList.add('border-black')
    }
    currentSelectedCategory = category;
    if(category == 'All'){
        wrapperSetBooks(currentBooks);
        return;
    }
    currentfilterBooks = currentBooks.filter(book=> {
        if(!book.categories){
            return false;
        }
        if(book.categories.includes(category)){
            return true;
        }
        return false;
    });
    wrapperSetBooks(currentfilterBooks);
    
}

const setCategoriesBar = (categoriesData) => {
    const categoriesContainer = document.getElementById('categories-container');
    let innerHTML = ``;
    categoriesData.forEach((category, index)=>{
        const sanitizedCategory = `${category}`; 
        const categoryHTML = `<div onclick='' id="${sanitizedCategory}-books-btn" class="py-1 mr-4 text-black text-xs ${currentSelectedCategory === sanitizedCategory ? 'border-b-2 border-black' : ''} ">${category}</div>`;
        innerHTML += categoryHTML
    })
    categoriesContainer.innerHTML = innerHTML;
    handleCategoriesContainerResize()
    addEventListenerToCategoryButton()
}

const getCategories = async () => {
    try {
        const resJson = await fetch('/get-categories/');
        const res = await resJson.json();
        res.categories.sort()
        categories = ['All', ...res.categories]
        setCategoriesBar(categories)

    } catch (error) {
        
    }
}
window.addEventListener("DOMContentLoaded", async ()=> {
    await getCategories();
    categoriesOverlay.classList.remove('hidden');
    await getBooks();
    homeContent.classList.remove('hidden');
    loadingSpinner.style.display = 'none';
    handleCategoriesContainerResize();
})