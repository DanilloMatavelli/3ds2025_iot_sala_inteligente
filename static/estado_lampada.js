async function atualizarStatus() {
    const resposta = await fetch('https://sala-inteligente1-nsrl.onrender.com/get/estado_lampada');
    const dados = await resposta.json();
    const estado = dados.ESTADO_LAMPADA;

    const statusLampada = document.getElementById('status');
    const icone_Lampada = document.getElementById('icone');

    if (estado === 'LIGADO') {
        statusLampada.innerText = 'Ligada';
        icone_Lampada.innerText = '💡';
    }
    else {
        statusLampada.innerText = 'Desligada';
        icone_Lampada.innerText = '💤';
    }
}

// Atualizar a cada 2 segundos
setInterval(atualizarStatus, 2000);
window.onload = atualizarStatus;