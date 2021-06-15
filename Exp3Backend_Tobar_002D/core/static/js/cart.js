var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var productoId = this.dataset.product
        var accion = this.dataset.action
        console.log('productoId:', productoId, 'accion:', accion)

        console.log("USER: ", user)
        if (user === 'AnonimousUser') {
            console.log('el usuario no esta autenticado')
        } else {
            updateOrdenUsuario(productoId, accion)
        }
    })
}

function updateOrdenUsuario(productoId, accion){
    console.log('Usuario autenticado, enviando datos...')

    var url = '/update_item/'
    console.log('URL:', url)
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productoId':productoId, 'accion':accion})        
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}

function addCookieItem(productoId, accion) {
    console.log('No esta loggeado')

    if (accion == 'add') {
        if (carrito[productoId] == undefined) {
            carrito[productoId] = {'cantidad':1}
        } else {
            carrito[productoId]['cantidad'] += 1
        }
    }
    if (accion == 'remove') {
        carrito[productoId]['cantidad'] -=1
        
        if (carrito[productoId]['cantidad'] <= 0) {
            console.log('Articulo eliminado')
            delete carrito[productoId]
        }
    }
    console.log('Carrito: ', carrito)
    document.cookie = 'carrito=' + JSON.stringify(carrito) + ";domain=;path=/"
    location.reload()
}