<script>
export default {
  name: 'MenuComponent',
  // other component options...
}
</script>


<template>
    <label for="show-menu" class="show-menu">Desplegar Menu</label>
        <input type="checkbox" id="show-menu" role="button">
            <ul id="menu">
            <li><a href="#">Log Out</a></li>
            <li>
                <a href="#">Mostrar Tareas &nbsp;￬</a>
                <ul class="hidden">
                    <li><a href="#">Universidad</a></li>
                    <li><a href="#">Ejercicio</a></li>
                </ul>
            </li>
            <li>
                <a href="#">Productos &nbsp;￬</a>
                <ul class="hidden">
                    <li><a href="#">Diseño web</a></li>
                    <li><a href="#">Diseño gràfico</a></li>
                    <li><a href="#">Marketing</a></li>
                </ul>
            </li>
            <li><a href="#">Noticias</a></li>
            <li><a href="#">Contacto</a></li>
        </ul>
</template>
  
<style>
/* Menu styles */
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    position: relative;
}

li {
    display: inline-block;
    float: left;
    margin-right: 1px;
}

/* Style for links */
li a {
    display: block;
    min-width: 140px;
    height: 35px;
    text-align: center;
    line-height: 35px;
    font-family: 'Inter', sans-serif; /* Update font */
    color: var(--vtc-c-text-dark-3); /* Text color from palette */
    background: rgba(255, 255, 255, 0.07); /* Background color */
    text-decoration: none;
    border-radius: 2px; /* Rounded corners */
}

li:hover a {
    background: linear-gradient(to right, #ff512f, #f09819); /* Gradient from palette */
}

li:hover ul a {
    background: rgba(255, 255, 255, 0.13);
    color: var(--color-text);
}

/* Hover for dropdown links */
li:hover ul a:hover {
    background: linear-gradient(to right, #ff512f, #f09819); /* Gradient from palette */
    color: var(--color-text);
}

/* Hide dropdown links until needed */
li ul {
    display: none;
}

/* Make dropdown links vertical */
li ul li {
    display: block;
    float: none;
}

li ul li a {
    width: auto;
    min-width: 100px;
    padding: 0 19px;
}

/* Display dropdown menu on hover */
ul li a:hover + .hidden,
.hidden:hover {
    display: block;
}

/* Menu button styles */
.show-menu {
    font-family: 'Inter', sans-serif;
    font-weight: bold;
    text-decoration: none;
    color: var(--vtc-c-text-dark-3);
    background: linear-gradient(to right, #ff512f, #f09819); /* Gradient from palette */
    text-align: center;
    padding: 7px 0;
    display: none;
    border-radius: 10px; /* Rounded corners */
}

input[type=checkbox] {
    display: none;
}

/* Show menu when invisible checkbox is checked */
input[type=checkbox]:checked ~ #menu {
    display: block;
}


/*Estilo responsivo ancho menor de 750px*/

@media screen and (max-width : 770px){
	/*Hacer que los vínculos desplegables aparezcan en línea*/
	ul {
		position: static;
		display: none;
	}
	/*Crear espacio vertical*/
	li {
		margin-bottom: 1px;
	}
	/*Todos los enlaces del menú de ancho completo*/
	ul li, li a {
		width: 100%;
	}

	.show-menu {
		display:block;
		cursor:pointer;
	}
}
</style>