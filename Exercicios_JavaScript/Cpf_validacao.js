class cpfValidacao {
    constructor(cpf) {
        this.cpf = cpf;
        const cpfArray = Array.from(cpf).map(Number);
        
        function calculoPrimeiroDigito(cpfArray) {
            return cpfArray.slice(0, 9).reduce((ac, valor, index) => {
                let mutiplicador = 10 - index;
                let calculo = mutiplicador * valor + ac;
                if (mutiplicador === 2) {
                    let resultado = calculo % 11;
                    return (resultado < 2) ? 0 : resultado - 11;
                }
                return calculo;
            }, 0);
        }
        
        function calculoSegundoDigito (cpfArray) {
            return cpfArray.slice(0, 9).concat(calculoPrimeiroDigito(cpfArray)).reduce((ac, valor, index) => {
                let mutiplicador = 11 - index;
                let calculo = mutiplicador * valor + ac;
                if (mutiplicador === 2) {
                    let resultado = calculo % 11;
                    return (resultado < 2) ? 0 : 11 - resultado;
                }
                return calculo;
            }, 0);
        }

        const cpfGeradoPelosCalculos = (`${cpf.slice(0, 9)}${calculoPrimeiroDigito(cpfArray)}${calculoSegundoDigito(cpfArray) }`);
        
        if (cpfGeradoPelosCalculos === cpf) {
            console.log(`${cpf} é um CPF Válido `);
        } 
        else {
            console.log(`${cpf} é um CPF Inválido `);
        }
    }
}

new cpfValidacao('13311976606');

