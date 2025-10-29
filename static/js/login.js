// Duas APi, pois temos 2 rotas e bancos diferentes
const apiUrl = "http://127.0.0.1:5036/clientes/login";

async function loginUsuario() {
    const user = {
        email: document.getElementById("email").value,
        senha: document.getElementById("senha").value
    };

    try {
        // Verificando se o cliente está no BD
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(user)
        });
        const data = await response.json();

        console.log(data)

        //verificando se a senha está errada ou não
        if (data.message === "senha invalida") {
            errorMessage = "senha invalida";
            alert("Senha inválida");
            return;
        }

        // Caso a requisição para cliente não funcione 
        if (data.success === true) {
            console.log("Login de cliente realizado")

            // Página de redirecionamento para depois do login, alterar depois
            // Alert só para voces saberem que deu certo
            alert("Login realizado!")

            // Redirecionamento genérico
            window.location.href = "http://127.0.0.1:5036/"
            
            return;
        }

        

        // Se o login não foi bem-sucedido, exibe a mensagem de erro apropriada
        alert(data.message || "ERRO AO REALIZAR LOGIN");



    } catch (error) {
        console.error("Erro ao realizer login:", error);

    }


}