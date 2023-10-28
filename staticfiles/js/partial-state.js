var isMobileNavbarOpen = false;
let isSidebarOpen = false;

window.addEventListener('resize', ()=>{
    const mobileSearchButton = document.getElementById("mobile-search-button");
    const mobileSearchBar = document.getElementById("mobile-search-bar");
    if(!mobileSearchButton || !mobileSearchBar){
        return;
    }
    const screenWidth = window.innerWidth;
    let maxWidth = 1024;
    if(screenWidth >= maxWidth){
        if(isMobileNavbarOpen){
            closeMobileNavbar()
        }
    }
})
window.addEventListener('resize', ()=>{
    const sidebar = document.getElementById('sidebar');
    if(!sidebar){
        return;
    }
    const screenWidth = window.innerWidth;
    if(screenWidth >= 768){
        if(isSidebarOpen){
            closeSidebar()
        }
    }
})


const openSidebar = ()=> {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.remove('-translate-x-[100%]');
    sidebar.classList.add('translate-x-0');
    isSidebarOpen = true;
}
const closeSidebar = ()=> {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.remove('translate-x-0');
    sidebar.classList.add('-translate-x-[100%]');  
    isSidebarOpen = false
}
const toggleMobileNavbar = () => {
    if(isMobileNavbarOpen){
        closeMobileNavbar()
    }
    else{
        openMobileNavbar()
    }
}
const closeMobileNavbar = () => {
    const mobileSearchButton = document.getElementById("mobile-search-button");
    const mobileSearchBar = document.getElementById("mobile-search-bar");
    mobileSearchButton.innerHTML = `<svg class="w-4 h-4" onclick="toggleMobileNavbar();" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
</svg>
<div onclick="openSidebar();" class="md:hidden ml-6 fas fa-bars  text-white">
</div>`;
    mobileSearchBar.classList.remove('translate-y-0');
    mobileSearchBar.classList.add('-translate-y-48');
    isMobileNavbarOpen = false;    
}
const openMobileNavbar = () =>{
    const mobileSearchButton = document.getElementById("mobile-search-button");
    const mobileSearchBar = document.getElementById("mobile-search-bar");
    mobileSearchButton.innerHTML = `<div onclick="toggleMobileNavbar();" class="fas fa-times w-4 h-4 text-red-500"></div>`;
    mobileSearchBar.classList.remove('-translate-y-48');
    mobileSearchBar.classList.add('translate-y-0');
    isMobileNavbarOpen = true;
}
