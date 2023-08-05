(function () {
    'use strict';
    let forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                let inputs = form.querySelectorAll('.form-control');
                let camposEmBranco = false;

                inputs.forEach(function (input) {
                    if (input.value.trim() === '') {
                        camposEmBranco = true;
                        input.classList.add('is-invalid');
                        input.classList.remove('is-valid');
                    } else {
                        input.classList.remove('is-invalid');
                        input.classList.add('is-valid');
                    }
                });

                if (camposEmBranco) {
                    event.preventDefault();
                    event.stopPropagation();
                    form.scrollIntoView({behavior: 'smooth', block: 'start'});
                    return;
                }

                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                    form.scrollIntoView({behavior: 'smooth', block: 'start'});
                }

                let qtdeInputs = document.getElementsByClassName("input-qtde");
                let soma = 0;
                for (let i = 0; i < qtdeInputs.length; i++) {
                    soma += Number(qtdeInputs[i].value);
                }

                if (soma === 0) {
                    alert('A quantidade de pelo menos um produto precisa ser maior que zero!');
                    event.preventDefault();
                    event.stopPropagation();
                    form.scrollIntoView({behavior: 'smooth', block: 'start'});
                }

                form.classList.add('was-validated');
            }, false);
        });
})();

(function () {
    'use strict';
    const estados = [
        {nome: 'Acre', sigla: 'AC'},
        {nome: 'Alagoas', sigla: 'AL'},
        {nome: 'Amapá', sigla: 'AP'},
        {nome: 'Amazonas', sigla: 'AM'},
        {nome: 'Bahia', sigla: 'BA'},
        {nome: 'Ceará', sigla: 'CE'},
        {nome: 'Distrito Federal', sigla: 'DF'},
        {nome: 'Espírito Santo', sigla: 'ES'},
        {nome: 'Goiás', sigla: 'GO'},
        {nome: 'Maranhão', sigla: 'MA'},
        {nome: 'Mato Grosso', sigla: 'MT'},
        {nome: 'Mato Grosso do Sul', sigla: 'MS'},
        {nome: 'Minas Gerais', sigla: 'MG'},
        {nome: 'Pará', sigla: 'PA'},
        {nome: 'Paraíba', sigla: 'PB'},
        {nome: 'Paraná', sigla: 'PR'},
        {nome: 'Pernambuco', sigla: 'PE'},
        {nome: 'Piauí', sigla: 'PI'},
        {nome: 'Rio de Janeiro', sigla: 'RJ'},
        {nome: 'Rio Grande do Norte', sigla: 'RN'},
        {nome: 'Rio Grande do Sul', sigla: 'RS'},
        {nome: 'Rondônia', sigla: 'RO'},
        {nome: 'Roraima', sigla: 'RR'},
        {nome: 'Santa Catarina', sigla: 'SC'},
        {nome: 'São Paulo', sigla: 'SP'},
        {nome: 'Sergipe', sigla: 'SE'},
        {nome: 'Tocantins', sigla: 'TO'}
    ];

    const input = document.getElementById('estado');

    estados.forEach(function (estado) {
        const option = document.createElement('option');
        option.value = estado.sigla;
        option.textContent = estado.nome;
        input.appendChild(option);
    });
})();

function formatarTelefone() {
    const input = document.getElementById('telefone');
    let telefone = input.value.replace(/\D/g, '');
    const tamanho = telefone.length;

    if (tamanho > 10) {
        telefone = telefone.replace(/^(\d{2})(\d{5})(\d{4}).*/, '($1) $2-$3');
    } else if (tamanho > 6) {
        telefone = telefone.replace(/^(\d{2})(\d{4})(\d{0,4}).*/, '($1) $2-$3');
    } else if (tamanho > 2) {
        telefone = telefone.replace(/^(\d{2})(\d{0,5})/, '($1) $2');
    }

    input.value = telefone;
}

function validarQtde(input) {
    if (input.value.length > 2) {
        input.value = input.value.slice(0, 2);
    }
}

function decrementar(input_qtde) {
    const input = document.getElementById(input_qtde);
    if (input.value > 0) {
        input.value = parseInt(input.value) - 1;
    }
}

function incrementar(input_qtde) {
    const input = document.getElementById(input_qtde);
    if (input.value < 99) {
        input.value = parseInt(input.value) + 1;
    }
}