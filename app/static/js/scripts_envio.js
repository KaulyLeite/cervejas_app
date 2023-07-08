function gerar(id) {
    let conteudo = document.getElementById(id).innerHTML;
    let nome = 'Pedido - {{ pedido }}';
    let iframe = document.createElement('iframe');
    let bootstrap = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"' +
        ' rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"' +
        ' crossorigin="anonymous">';
    let styles_path = '/static/css/styles_envio.css';
    let styles_envio = '<link href="' + styles_path + '" rel="stylesheet" type="text/css">';

    iframe.style.display = 'none';
    document.body.appendChild(iframe);

    let doc = iframe.contentDocument || iframe.contentWindow.document;
    let temp = '<!DOCTYPE html><html lang="pt-BR"><head><title>' + nome + '</title>' +
        bootstrap + styles_envio + '</head><body>' + conteudo + '</body></html>';

    doc.open();
    doc.write(temp);
    doc.close();

    iframe.onload = function () {
        let head = document.getElementsByTagName('head')[0];
        let style = document.createElement('style');

        style.innerHTML = bootstrap;
        head.appendChild(style);
        iframe.contentWindow.print();
        document.body.removeChild(iframe);
    };
}

function home() {
    window.location.href = '/';
}