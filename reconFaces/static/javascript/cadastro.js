var carregaFoto1 = $(function(){
    $('#id_foto1').change(function(){
        const file = $(this)[0].files[0]
        const fileReader = new FileReader()
        fileReader.onloadend = function(){
            $('#foto1').attr('src', fileReader.result)
            }
            fileReader.readAsDataURL(file)
    })
})

var carregaFoto2 = $(function(){
    $('#id_foto2').change(function(){
        const file = $(this)[0].files[0]
        const fileReader = new FileReader()
        fileReader.onloadend = function(){
            $('#foto2').attr('src', fileReader.result)
            }
            fileReader.readAsDataURL(file)
    })
})

var carregaFoto3 = $(function(){
    $('#id_foto3').change(function(){
        const file = $(this)[0].files[0]
        const fileReader = new FileReader()
        fileReader.onloadend = function(){
            $('#foto3').attr('src', fileReader.result)
            }
            fileReader.readAsDataURL(file)
    })
})

var carregaFoto4 = $(function(){
    $('#id_foto4').change(function(){
        const file = $(this)[0].files[0]
        const fileReader = new FileReader()
        fileReader.onloadend = function(){
            $('#foto4').attr('src', fileReader.result)
            }
            fileReader.readAsDataURL(file)
    })
})

var carregaFoto5 = $(function(){
    $('#id_foto5').change(function(){
        const file = $(this)[0].files[0]
        const fileReader = new FileReader()
        fileReader.onloadend = function(){
            $('#foto5').attr('src', fileReader.result)
            }
            fileReader.readAsDataURL(file)
    })
})

var carregaFoto6 = $(function(){
    $('#id_foto6').change(function(){
        const file = $(this)[0].files[0]
        const fileReader = new FileReader()
        fileReader.onloadend = function(){
            $('#foto6').attr('src', fileReader.result)
            }
            fileReader.readAsDataURL(file)
    })
})