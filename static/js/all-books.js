var currentSelectedCategory = 'All';
var maturityRating = 'All';
var currentBooks = [];
var currentfilterBooks= [];
var categoryMap = new Map();
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

const sortCategory = (books) => {
    categoryMap = new Map()
    categoryMap.set('All', 0)
    books.forEach(book => {
        if(categoryMap.has('All')){
            categoryMap.set('All', categoryMap.get('All') + 1)
        }
        book.categories.forEach(category => {
            if(categoryMap.has(category)){
                categoryMap.set(category, categoryMap.get(category) + 1);
            }
            else{
                categoryMap.set(category, 1);
            }
        })
    })
    categoryMap = Array.from(categoryMap.entries()).sort((a, b) => b[1] - a[1]);
}

const setBooksPreference = () => {
    if(currentSelectedCategory == 'All'){
        wrapperSetBooks(currentBooks);
    }
    else{
        currentfilterBooks = currentBooks.filter(book=> {
            if(!book.categories){
                return false;
            }
            if(book.categories.includes(currentSelectedCategory)){
                return true;
            }
            return false;
        });
        wrapperSetBooks(currentfilterBooks);
    }
}
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
            <div  class="flex-auto flex flex-col  ">
                    <div class="  w-full px-2 grow flex  min-h-[13rem]  py-2">
                        <img class="rounded-md h-[10rem] aspect-[3/4]" src=${book.thumbnail? book.thumbnail : NO_THUMBNAIL_URL } alt="">
                        <div class=" pl-3 flex-1 flex flex-col min-h-full ">
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
                    <div class="mt-auto border-b border-[#460C90] w-full opacity-20 ${isFirstLast? ' hidden ' : isSecondLast? `${res.length % 2 == 0? ` md:hidden ` :
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

const addEventListenerToCategoryButton = (cmap) => {
    for(let[key,value] of cmap){
        const category = key
        const id = category + "-books-btn";
        const element = document.getElementById(id);
        element.addEventListener('click', ()=>{
            setSelectedCategory(category);
        })
    }
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
    setBooksPreference()
}

const setCategoriesBar = (categoriesData) => {
    const categoriesContainer = document.getElementById('categories-container');
    let innerHTML = ``;
    for(let[key,value] of categoriesData){
        category = key
        const sanitizedCategory = `${category}`; 
        const categoryHTML = `<div onclick='' id="${sanitizedCategory}-books-btn" class="py-1 mr-4 text-black text-xs ${currentSelectedCategory === sanitizedCategory ? 'border-b-2 border-black' : ''} ">${category}</div>`;
        innerHTML += categoryHTML
    }
    categoriesContainer.innerHTML = innerHTML;
    handleCategoriesContainerResize()
    addEventListenerToCategoryButton(categoriesData)
}

const getCategories =  () => {
    //console.log('sini')
    sortCategory(currentBooks)
    setCategoriesBar(categoryMap)
}
window.addEventListener("DOMContentLoaded", async ()=> {
    try {
        await getBooks();
        getCategories();
        categoriesOverlay.classList.remove('hidden');
        homeContent.classList.remove('hidden');
        loadingSpinner.style.display = 'none';
        handleCategoriesContainerResize();
    } catch (error) {
        
    }
})