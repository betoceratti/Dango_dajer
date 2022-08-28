   

    const btn_form = document.getElementById('show');

    btn_form.addEventListener('click',()=>{
        document.querySelector('.form_blog').classList.toggle('active');
    });
    

   //funcion para controlar los eventos en este caso de los links para eliminar articulos
    const botones = document.querySelectorAll('.botones');

    botones.forEach(boton =>{
        boton.addEventListener('click',function(e){
            // console.log(e);
            let confirmacion = confirm("Estas seguro de eliminar el articulo ? ");
            if(!confirmacion){
                e.preventDefault();
            }
        })
        // console.log(boton);

    })
   
   






