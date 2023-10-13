/*
* Controls the opening and closing of the mobile side menu on pages and dashboard
* */
const accountMobileMenuOpen = document.getElementById('account-mobile-menu-open');
const accountMobileMenuClose = document.getElementById('account-mobile-menu-close');
const accountMobileMenuContent = document.getElementById('account-mobile-menu-content');
if (accountMobileMenuOpen !== null || accountMobileMenuClose !== null || accountMobileMenuContent !== null) {
    accountMobileMenuOpen.addEventListener('click', () => {
        accountMobileMenuContent.classList.toggle('hidden');
        // avoid the scroll of the web and show only the menu
        document.body.classList.remove('overflow-auto');
        document.body.classList.add('overflow-hidden');
    });
    accountMobileMenuClose.addEventListener('click', () => {
        accountMobileMenuContent.classList.toggle('hidden');
        // avoid the scroll of the web and show only the menu
        document.body.classList.add('overflow-auto');
        document.body.classList.remove('overflow-hidden');
    });
}