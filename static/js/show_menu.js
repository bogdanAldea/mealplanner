const showMenu = (togglerId, navId, bodyId, headerId) => {
    const toggler = document.getElementById(togglerId),
    navEl = document.getElementById(navId),
    bodyEl = document.getElementById(bodyId),
    headerEl = document.getElementById(headerId)

    if (toggler && navEl && bodyEl && headerEl) {
        toggler.addEventListener('click', () => {
            navEl.classList.toggle('show')
            toggler.classList.toggle('bx-x')
            bodyEl.classList.toggle('desktop-padding')
            headerEl.classList.toggle('desktop-padding')
        })
    }
}

showMenu('toggler-icon', 'sidebar', 'body', 'header')