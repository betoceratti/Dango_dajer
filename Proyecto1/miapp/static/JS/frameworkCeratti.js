//CODIGO PARA INICIALIZAR AOS 
AOS.init();

//FUNCION PARA DESPLEGAR EL NAV 
const nav = document.getElementById('btn');
nav.addEventListener('click', () => {
   document.getElementById('nav').classList.toggle('active');
});       
//FUNCION PARA DESPLEGAR EL MENU RESPONSIVE
const desplegable = document.getElementById('btn1');
desplegable.addEventListener('click', () => {
   document.getElementById('menu').classList.toggle('active');
});       


//COMIEMZA EL TYPED ESCRITURA
const typed = new Typed('.typed', {
    strings: [
       '<i class="web">DAJER</i>',
       '<i class="web">PRODEMEX</i>'
       /*'<i class="web">Hipotecario</i>',
       '<i class="web">Auto</i>'*/
    ],
    
    //stringsElement: '#cadenas-texto', // ID del elemento que contiene cadenas de texto a mostrar.
    typeSpeed: 75, // Velocidad en mlisegundos para poner una letra,
    startDelay: 300, // Tiempo de retraso en iniciar la animacion. Aplica tambien cuando termina y vuelve a iniciar,
    backSpeed: 75, // Velocidad en milisegundos para borrrar una letra,
    smartBackspace: true, // Eliminar solamente las palabras que sean nuevas en una cadena de texto.
    shuffle: false, // Alterar el orden en el que escribe las palabras.
    backDelay: 1500, // Tiempo de espera despues de que termina de escribir una palabra.
    loop: true, // Repetir el array de strings
    loopCount: false, // Cantidad de veces a repetir el array.  false = infinite
    showCursor: true, // Mostrar cursor palpitanto
    cursorChar: '|', // Caracter para el cursor
    contentType: 'html', // 'html' o 'null' para texto sin formato
    });





//FUNCION PARA DESPLEGAR EL FORMULARIO DE CONACVTO
const bform = document.getElementById('btnform');
bform.addEventListener('click', () => {
   
   document.querySelector('.form').classList.toggle('show');
});       




//Codigo para el formulario      

function login(){
   let email = document.getElementById('email').value;
   let mensaje = document.getElementById('mensaje').value;
   let buzon = document.getElementById('buzon');
 
   if(email == "robertoceratti@gmail.com" && mensaje != ""){
       buzon.innerHTML = "Tu mensaje se ha enviado con exito";
       buzon.classList.add('success');
       localStorage.email = email;
       localStorage.message = mensaje;
       clear();
       change();
     
 
   }else{
       // alert("Error en el envio");
       buzon.innerHTML = "Error en el envio";
       buzon.classList.add('error');
       clear();
       change();
 
       
   }        
 }; 
 
 
 function clear() {
   let email = document.getElementById('email');
   let mensaje = document.getElementById('mensaje');
 
   email.value = "";
   mensaje.value = "";
 
 }
 
 
 // setTimeout(()=>{},2000);
 
 function change(){
 setTimeout(() => {
   let buzon = document.getElementById('buzon');
   buzon.innerHTML = "";    
 },3000);
 
 };
 
 
 //FUNCION PARA ACTIVAR LOS ENLACES

const enlaces = document.querySelectorAll('.nav .navbar li a');
enlaces.forEach((enlace)=>{
enlace.addEventListener('click',(evento)=>{
  evento.preventDefault;
  enlaces.forEach((elemento)=> elemento.classList.remove('activo'));
  evento.target.classList.add('activo');

});
});


//FUNCION PARA AL ABRIR WINDOWS CARGUE EL LOADER
window.addEventListener("load", () =>{

   document.getElementById("loader").classList.toggle("out");
   
   });



//Codigo para que el nav aparezac o no segun el scroll

let ubicaconPricipal =window.pageYOffset;

window.addEventListener('scroll',()=>{

   let desplazamientoActual = window.pageYOffset;
   let alturaPage = document.documentElement.scrollTop;
   //alert(desplazamientoActual);
   //alert(alturaPage);

   if(ubicaconPricipal > desplazamientoActual){
      document.getElementsByTagName("nav")[0].style.top ="0px"
      // document.getElementById('nav').style.top="0px"
     
  }else{
      //  document.getElementById('nav').style.top="-100px"
      document.getElementsByTagName("nav")[0].style.top ="-100px"
     // document.getElementsByTagName("nav")[0].style.background ="white"
     
  }
  ubicaconPricipal = desplazamientoActual;

 


});