(function () {
    'use strict';
    let forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
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