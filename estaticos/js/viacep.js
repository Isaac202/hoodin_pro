$(document).ready(function() {
    $('#id_cep').on('input', function(e) {
        let cep = $('#id_cep').val();
        if (cep.length == 9) {
            //Consulta o webservice viacep.com.br/
            $.getJSON("https://viacep.com.br/ws/" + cep + "/json/", function(dados) {
                console.log('Buscando')
                if (!("erro" in dados)) {
                    console.log('deu certo')
                        //Atualiza os campos com os valores da consulta.
                    $("#id_logradouro").val(dados.logradouro);
                    $("#id_bairro").val(dados.bairro);
                    $("#id_complemento").val(dados.complemento);
                    $("#id_localidade").val(dados.localidade);
                    $("#id_uf option[value=" + dados.uf + "]").attr('selected', 'selected');
                    let uf = $("#id_uf option[value=" + dados.uf + "]").html()
                    $("#uf_col input.select-dropdown").val(uf);

                }
            });
        }
    });
});